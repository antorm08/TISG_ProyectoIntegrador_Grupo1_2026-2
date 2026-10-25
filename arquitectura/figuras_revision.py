#!/usr/bin/env python3
"""Figuras corregidas v1.1; no sobrescribe los diagramas históricos."""

from svg_lib import (defs, svg, rect, txt, multi, cabecera,
                     C_APP, C_DATA, C_ACTOR, C_GAP, C_INFRA, C_DARK)

A, H = 1320, 860


def flecha(puntos, mid=None):
    """Punta explícita: el renderizador SVG no interpreta marker-end."""
    import math
    x, y = puntos[-1]
    anterior_x, anterior_y = puntos[-2]
    distancia = math.hypot(x - anterior_x, y - anterior_y)
    dx, dy = (x - anterior_x) / distancia, (y - anterior_y) / distancia
    base_x, base_y = x - 12 * dx, y - 12 * dy
    vertices = [(x, y), (base_x - 5 * dy, base_y + 5 * dx),
                (base_x + 5 * dy, base_y - 5 * dx)]
    linea = " ".join(f"{px},{py}" for px, py in puntos)
    punta = " ".join(f"{px},{py}" for px, py in vertices)
    salida = (f'<polyline points="{linea}" fill="none" stroke="#334155" stroke-width="2"/>'
              f'<polygon points="{punta}" fill="#334155"/>')
    if mid:
        salida += txt(mid[0], mid[1], mid[2], size=14, anchor="middle")
    return salida


def base(titulo, sub):
    return [defs(), cabecera(titulo, sub, A),
            txt(35, 815, "Elaboración propia · Grupo 1 · Semana 5 · Revisión v1.1 · 24/10/2026", size=15),
            txt(35, 842, "Leyenda: azul = aplicación/consumo; verde = datos; naranja = personas; gris = límite o control; flecha = flujo/prerrequisito.", size=13)]


def bloque(b, x, y, w, titulo, lineas, color=C_APP, h=120):
    b.append(rect(x, y, w, h, *color))
    b.append(txt(x + 15, y + 30, titulo, size=18, bold=True))
    b.append(multi(x + 15, y + 58, lineas, size=15, anchor="start", lh=22))


def figura_asis():
    b = base("Figura 1. Arquitectura AS-IS — ERP propio", "Hecho aclarado por el equipo: CodeIgniter y MySQL. El resto del escenario se identifica como hipótesis.")
    bloque(b, 40, 115, 1240, "Roles del caso académico", ["Gerencia · Costos/Presupuestos · Obra/Administración · Compras/Logística · TI", "Roles funcionales, no cantidad de personas ni cargos verificados."], C_ACTOR)
    bloque(b, 100, 300, 470, "ERP propio — CodeIgniter", ["Obras, partidas, actividades, tareo, metrados", "y costos: alcance funcional del caso.", "Versiones y componentes internos: por validar."], h=160)
    bloque(b, 750, 300, 470, "MySQL transaccional", ["Registro operacional e histórico del ERP.", "No se asume versión, tamaño ni réplica.", "No se accede al servidor en esta revisión."], C_DATA, h=160)
    b.append(flecha([(570, 380), (750, 380)], mid=(660, 360, "acceso a datos")))
    b.append(flecha([(335, 235), (335, 300)]))
    bloque(b, 100, 520, 470, "Planillas y documentos del escenario", ["Consolidación y criterios locales supuestos.", "Sin productos de ofimática confirmados."], C_GAP)
    bloque(b, 750, 520, 470, "Límites del levantamiento", ["Infraestructura, accesos, backups y APIs:", "desconocidos; no se afirma su ausencia."], C_INFRA)
    bloque(b, 100, 680, 1120, "Brecha académica S-08", ["Los históricos no se reutilizan de forma integrada para presupuestar y comparar previsto–ejecutado."], C_GAP, h=90)
    return svg(A, H, "".join(b))


def figura_flujo():
    b = base("Figura 2. Flujo AS-IS y oportunidad", "Proceso funcional del caso; no es un trazado de transacciones de producción.")
    nodos = [(40, "1. Registrar ejecución", ["Obra → partida → actividad", "Tareo, metrados y costos"], C_APP),
             (480, "2. Conservar histórico", ["ERP propio / MySQL", "Calidad por validar"], C_DATA),
             (920, "3. Consolidar", ["Extractos y planillas", "Práctica hipotética"], C_GAP)]
    for x, titulo, subs, color in nodos:
        bloque(b, x, 180, 350, titulo, subs, color, h=150)
    for x in (390, 830):
        b.append(flecha([(x, 250), (x + 90, 250)]))
    bloque(b, 480, 440, 350, "4. Presupuestar / controlar", ["Comparar previsto y ejecutado", "Revisión humana de Costos"], C_ACTOR, h=150)
    b.append(flecha([(1095, 330), (1095, 400), (655, 400), (655, 440)]))
    bloque(b, 100, 660, 1120, "Brecha y límite de evidencia", ["Sin referencia común reutilizable en el escenario. Hasta 15 días es un supuesto, no medición real.", "La PoC usa datos sintéticos: no prueba ahorro, adopción ni rendimiento de este flujo real."], C_GAP)
    return svg(A, H, "".join(b))


def figura_tobe():
    b = base("Figura 3. TO-BE v0.1 revisada — complemento del ERP", "Piloto sintético; futura integración solo con autorización. No reemplazar ni migrar el ERP.")
    bloque(b, 35, 130, 280, "ERP conservado", ["CodeIgniter / MySQL", "Solo lectura autorizada", "Sin escritura de retorno"], h=140)
    bloque(b, 355, 130, 280, "Extractos por lotes", ["CSV sintético en PoC", "Ventana y límite futuros", "Sin réplica obligatoria"], C_DATA, h=140)
    bloque(b, 675, 130, 280, "Staging / validación", ["SQL/Python versionados", "Unidades, IDs y pruebas", "Conciliación y rechazos"], C_DATA, h=140)
    for x in (315, 635):
        b.append(flecha([(x, 200), (x + 40, 200)]))
    bloque(b, 675, 370, 280, "Destino analítico", ["Hechos y dimensiones", "CSV local en el piloto", "MySQL separado: candidato"], C_DATA, h=140)
    b.append(flecha([(815, 270), (815, 370)]))
    bloque(b, 355, 370, 280, "Modelo / tablero BI", ["Power BI: candidato", "Alternativa local aprobada", "Permisos por obra"], C_DARK, h=140)
    b.append(flecha([(675, 440), (635, 440)]))
    bloque(b, 35, 370, 280, "Revisión humana", ["Costos valida las cifras", "Obra y Gerencia consumen", "No decisión autónoma"], C_ACTOR, h=140)
    b.append(flecha([(355, 440), (315, 440)]))
    bloque(b, 995, 130, 290, "Compartir en SaaS", ["Solo si se aprueba:", "licencia + identidad + RLS", "gateway para fuente privada", "No exponer MySQL a Internet"], C_GAP, h=200)
    bloque(b, 995, 390, 290, "Escalamiento condicional", ["Réplica MySQL / Airflow", "dbt / Prometheus / Grafana", "solo con evidencia y soporte"], C_GAP, h=140)
    bloque(b, 35, 610, 1250, "Controles transversales y fronteras", ["Cuenta restringida · contratos de datos · logs de estado/duración/frescura · pruebas · Git · aprobación humana.", "Fuente operacional y almacenamiento analítico separados; topología real por validar. No hay conexión productiva en esta corrección.", "Fuera de alcance: reemplazo ERP, agentes económicos, RAG, eventos y lakehouse."], C_INFRA, h=155)
    return svg(A, H, "".join(b))


def figura_dependencias():
    b = base("Figura 4. Dependencias del TO-BE revisado", "Prerrequisitos sin duraciones estimadas: no se afirma una ruta crítica calculada.")
    nodos = [
        (40, 130, "F-01 · Alcance y responsables", ["Aprobación y política de datos"], C_ACTOR),
        (360, 130, "E-2 · Contrato de datos", ["Depende de F-01"], C_DATA),
        (680, 130, "E-3 · Extracto aislado", ["Depende de E-2"], C_DATA),
        (1000, 130, "E-4 · Validar / cargar", ["Depende de E-3"], C_DATA),
        (1000, 350, "E-5 · Modelo analítico", ["Depende de E-4"], C_DATA),
        (680, 350, "E-6 · BI y permisos", ["Depende de E-5 y E-1"], C_DARK),
        (360, 350, "E-9 · Evaluar piloto", ["Depende de E-6, E-7 y E-8"], C_ACTOR),
        (40, 350, "E-10 · Revisar / decidir", ["Depende de E-9"], C_GAP),
        (360, 570, "E-8 · Pruebas y revisión", ["Depende de E-2"], C_INFRA),
        (680, 570, "E-1 · Formación", ["Depende de F-01"], C_ACTOR),
        (1000, 570, "E-7 · Logs y recuperación", ["Depende de E-4"], C_INFRA),
    ]
    for x, y, titulo, subs, color in nodos:
        bloque(b, x, y, 280, titulo, subs, color)
    for x in (320, 640, 960):
        b.append(flecha([(x, 190), (x + 40, 190)]))
    b.append(flecha([(1140, 250), (1140, 350)]))
    for x in (1000, 680, 360):
        b.append(flecha([(x, 410), (x - 40, 410)]))
    b.append(flecha([(820, 570), (820, 470)]))
    b.append(flecha([(500, 570), (500, 470)]))
    b.append(flecha([(1140, 570), (1140, 530), (570, 530), (570, 470)]))
    b.append(txt(40, 735, "Cada nodo declara sus dependencias completas; las flechas destacan la secuencia principal y entradas de validación.", size=15))
    b.append(txt(40, 768, "H2/H3 siguen pendientes. No escalar sin medir valor, carga, permisos y capacidad operativa. Radar final v1.0: S14.", size=15))
    return svg(A, H, "".join(b))
