#!/usr/bin/env python3
"""Consolida los registros de la Semana 1 y añade los de la Semana 5 (Hito I).

Lee `Registros_y_Radar_Semana1.xlsx`, agrega filas en Decisiones, Contribuciones,
Supuestos y Fuentes, y escribe `Registros_y_Radar_Semana5.xlsx` (sin dependencias
externas). Incluye renumeración de decisiones S4 (D-06–D-08 → D-11–D-13)
para preservar trazabilidad.

Se reutiliza el parser minimalista de XLSX XML existente.
"""

import os
import zipfile
import xml.etree.ElementTree as ET

NS = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
RNS = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"
BASE = os.path.dirname(os.path.abspath(__file__))
ENTRADA = os.path.join(BASE, "Registros_y_Radar_Semana1.xlsx")
SALIDA = os.path.join(BASE, "Registros_y_Radar_Semana5.xlsx")

NUEVAS = {
    "Decisiones": [
        ["D-06", "18/09/2026", "Adoptar enfoque API-first interno antes de exponer APIs a terceros",
         "Exponer externas desde inicio; punto a punto", "Valor es integración y eficiencia (Postman 2025)", "Equipo", "Inicial"],
        ["D-07", "18/09/2026", "No priorizar provision del ERP o capa analítica como SaaS a terceros",
         "Spin-off vertical para constructoras", "Implica cambiar de negocio", "Equipo", "Inicial"],
        ["D-08", "18/09/2026", "Portal de cliente acotado como componente potencial de valor",
         "Mantener información estrictamente interna", "Afecta bloques 3,4,7 del Canvas", "Equipo", "Inicial"],
        ["D-09", "25/09/2026", "Limitar e-commerce a captación, reserva y pago digital",
         "Venta inmobiliaria completa en línea", "Ticket alto, financiamiento y contrato (CAPECE 2026)", "Equipo", "Inicial"],
        ["D-10", "02/10/2026", "Fijar BI y analítica operacional como tendencia principal (Semana 4)",
         "Arquitectura de datos; IA generativa", "Ataca S-08 y anillo Adoptar del Radar v0.1", "Equipo", "Vigente"],
        ["D-11", "02/10/2026", "Validar H1 con PoC de estimación por históricos sobre datos sintéticos",
         "Encuesta; piloto en producción", "Mide desvío sin riesgo a escala académica", "Equipo", "Vigente"],
        ["D-12", "02/10/2026", "Mantener IA generativa en Probar/Evaluar subordinada a H1 y H2",
         "Priorizar IA como primera capa", "Depende de datos confiables (D-03)", "Equipo", "Vigente"],
        ["D-13", "09/10/2026", "Documentar arquitectura AS-IS/TO-BE v0.1 como evolución por capas (sin reemplazar ERP)",
         "Reemplazo; big bang", "Proporcionalidad, reversibilidad y alineado a ADR-01–ADR-06", "Equipo", "Vigente"],
    ],
    "Contribuciones": [
        ["Anthony Romani", "Consolidación de stakeholders y AS-IS de actores e integraciones (S5)", "Sección 3, Figura 1", "09/10/2026", "Documento: Sección 3; arquitectura/as-is", "Registrado", "-"],
        ["Max Astuhuaman", "Deuda técnica priorizada y ADR-01 a ADR-06 (S5)", "Secciones 4 y 6", "09/10/2026", "Documento: Secciones 4 y 6", "Registrado", "-"],
        ["Guillermo Calle", "TO-BE v0.1, diagramas y mapa de dependencias (S5)", "Secciones 5 y 7", "09/10/2026", "Figuras 1–4; arquitectura/", "Registrado", "-"],
        ["Pablo Mendoza", "Trazabilidad S1–S5, riesgos y consolidación Hito I (S5)", "Secciones 2 y 9", "09/10/2026", "Documento: Secciones 2 y 9; revisión integral", "Registrado", "-"],
    ],
    "Supuestos": [
        ["S-13", "Todo componente del TO-BE requiere función de negocio definida antes de adoptar", "Arquitectura", "Vigente", "No adoptar tecnología por moda (Hito I)", "Equipo (Semana 5)"],
    ],
    "Fuentes": [
        ["F-25", "1", "ISO/IEC/IEEE 42010:2011 Systems and software engineering — Architecture description", "2011", "Descripción arquitectónica y buenas prácticas", "https://standards.ieee.org/ieee/42010/5692/"],
        ["F-26", "2", "Thoughtworks Technology Radar Vol. 33", "2025", "Tendencias y ubicación de anillos", "https://www.thoughtworks.com/radar"],
        ["F-27", "4", "Kruchten P., Nord R.L., Ozkaya I. Technical debt: From metaphor to theory and practice", "2012", "Marco para deuda técnica priorizada", "https://doi.org/10.1109/MS.2012.167"],
    ],
}