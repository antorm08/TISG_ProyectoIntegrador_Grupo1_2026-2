"""Validador local de solo lectura. Contrato POC-02 v1.0, Python 3.12."""

import argparse
import csv
from decimal import Decimal, InvalidOperation
import io
import json
from pathlib import Path
import re

NUMERO = re.compile(r"[+-]?(?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)(?:[eE][+-]?[0-9]+)?\Z")
NO_FINITO = re.compile(r"[+-]?(?:s?nan[0-9]*|inf(?:inity)?)\Z", re.I)
MAX_BYTES = 1024 * 1024


def validar(costos: Path, metrados: Path) -> dict:
    """Devuelve diagnósticos estables sin escribir archivos ni revelar valores."""
    errores = []
    archivos = {}
    claves = {}
    estructuras = []

    def error(archivo, fila, campo, codigo, mensaje):
        errores.append(dict(archivo=archivo, fila=fila, campo=campo,
                            codigo=codigo, mensaje=mensaje))

    def leer(nombre, ruta, numerico):
        archivos[nombre] = {"filas": 0}
        claves[nombre] = {}

        def err(codigo, mensaje, fila=0, campo=""):
            error(nombre, fila, campo, codigo, mensaje)

        try:
            ruta = Path(ruta)
            if ruta.is_symlink() or (ruta.exists() and not ruta.is_file()):
                err("E_ARCHIVO_TIPO", "Se requiere un archivo regular sin enlace simbólico.")
                return False
            with ruta.open("rb") as entrada:
                datos = entrada.read(MAX_BYTES + 1)
        except OSError:
            err("E_LECTURA", "No se pudo leer el archivo.")
            return False
        if len(datos) > MAX_BYTES:
            err("E_LIMITE", "El archivo supera el límite de 1 MiB.")
            return False
        try:
            texto = datos.decode("utf-8-sig", errors="strict")
        except UnicodeError:
            err("E_CODIFICACION", "El archivo debe usar UTF-8 válido.")
            return False
        if not texto.strip():
            err("E_ARCHIVO_VACIO", "El archivo no contiene datos CSV.")
            return False
        lector = csv.reader(io.StringIO(texto, newline=""), strict=True)
        try:
            cabecera = next(lector)
            if len(set(cabecera)) != len(cabecera):
                err("E_CABECERA_DUPLICADA", "Las columnas de cabecera deben ser únicas.")
                return False
            faltantes = sorted({"obra_id", "partida_id", numerico} - set(cabecera))
            if faltantes:
                for campo in faltantes:
                    err("E_COLUMNA_FALTANTE", "Falta una columna obligatoria.", campo=campo)
                return False
            if any(len(c) > 4096 for c in cabecera):
                err("E_FILA_ESTRUCTURA", "La cabecera supera los límites permitidos.")
                return False
            estructura = True
            for fila in lector:
                n = lector.line_num
                archivos[nombre]["filas"] += 1
                if len(fila) != len(cabecera) or any(len(c) > 4096 for c in fila):
                    err("E_FILA_ESTRUCTURA", "La fila no cumple la estructura o los límites.", n)
                    estructura = False
                    continue
                registro = dict(zip(cabecera, fila))
                ids = [registro[c].strip() for c in ("obra_id", "partida_id")]
                ids_validos = True
                for campo, valor in zip(("obra_id", "partida_id"), ids):
                    if not valor:
                        err("E_ID_VACIO", "El identificador no puede estar vacío.", n, campo)
                        ids_validos = False
                    elif len(valor) > 128 or any(ord(c) < 32 for c in valor):
                        err("E_ID_FORMATO", "El identificador no cumple el formato permitido.", n, campo)
                        ids_validos = False
                if ids_validos:
                    clave = tuple(ids)
                    if clave in claves[nombre]:
                        err("E_CLAVE_DUPLICADA", f"Clave repetida; primera aparición en fila {claves[nombre][clave]}.", n, "obra_id,partida_id")
                    else:
                        claves[nombre][clave] = n
                valor = registro[numerico].strip()
                if len(valor) > 128:
                    err("E_NUMERO_FORMATO", "El número no cumple el formato permitido.", n, numerico)
                elif NO_FINITO.fullmatch(valor):
                    err("E_NUMERO_NO_FINITO", "El número debe ser finito.", n, numerico)
                elif not NUMERO.fullmatch(valor):
                    err("E_NUMERO_FORMATO", "El número no cumple el formato permitido.", n, numerico)
                else:
                    try:
                        decimal = Decimal(valor)
                        if not decimal.is_finite():
                            err("E_NUMERO_NO_FINITO", "El número debe ser finito.", n, numerico)
                        elif decimal <= 0:
                            err("E_NO_POSITIVO", "El valor debe ser estrictamente positivo.", n, numerico)
                    except InvalidOperation:
                        err("E_NUMERO_FORMATO", "El número no cumple el formato permitido.", n, numerico)
            if not archivos[nombre]["filas"]:
                err("E_SIN_FILAS", "El archivo solo contiene cabecera.")
                return False
            return estructura
        except csv.Error:
            err("E_CSV", "El contenido CSV está malformado.")
            return False

    for nombre, ruta, campo in [("costos", costos, "costo_real"), ("metrados", metrados, "cantidad")]:
        estructuras.append(leer(nombre, ruta, campo))
    if all(estructuras):
        for nombre, otro, codigo in [("costos", "metrados", "E_SIN_METRADO"), ("metrados", "costos", "E_SIN_COSTO")]:
            for clave in claves[nombre].keys() - claves[otro].keys():
                error(nombre, claves[nombre][clave], "obra_id,partida_id", codigo,
                      "La clave no tiene correspondencia en el otro archivo.")
    errores.sort(key=lambda e: (e["archivo"] != "costos", e["fila"], e["campo"], e["codigo"], e["mensaje"]))
    return {"version_contrato": "1.0", "estado": "INVALIDO" if errores else "VALIDO",
            "archivos": archivos, "errores": errores}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--costos", required=True, type=Path)
    parser.add_argument("--metrados", required=True, type=Path)
    args = parser.parse_args()
    resultado = validar(args.costos, args.metrados)
    print(json.dumps(resultado, ensure_ascii=False, indent=2))
    return 0 if resultado["estado"] == "VALIDO" else 1


if __name__ == "__main__":
    raise SystemExit(main())
