#!/usr/bin/env python3
"""Inventarios explícitos, sin sobrescritura. verify es siempre de solo lectura.

capture-git registra blobs de un commit exacto; capture-worktree registra bytes
locales compartibles y declara cambios sin commit. No ejecuta código del proyecto.
"""

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]


def git(root, *args):
    return subprocess.check_output(["git", "--no-optional-locks", "-C", str(root), *args], stderr=subprocess.PIPE)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def seguro(root, relativa):
    p = (root / relativa).resolve()
    if not p.is_relative_to(root) or p == root:
        raise ValueError(f"Ruta no válida en inventario: {relativa}")
    return p


def capturar(root, salida, modo, ref):
    salida = salida.resolve()
    if salida.exists():
        raise ValueError("El destino ya existe; no se sobrescribe evidencia")
    if not salida.parent.is_dir():
        raise ValueError("La carpeta de evidencia debe existir y estar autorizada")
    head = git(root, "rev-parse", "--verify", "HEAD^{commit}").decode().strip()
    datos = {"formato": "inventario-repositorio-1", "fecha_utc": datetime.now(timezone.utc).isoformat(), "modo": modo, "head_observado": head}
    archivos = {}
    if modo == "git":
        commit = git(root, "rev-parse", "--verify", ref + "^{commit}").decode().strip()
        entradas = git(root, "ls-tree", "-r", "-z", commit).split(b"\0")
        for entrada in filter(None, entradas):
            meta, nombre = entrada.split(b"\t", 1)
            permisos, tipo, objeto = meta.decode().split()
            if tipo != "blob" or permisos not in ("100644", "100755"):
                raise ValueError("Solo se inventarían archivos regulares; revisar enlaces/submódulos")
            contenido = git(root, "cat-file", "blob", objeto)
            archivos[nombre.decode("utf-8")] = {"sha256": sha(contenido), "bytes": len(contenido), "blob_git": objeto}
        datos.update(commit_fotografia=commit, alcance="Blobs de un commit exacto, no bytes del árbol de trabajo ni aprobación humana")
    else:
        nombres = set(filter(None, git(root, "ls-files", "--cached", "--others", "--exclude-standard", "-z").decode("utf-8").split("\0")))
        for nombre in sorted(nombres):
            p = seguro(root, nombre)
            if p == salida:
                continue
            if p.is_symlink() or not p.is_file():
                raise ValueError(f"Archivo ausente/no regular: {nombre}")
            contenido = p.read_bytes()
            archivos[nombre] = {"sha256": sha(contenido), "bytes": len(contenido)}
        datos.update(alcance="Bytes compartibles locales; incluye modificaciones y archivos nuevos SIN COMMIT. No representa íntegramente HEAD.", excluido_autorreferencia=salida.relative_to(root).as_posix() if salida.is_relative_to(root) else salida.name)
    datos["archivos"] = archivos
    with salida.open("x", encoding="utf-8", newline="\n") as f:
        json.dump(datos, f, ensure_ascii=False, indent=2)
        f.write("\n")
    return {"estado": "CREADO", "modo": modo, "archivos": len(archivos), "salida": str(salida)}


def verificar(root, inventario):
    datos = json.loads(inventario.read_text(encoding="utf-8"))
    if datos.get("formato") != "inventario-repositorio-1":
        raise ValueError("Formato histórico distinto: no se reinterpreta como fotografía nueva")
    diferencias = []
    if datos["modo"] == "git":
        commit = datos["commit_fotografia"]
        resuelto = git(root, "rev-parse", "--verify", commit + "^{commit}").decode().strip()
        if resuelto != commit:
            raise ValueError("Identificador de commit no exacto")
        entradas = {}
        for entrada in filter(None, git(root, "ls-tree", "-r", "-z", commit).split(b"\0")):
            meta, nombre = entrada.split(b"\t", 1)
            entradas[nombre.decode("utf-8")] = meta.decode().split()[2]
        if set(entradas) != set(datos["archivos"]):
            diferencias.append("Conjunto de rutas distinto de la fotografía Git")
        for nombre, registro in datos["archivos"].items():
            blob = entradas.get(nombre)
            if blob != registro.get("blob_git"):
                diferencias.append(nombre)
                continue
            contenido = git(root, "cat-file", "blob", blob)
            if sha(contenido) != registro["sha256"] or len(contenido) != registro["bytes"]:
                diferencias.append(nombre)
    elif datos["modo"] == "worktree":
        for nombre, registro in datos["archivos"].items():
            p = seguro(root, nombre)
            if not p.is_file() or p.is_symlink() or sha(p.read_bytes()) != registro["sha256"] or p.stat().st_size != registro["bytes"]:
                diferencias.append(nombre)
    else:
        raise ValueError("Modo desconocido")
    return {"estado": "OK" if not diferencias else "DIVERGENCIA", "modo": datos["modo"], "archivos": len(datos["archivos"]), "diferencias": diferencias, "alcance": "Verifica las rutas registradas; worktree no certifica ausencia de archivos añadidos después. git exige conjunto exacto del commit."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    sub = parser.add_subparsers(dest="accion", required=True)
    for accion in ("capture-git", "capture-worktree"):
        p = sub.add_parser(accion)
        p.add_argument("--salida", type=Path, required=True)
        if accion == "capture-git":
            p.add_argument("--ref", required=True)
    sub.add_parser("verify").add_argument("inventario", type=Path)
    args = parser.parse_args()
    try:
        if args.accion == "verify":
            resultado = verificar(args.root.resolve(), args.inventario)
        else:
            resultado = capturar(args.root.resolve(), args.salida, "git" if args.accion == "capture-git" else "worktree", getattr(args, "ref", None))
        print(json.dumps(resultado, ensure_ascii=False, indent=2))
        return 1 if resultado["estado"] == "DIVERGENCIA" else 0
    except (ValueError, OSError, KeyError, TypeError, subprocess.CalledProcessError) as error:
        print(json.dumps({"estado": "ERROR", "tipo": type(error).__name__, "detalle": str(error)}, ensure_ascii=False), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
