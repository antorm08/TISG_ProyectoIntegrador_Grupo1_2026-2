#!/usr/bin/env python3
"""Figuras 3 (TO-BE v0.1) y 4 (mapa de dependencias)."""

from svg_lib import (T_SUB, T_INK, C_ACTOR, C_APP, C_DATA, C_INFRA, C_EXT, C_GAP,
                     C_SHEET, C_DARK, C_GREY, C_CLOUD, C_WARN, caja, label_capa,
                     defs, flecha, leyenda, cabecera, marco, svg, rect, txt, multi)


def figura_tobe():
    A, H = 1500, 1060
    b = [defs(), cabecera(
        "Figura 3. Arquitectura TO-BE v0.1 — evolución controlada del AS-IS",
        "Se conserva Odoo 16 como núcleo transaccional; se añade capa analítica, integración explícita y observabilidad",
        A), marco(A, H)]
    # perímetro on-premise
    b.append(rect(45, 100, 945, 830, "#F8FAFC", "#94A3B8", dash="8 5"))
    b.append(txt(55, 122, "Perímetro on-premise (evolución del parque actual)",
                 size=11.5, fill=T_SUB, italic=True))
    b.append(label_capa(60, 128, 150, 24, "Actores"))
    b.append(label_capa(60, 300, 150, 30, "Núcleo transaccional"))
    b.append(label_capa(565, 300, 150, 30, "Capa de datos"))
    b.append(label_capa(60, 585, 150, 30, "Operación y seguridad"))
    # actores
    actores = ["Dirección", "Gerencia de Proyectos", "Jefatura de Costos",
               "Compras", "Obra", "Contabilidad", "Tecnología", "Auditoría"]
    for i, a in enumerate(actores):
        x = 165 + (i % 4) * 203
        y = 160 + (i // 4) * 68
        b.append(caja(x, y, 190, 58, C_ACTOR, a, tsize=12))
    # núcleo transaccional
    b.append(caja(165, 330, 380, 250, C_APP, "Odoo 16 Enterprise (on-premise)",
                  tsize=14.5))
    modulos = ["Ventas", "Compras", "Inventario", "Contabilidad",
               "Manufactura", "Proyectos", "RR.HH."]
    for i, m in enumerate(modulos):
        x = 180 + (i % 2) * 175
        y = 375 + (i // 2) * 50
        b.append(caja(x, y, 160, 42, ("#EFF6FF", "#1E40AF"), m, tsize=11.5))
    b.append(txt(355, 565, "Fuente única de transacciones (sin cambio de negocio)",
                 size=10.5, fill=T_SUB, anchor="middle", italic=True))
    # capa de datos
    b.append(caja(565, 330, 400, 250, C_DATA, "Capa de datos analítica",
                  tsize=14.5))
    datos = [("Réplica PostgreSQL", ["solo lectura", "PostgreSQL 15"]),
             ("Apache Airflow", ["orquestación", "extrae y programa"]),
             ("dbt Core", ["transforma y testea", "modelo versionado"]),
             ("Modelo por proyecto", ["hechos y dimensiones", "gobierno básico"])]
    for i, (t, s) in enumerate(datos):
        x = 580 + (i % 2) * 190
        y = 375 + (i // 2) * 100
        b.append(caja(x, y, 175, 90, ("#ECFDF5", "#059669"), t, s, tsize=12, ssize=10))
    # operación y seguridad
    b.append(caja(165, 615, 800, 145, C_INFRA, "Operación y seguridad",
                  tsize=13.5))
    op = ["Prometheus + Grafana", "GitHub Actions (CI/CD)", "Copias y control de acceso"]
    for i, t in enumerate(op):
        b.append(caja(180 + i * 265, 660, 255, 90, C_GREY, t, tsize=12))
    b.append(caja(165, 780, 800, 100, C_DARK,
                  "Contrato funcional: los sistemas publican datos de negocio "
                  "documentados y versionados", tsize=13))
    # nube
    b.append(rect(1015, 100, 445, 430, C_CLOUD[0], C_CLOUD[1], dash="8 5"))
    b.append(txt(1237, 128, "Nube (SaaS controlado)", size=13, fill=T_SUB,
                 bold=True, anchor="middle"))
    b.append(caja(1035, 145, 405, 120, C_DARK, "Power BI Pro (SaaS)",
                  ["Capa de consumo", "RLS por rol", "modelos por proyecto"],
                  tsize=13.5))
    b.append(caja(1035, 285, 190, 100, ("#EFF6FF", "#1D4ED8"), "Microsoft 365",
                  ["documentos"], tsize=12))
    b.append(caja(1250, 285, 190, 100, C_EXT, "OSE / SUNAT",
                  ["comprobantes"], tsize=12))
    b.append(caja(1035, 405, 405, 110, C_GREY, "Backups cifrados y registro de accesos",
                  ["controles mínimos de seguridad"], tsize=12))
    # fuera de alcance
    b.append(caja(1015, 560, 445, 310, C_GAP,
                  "Fuera del alcance de v0.1 (Evaluar / Esperar)",
                  ["— Eventos y agentes IA generativa",
                   "— Lakehouse / data lake",
                   "— Reemplazo de ERP",
                   "— Integraciones en tiempo real con terceros"],
                  tsize=12.5, dash="8 4"))
    # flechas
    b.append(flecha([(355, 286), (355, 330)],
                    mid=(355, 310, "")))
    b.append(flecha([(545, 455), (565, 455)],
                    mid=(555, 440, "lectura")))
    b.append(flecha([(600, 615), (600, 580)],
                    mid=(600, 597, "observabilidad")))
    b.append(flecha([(965, 400), (1000, 400), (1000, 215), (1035, 215)],
                    mid=(1000, 300, "modelo publicado")))
    b.append(flecha([(965, 340), (1035, 340)],
                    dash="7 4", mid=(1000, 330, "documentos")))
    # leyenda
    b.append(txt(60, 940, "Leyenda", size=12.5, bold=True))
    b.append(leyenda(60, 950, [
        ("box", C_ACTOR, "Actor / usuario"), ("box", C_APP, "Aplicación transaccional"),
        ("box", ("#ECFDF5", "#059669"), "Capa de datos (nueva)"),
        ("box", C_GREY, "Infraestructura / operación"),
        ("box", C_DARK, "Capa de consumo"), ("dashbox", C_GAP, "Fuera de alcance v0.1"),
        ("line", None, "Integración explícita y versionada"),
        ("dashed", None, "Contrato de datos / soporte")]))
    return svg(A, H, "".join(b))


def figura_dependencias():
    A, H = 1500, 1000
    X = [60, 250, 440, 630, 820, 1010, 1200]
    b = [defs(), cabecera(
        "Figura 4. Mapa de dependencias del TO-BE v0.1",
        "Capas de izquierda a derecha: personas → datos → integración → transformación → consumo",
        A), marco(A, H)]
    capas = ["Personas", "Contrato de datos", "Ingesta", "Orquestación",
             "Transformación", "Consumo", "Validación"]
    for i, c in enumerate(capas):
        b.append(txt(X[i] + 80, 118, c.replace("\n", " "), size=11.5, fill=T_SUB,
                     bold=True, anchor="middle"))
    nodos = [
        (X[0], 140, "F-01", "Gobernanza\ndel dato", ["Dueños por dominio", "registro de datos"], C_DARK),
        (X[0], 560, "E-1", "Personas", ["capacitación", "habilidades de datos"], C_ACTOR),
        (X[1], 140, "E-2", "Contrato de datos", ["diccionario", "SLA de datos"], C_DATA),
        (X[2], 140, "E-3", "Réplica PostgreSQL", ["solo lectura", "PostgreSQL 15"], C_DATA),
        (X[3], 140, "E-4", "Apache Airflow", ["orquestación", "extracción"], C_DATA),
        (X[4], 90, "E-5", "dbt Core", ["modelos y tests", "versionado en Git"], C_DATA),
        (X[4], 250, "E-7", "Observabilidad", ["Prometheus", "Grafana"], C_GREY),
        (X[4], 410, "E-8", "CI/CD SSDF", ["GitHub Actions", "controles"], C_GREY),
        (X[5], 90, "E-6", "Power BI Pro", ["modelos", "RLS"], C_DARK),
        (X[6], 250, "E-9", "Validación y\nlínea base", ["KPI piloto", "evidencia"], C_SHEET),
        (X[6], 410, "E-10", "v0.2 / Radar v1.0", ["revisión", "nuevas tecnologías"], C_GAP),
    ]
    for x, y, cod, titulo, subs, col in nodos:
        fill, stroke = col
        b.append(rect(x, y, 160, 110, fill, stroke))
        b.append(txt(x + 80, y + 20, cod, size=11.5, bold=True, anchor="middle"))
        b.append(multi(x + 80, y + 37, titulo.split("\n"), size=11, fill=T_INK, lh=13))
        b.append(multi(x + 80, y + 68, subs, size=9.5, lh=12))
    # dependencias principales (de izquierda a derecha)
    b.append(flecha([(220, 195), (250, 195)]))            # F-01 -> E-2
    b.append(flecha([(410, 195), (440, 195)]))            # E-2 -> E-3
    b.append(flecha([(600, 195), (630, 195)]))            # E-3 -> E-4
    b.append(flecha([(790, 160), (820, 160)]))            # E-4 -> E-5
    b.append(flecha([(790, 185), (805, 185), (805, 305), (820, 305)]))   # E-4 -> E-7
    b.append(flecha([(790, 210), (812, 210), (812, 465), (820, 465)]))   # E-4 -> E-8
    b.append(flecha([(980, 145), (1010, 145)]))           # E-5 -> E-6
    b.append(flecha([(1090, 200), (1090, 225), (1280, 225), (1280, 250)]))  # E-6 -> E-9
    b.append(flecha([(980, 305), (1200, 305)]))           # E-7 -> E-9
    b.append(flecha([(980, 465), (1120, 465), (1120, 300), (1200, 300)]))  # E-8 -> E-9
    b.append(flecha([(1280, 360), (1280, 410)]))          # E-9 -> E-10
    b.append(flecha([(220, 615), (995, 615), (995, 145), (1010, 145)]))   # E-1 -> E-6
    b.append(flecha([(1360, 465), (1440, 465), (1440, 145), (1170, 145)],
                    dash="7 4", mid=(1440, 300, "revisión continua")))
    # restricciones
    b.append(caja(60, 740, 1340, 120, C_WARN,
                  "Restricciones que condicionan el mapa de dependencias",
                  ["— Todo cambio se hace sin interrumpir la operación de Odoo 16.",
                   "— Cada decisión de ADR-01 a ADR-06 desbloquea la columna siguiente del mapa.",
                   "— No se adopta tecnología sin función de negocio definida (requisito del Hito I)."],
                  tsize=12.5, ssize=11))
    b.append(txt(60, 940,
                 "Leyenda: flechas de izquierda a derecha = dependencia obligatoria. "
                 "El mapa muestra el orden mínimo para llegar a un modelo de datos y un tablero piloto confiables.",
                 size=11.5, fill=T_SUB, italic=True))
    return svg(A, H, "".join(b))
