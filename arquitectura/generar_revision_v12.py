#!/usr/bin/env python3
"""Genera únicamente figuras/láminas v1.2; no modifica los históricos."""

from pathlib import Path
import re
import sys
import textwrap

from svg_lib import svg, rect, txt, multi
from figuras_revision import flecha, figura_tobe, figura_dependencias
from render_diagramas import renderizar

ROOT = Path(__file__).resolve().parents[1]
DESTINO = ROOT / "arquitectura/revision-v1.2"
S2 = ROOT / "entregas/semana-02/revision-v1.2"
W, H = 1400, 1000
AZUL = ("#DBEAFE", "#1D4ED8")
VERDE = ("#DCFCE7", "#15803D")
GRIS = ("#F1F5F9", "#64748B")
NARANJA = ("#FFF7ED", "#B45309")


def base(titulo, subtitulo, semana="5"):
    return [txt(30, 39, titulo, size=25, bold=True),
            txt(30, 70, subtitulo, size=17),
            txt(30, 945, f"UNMSM · FISI · Tendencias en Ingeniería de Software y Gestión · Grupo 1 · S{semana} · v1.2 · 25/10/2026", size=15),
            txt(30, 972, "Elaboración propia con asistencia IA · Pendiente de validación humana · No representa inventario empresarial observado", size=14)]


def caja(b, x, y, w, h, titulo, textos, color=AZUL, fs=19):
    b.append(rect(x, y, w, h, *color))
    b.append(txt(x + 15, y + 30, titulo, size=21, bold=True))
    lineas = []
    for texto in textos:
        lineas.extend(textwrap.wrap(texto, width=max(15, int((w - 35) / (fs * .57)))))
    if 60 + len(lineas) * (fs + 6) > h:
        raise ValueError(f"Contenido excede caja: {titulo}")
    b.append(multi(x + 15, y + 63, lineas, size=fs, anchor="start", lh=fs + 6))


def asis():
    b = base("Figura 1. AS-IS: topología lógica académica", "K = stack aclarado por el equipo; S = supuesto del escenario; ND = desconocido. Flecha = acceso/intercambio conceptual.")
    caja(b, 35, 105, 1330, 145, "N1 [S-22] · Puesto/navegador y roles funcionales", [
        "Gerencia · Costos/Presupuestos · Obra/Administración · Compras/Logística · TI.",
        "Dispositivos, sedes, red y autenticación reales: ND. No se inventan equipos ni personas."], NARANJA)
    b.append(flecha([(400, 250), (400, 310)], mid=(660, 285, "F1: usuario–ERP; sesión/permisos por validar")))
    b.append(rect(35, 310, 1330, 370, *GRIS, dash="8 5"))
    b.append(txt(55, 340, "Frontera operacional del ERP [S-22]: nodos lógicos, no servidores físicos confirmados", size=20, bold=True))
    caja(b, 65, 365, 760, 275, "N2 [S] · Entorno de aplicación/PHP", [
        "ERP propio CodeIgniter [K, S-14]. Versión: ND.",
        "Módulos conceptuales: obras, partidas, actividades, tareo/HH, metrados y costos/presupuesto.",
        "Topología y controles de aplicación: supuestos/por levantar."], AZUL)
    caja(b, 975, 365, 355, 275, "N3 · MySQL [K]", [
        "Datos operacionales e históricos.",
        "Versión, hosting, volumen, respaldo y accesos: ND.",
        "Separación lógica [S]."], VERDE, fs=18)
    b.append(flecha([(825, 485), (975, 485)], mid=(900, 464, "F2: datos")))
    b.append(txt(845, 530, "acceso solo", size=17))
    b.append(txt(845, 555, "por app [S]", size=17))
    b.append(flecha([(65, 590), (15, 590), (15, 710), (400, 710), (400, 740)], mid=(650, 716, "F3: exportación fuera del ERP [S-23]")))
    caja(b, 65, 740, 760, 160, "N4 [S-23] · Área de exportación y planillas", [
        "Costos consolida CSV/documentos del escenario; acceso autorizado propuesto.",
        "Sin producto ofimático confirmado; no prueba de interfaz instalada."], GRIS, fs=18)
    caja(b, 975, 740, 355, 160, "Terceros / contexto", [
        "Clientes, proveedores, banca y OSE.",
        "Contratos/API: ND; sin acceso directo a BD."], NARANJA, fs=17)
    b.append(txt(55, 665, "N2/N3 pueden compartir host: no se afirma nube, dos servidores, IP, SO, firewall o red real.", size=18))
    return svg(W, H, "".join(b))


def datos():
    b = base("Figura 2. AS-IS: relaciones conceptuales y granularidad", "Modelo del proceso; no claves foráneas ni relaciones físicas verificadas. Azul/verde = proceso/datos; flecha = asociación o derivación.")
    for x, titulo, lineas in [
        (40, "Obra", ["Identificador y contexto", "Una obra: varias partidas"]),
        (505, "Partida", ["Código + unidad por obra", "Una partida: actividades"]),
        (970, "Actividad", ["Unidad de trabajo", "Fecha/periodo asociado"]),
    ]:
        caja(b, x, 140, 390, 160, titulo, lineas, AZUL)
    b.append(flecha([(430, 220), (505, 220)]))
    b.append(flecha([(895, 220), (970, 220)]))
    caja(b, 40, 410, 390, 190, "Tareo / horas-hombre", ["HH por actividad/periodo", "Identidades anonimizadas", "HH no son costo sin tarifa"], VERDE)
    caja(b, 505, 410, 390, 190, "Rendimientos derivados", ["HH/unidad = HH / metrado", "Productividad = metrado/HH", "Denominador cero: ND"], VERDE)
    caja(b, 970, 410, 390, 190, "Metrados", ["Cantidad y unidad ejecutada", "Mismo contexto/periodo", "No depende del tareo"], VERDE)
    b.append(flecha([(1165, 300), (1165, 350), (235, 350), (235, 410)]))
    b.append(flecha([(1165, 300), (1165, 410)]))
    b.append(flecha([(430, 505), (505, 505)]))
    b.append(flecha([(970, 505), (895, 505)]))
    caja(b, 175, 730, 460, 160, "Costos de ejecución", ["Materiales + mano de obra + otros", "Evitar doble conteo y tarifas inventadas"], AZUL, fs=18)
    caja(b, 815, 730, 460, 160, "Histórico → presupuesto", ["Costo/unidad por obra/partida/periodo", "Comparabilidad antes de reutilizar"], VERDE, fs=18)
    b.append(flecha([(235, 600), (235, 730)]))
    b.append(flecha([(1165, 600), (1165, 670), (550, 670), (550, 730)]))
    b.append(flecha([(635, 810), (815, 810)]))
    b.append(txt(45, 109, "Secuencia: Obra → Partida → Actividad → HH → Metrados/Rendimientos → Costos → Histórico; no causalidad entre mediciones.", size=17))
    b.append(txt(45, 918, "Tareo y metrado se vinculan por obra/partida/actividad/periodo; no por una FK confirmada.", size=18))
    return svg(W, H, "".join(b))


def canvas_s2():
    sys.path.insert(0, str(ROOT / "documentos/proyecto"))
    from artefactos_hito import leer_tablas
    texto = (ROOT / "documentos/proyecto/Semana5_Hito_I_v1.2.md").read_text(encoding="utf-8")
    tabla = next(t for t in leer_tablas(texto) if t[0][0] == "Bloque BMC AS-IS")
    contenido = dict(tabla[1:])
    b = base("S2 · Lámina 1. Business Model Canvas AS-IS", "Caso ficticio. Segmentos = quién compra; canales = cómo se capta/relaciona. ERP = recurso interno, no cliente.", semana="2")
    cajas = [
        ("Socios", 25, 120, 245, 510), ("Actividades", 290, 120, 245, 245),
        ("Recursos", 290, 385, 245, 245), ("Propuesta de valor", 555, 120, 285, 510),
        ("Relación con clientes", 860, 120, 245, 245), ("Canales", 860, 385, 245, 245),
        ("Segmentos", 1125, 120, 250, 510), ("Costos", 25, 665, 665, 225),
        ("Ingresos", 715, 665, 660, 225),
    ]
    for nombre, x, y, w, h in cajas:
        titulo = "Relación" if nombre == "Relación con clientes" else nombre
        texto = contenido[nombre]
        if nombre == "Canales":
            texto = "Comerciales [S]: ventas/sala e invitaciones. Digitales [S]: web, redes, portales y correo al cliente."
        caja(b, x, y, w, h, titulo, [texto], VERDE if nombre in ("Ingresos", "Segmentos") else AZUL, fs=18)
    return svg(W, H, "".join(b))


def lamina(numero, titulo, tarjetas, fuente):
    b = base(f"S2 · Lámina {numero}. {titulo}", "Escenario académico, ERP propio CodeIgniter/MySQL. Propuestas y beneficios no implementados ni medidos.", semana="2")
    for i, (nombre, lineas) in enumerate(tarjetas):
        y = 140 + i * 235
        caja(b, 55, y, 1290, 205, nombre, lineas, [AZUL, VERDE, NARANJA][i % 3], fs=21)
    b.append(txt(55, 900, fuente, size=16))
    return svg(W, H, "".join(b))


def generar():
    DESTINO.mkdir(parents=True, exist_ok=True)
    S2.mkdir(parents=True, exist_ok=True)
    figuras = {"figura-01-arquitectura-as-is": asis(), "figura-02-relaciones-datos": datos()}
    for nombre, funcion in [("figura-03-arquitectura-to-be-v0-1", figura_tobe), ("figura-04-mapa-de-dependencias", figura_dependencias)]:
        contenido = funcion().replace("v1.1 · 24/10/2026", "v1.2 · 25/10/2026")
        contenido = contenido.replace("Alternativa local aprobada", "Alternativa local propuesta")
        contenido = contenido.replace("H2/H3 siguen pendientes.", "H1-v1.2/H2/H3 pendientes.")
        figuras[nombre] = contenido
    for nombre, contenido in figuras.items():
        ruta = DESTINO / (nombre + ".svg")
        ruta.write_text(contenido, encoding="utf-8")
        renderizar(ruta)
    laminas = [canvas_s2(), lamina(2, "Economía: no confundir efectos", [
        ("Ingresos y costos", ["Ingresos: contratos valorizados, venta de unidades y adicionales reconocidos.", "Costos: mano de obra, materiales, equipos, subcontratos, administración y TI."]),
        ("Eficiencia: P-01 y P-03", ["Históricos e integración buscan menos reproceso y discrepancias; todavía sin ahorro real medido.", "No se monetizan horas hipotéticas ni se añaden ingresos por APIs/SaaS."]),
        ("Valor al usuario: P-02", ["Transparencia potencial para el cliente; no garantiza ventas ni ingresos digitales.", "Posventa como relación/actividad, no nuevo flujo sin contrato y evidencia."]),
    ], "Fuente: elaboración propia a partir del Hito I v1.2, §3; supuestos económicos SE-01–SE-10."),
        lamina(3, "Canales, actores y dependencias", [
            ("Canales del escenario", ["Comerciales: fuerza/sala de ventas e invitaciones. Digitales: web, redes, portales y correo al cliente.", "El ERP es soporte interno; pagos bancarios son mecanismo de cobro supuesto."]),
            ("Actores", ["Clientes: contratantes/compradores. Socios: proveedores y subcontratistas.", "Banca y TI: habilitadores. Sector público y obligaciones: según contrato/tratamiento."]),
            ("Dependencias: no inventar integraciones", ["Stack aclarado: CodeIgniter/MySQL. Infraestructura y licencias desconocidas.", "No se afirma una API existente con SUNAT/OSE, banca o proveedores."]),
        ], "Fuente: Hito I v1.2, §§3 y 6; interfaces del escenario, no inventario empresarial."),
        lamina(4, "Oportunidades proporcionales", [
            ("SaaS y plataforma", ["SaaS como consumo potencial condicionado a permisos/costo, no comercializar el ERP.", "Portal acotado de participantes; no marketplace ni efectos de red garantizados."]),
            ("APIs y e-Business", ["Integrar cuando exista consumidor y contrato de datos; CSV basta para la primera PoC.", "Digitalizar compras/documentación antes de exponer servicios externos."]),
            ("e-Commerce: alcance limitado", ["Captación, reserva o pago son posibilidades futuras según contrato; no cierre íntegro prometido.", "Retiradas cifras CAPECE atribuidas a H1 2026 sin respaldo. No se usan para justificar D-10."]),
        ], "Fuentes: Postman (2025); Thoughtworks (2025); Hito I v1.2, §§3/12. No benchmarks internos."),
        lamina(5, "Propuestas y condiciones de avance", [
            ("P-01 · Históricos gobernados", ["Referencias para presupuesto y desvíos. Riesgo: calidad/comparabilidad.", "Protocolo independiente v1.2 diseñado, sin resultados nuevos ni ahorro demostrado."]),
            ("P-02 · Portal acotado", ["Información de avance al cliente. Riesgo: confidencialidad y expectativas.", "Fuera del primer TO-BE; validar demanda, permisos y licencia antes de pilotar."]),
            ("P-03 · Abastecimiento integrado", ["Reducir redigitación. Riesgo: capacidad/dependencia de terceros.", "Diagnosticar proveedores y definir contrato antes de construir APIs; revisión humana pendiente."]),
        ], "Fuente: Hito I v1.2, §§3/8; SSDF 1.1 final, Souppaya et al. (2022).")]
    import pymupdf
    with pymupdf.open() as presentacion:
        for i, contenido in enumerate(laminas, 1):
            ruta = S2 / f"lamina-{i:02}.svg"
            ruta.write_text(contenido, encoding="utf-8")
            renderizar(ruta)
            with pymupdf.open(ruta.with_suffix(".pdf")) as pagina:
                presentacion.insert_pdf(pagina)
        presentacion.set_metadata({"title": "S2 material complementario v1.2 — Grupo 1", "author": "Elaboración propia; validación humana pendiente"})
        presentacion.save(S2 / "Presentacion_S2_v1.2.pdf")


if __name__ == "__main__":
    generar()
