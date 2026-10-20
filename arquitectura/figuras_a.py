#!/usr/bin/env python3
"""Figuras 1 (AS-IS) y 2 (flujo de trabajo)."""

from svg_lib import (T_SUB, T_INK, C_ACTOR, C_APP, C_DATA, C_INFRA, C_EXT, C_GAP,
                     C_SHEET, C_DARK, C_GREY, caja, label_capa, defs, flecha,
                     leyenda, cabecera, marco, svg, rect, txt)


def figura_asis():
    A, H = 1500, 1060
    b = [defs(), cabecera(
        "Figura 1. Arquitectura AS-IS — Constructora Andina S.A.C. (Hito I)",
        "Semanas 1–4 · perímetro on-premise, integraciones manuales y ausencia de plataforma analítica",
        A), marco(A, H)]
    # perímetro on-premise
    b.append(rect(45, 100, 1145, 830, "#F8FAFC", "#94A3B8", dash="8 5"))
    b.append(txt(55, 122, "Perímetro de TI on-premise (2 servidores Hiper-V + NAS)",
                 size=11.5, fill=T_SUB, italic=True))
    b.append(label_capa(60, 125, 150, 24, "Actores"))
    b.append(label_capa(60, 312, 150, 24, "Aplicaciones"))
    b.append(label_capa(60, 596, 150, 22, "Datos"))
    b.append(label_capa(60, 770, 150, 22, "Infraestructura"))
    # actores
    actores = ["Dirección General", "Gerencia de Proyectos", "Jefatura de Costos",
               "Jefatura de Compras", "Superintendencia de Obra",
               "Contabilidad y Finanzas", "Tecnología (2 FTE)", "Auditoría externa"]
    for i, a in enumerate(actores):
        x = 175 + (i % 4) * 255
        y = 155 + (i // 4) * 70
        b.append(caja(x, y, 237, 55, C_ACTOR, a, tsize=12))
    # ERP Odoo 16
    b.append(caja(175, 345, 610, 210, C_APP, "Odoo 16 Enterprise (on-premise)", tsize=15))
    modulos = ["Ventas", "Compras", "Inventario", "Contabilidad", "Manufactura",
               "Proyectos", "RR.HH."]
    for i, m in enumerate(modulos):
        x = 190 + (i % 4) * 148
        y = 390 + (i // 4) * 55
        b.append(caja(x, y, 135, 45, ("#EFF6FF", "#1E40AF"), m, tsize=11.5))
    # otras aplicaciones
    b.append(caja(805, 345, 175, 100, C_SHEET,
                  "Excel 2021 / 365", ["Presupuestos", "Metrados", "Avances"],
                  tsize=13))
    b.append(caja(805, 455, 175, 100, C_SHEET,
                  "SharePoint / Outlook", ["Documentos", "Correos"],
                  tsize=13))
    b.append(caja(995, 345, 185, 210, C_GAP,
                  "Sin plataforma analítica", ["sin almacén corporativo",
                                               "sin gobierno de datos",
                                               "sin observabilidad"],
                  tsize=12.5, dash="8 4"))
    # datos
    datos = [("PostgreSQL 15", ["Base transaccional", "Odoo"]),
             ("Archivos Excel", ["Máster local", "versionado manual"]),
             ("Documentos", ["PDF/Word", "carpetas por proyecto"])]
    for i, (t, s) in enumerate(datos):
        b.append(caja(175 + i * 340, 625, 322, 100, C_DATA, t, s, tsize=13))
    # infraestructura
    infra = ["Servidor 1 · Odoo", "Servidor 2 · BD y réplica manual",
             "NAS on-premise", "Copias de seguridad locales"]
    for i, t in enumerate(infra):
        b.append(caja(175 + i * 255, 800, 240, 95, C_INFRA, t, tsize=12.5))
    # sistemas externos
    b.append(txt(1235, 130, "Sistemas externos", size=12, fill=T_SUB, bold=True))
    b.append(caja(1235, 150, 205, 80, C_EXT, "Proveedor de hosting",
                  ["Servidor en alquiler"], tsize=12))
    b.append(caja(1235, 345, 205, 80, C_EXT, "SUNAT",
                  ["Declaraciones"], tsize=12))
    b.append(caja(1235, 545, 205, 80, C_EXT, "OSE certificado",
                  ["Comprobantes"], tsize=12))
    b.append(caja(1235, 745, 205, 80, C_GAP,
                  "Sin integración API", ["carga manual"], tsize=12, dash="8 4"))
    # integraciones y flechas
    b.append(flecha([(500, 345), (500, 295), (1472, 295), (1472, 585), (1440, 585)],
                    dash="7 4", mid=(1000, 285, "Soporte remoto (acceso manual)")))
    b.append(flecha([(700, 345), (700, 330), (1472, 330), (1472, 585), (1440, 585)],
                    mid=(1080, 322, "Comprobantes electrónicos (JSON/XML)")))
    b.append(flecha([(1300, 545), (1300, 425)],
                    mid=(1300, 470, "Resumen diario")))
    b.append(flecha([(790, 395), (780, 395), (780, 600), (340, 600), (340, 625)],
                    mid=(560, 592, "Reportes XLSX manuales")))
    b.append(flecha([(890, 555), (890, 590), (1000, 590), (1000, 625)],
                    dash="7 4", mid=(950, 582, "Documentos sin estructura")))
    # leyenda
    b.append(txt(60, 940, "Leyenda", size=12.5, bold=True))
    b.append(leyenda(60, 950, [
        ("box", C_ACTOR, "Actor / usuario"), ("box", C_APP, "Aplicación"),
        ("box", C_DATA, "Almacén de datos"), ("box", C_INFRA, "Infraestructura"),
        ("box", C_EXT, "Sistema externo"), ("dashbox", C_GAP, "Brecha / limitación"),
        ("line", None, "Integración con sistema externo"), ("dashed", None, "Proceso manual")]))
    return svg(A, H, "".join(b))


def figura_flujo():
    A, H = 1500, 900
    b = [defs(), cabecera(
        "Figura 2. Flujo de información AS-IS — proyectos en ejecución",
        "Dato operativo nace en ERP y hojas de cálculo; el control de costos llega tarde y con esfuerzo manual",
        A), marco(A, H)]
    b.append(caja(60, 110, 250, 110, C_APP, "ERP Odoo 16",
                  ["Órdenes de compra", "Recepciones", "Facturas"], tsize=14))
    b.append(caja(345, 110, 250, 110, C_DATA, "Base PostgreSQL 15",
                  ["Asientos y stock", "sin histórica analítica"], tsize=14))
    b.append(caja(630, 110, 250, 110, C_APP, "Tareo / horas",
                  ["Excel de asistencia", "carga semanal"], tsize=14))
    b.append(caja(915, 110, 250, 110, C_APP, "Avance físico",
                  ["Metrados manuales", "actas PDF"], tsize=14))
    b.append(caja(1200, 110, 250, 110, C_APP, "Control de costos",
                  ["Cruce manual", "Excel de costos"], tsize=14))
    b.append(caja(60, 490, 250, 110, C_APP, "Compras y contratos",
                  ["Proveedores", "ordens"], tsize=14))
    b.append(caja(345, 490, 250, 110, C_SHEET, "Costos de materiales",
                  ["Presupuesto por partida", "hoja de cálculo"], tsize=14))
    b.append(caja(915, 390, 250, 110, C_SHEET, "Resumen ejecutivo",
                  ["Tablero manual", "sin fuente única"], tsize=14))
    b.append(caja(1200, 390, 250, 110, C_DATA, "Histórico de proyectos",
                  ["Carpeta compartida", "PDF y XLSX"], tsize=14))
    b.append(caja(1200, 520, 250, 110, C_SHEET, "Exportaciones",
                  ["copia y pega", "entre hojas"], tsize=14))
    b.append(caja(1200, 650, 250, 110, C_GAP, "Presupuesto a futuro",
                  ["decisión tardía", "varianza no temprana"], tsize=14, dash="8 4"))
    b.append(caja(630, 650, 250, 110, C_GAP, "Brecha de datos",
                  ["Sin ETL ni modelo", "integraciones invisibles"],
                  tsize=14, dash="8 4"))
    b.append(flecha([(310, 165), (345, 165)], mid=(328, 150, "sync")))
    b.append(flecha([(595, 165), (630, 165)]))
    b.append(flecha([(880, 165), (915, 165)]))
    b.append(flecha([(1165, 165), (1200, 165)],
                    mid=(1182, 150, "cruce")))
    b.append(flecha([(755, 165), (755, 160), (1325, 160), (1325, 390)]))
    b.append(flecha([(310, 545), (345, 545)]))
    b.append(flecha([(595, 545), (630, 530), (750, 530), (750, 430),
                     (915, 430)]))
    b.append(flecha([(1165, 445), (1200, 445)]))
    b.append(flecha([(1325, 500), (1325, 520)]))
    b.append(flecha([(1325, 630), (1325, 650)]))
    b.append(flecha([(880, 705), (1200, 705)], dash="7 4",
                    mid=(1040, 695, "información insuficiente")))
    b.append(txt(60, 830,
                 "Riesgo arquitectónico: el dato viaja por correo y hojas locales; no hay trazabilidad de la transformación "
                 "ni forma confiable de reconstruir un histórico comparable entre proyectos.",
                 size=12, fill=T_SUB, italic=True))
    return svg(A, H, "".join(b))
