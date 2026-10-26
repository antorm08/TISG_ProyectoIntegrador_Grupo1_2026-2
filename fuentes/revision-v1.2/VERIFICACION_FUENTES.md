# Verificación de fuentes — Revisión académica v1.2

UNMSM — FISI. Tendencias en Ingeniería de Software y Gestión. Grupo 1. S1–S5.
Versión v1.2. Consulta: 25/10/2026. Estado: pendiente de validación humana.

## Alcance

Se consultaron páginas públicas originales usando lectura HTTP; no se enviaron
documentos internos, formularios ni datos personales. Una página consultada no
equivale a inspeccionar el PDF completo enlazado. La IA no es fuente bibliográfica.
Se registra el contenido efectivamente accesible, no una certificación universal.

La bibliografía APA 7 completa está en `documentos/proyecto/Semana5_Hito_I_v1.2.md`,
§12. Los IDs siguientes identifican esas referencias, sin reemplazar autores/años.

| ID | Nivel guía | Fuente específica y URL | Localización verificada | Resultado y uso permitido |
|---|---|---|---|---|
| FV-01 | 1 | Souppaya, Scarfone y Dodson (2022), NIST SP 800-218: https://csrc.nist.gov/pubs/sp/800/218/final | Título, autores, Date Published y Document History | SSDF 1.1 final, febrero 2022; prácticas seguras, no porcentaje de mejora |
| FV-02 | 3 | Microsoft (2026a), On-premises data gateways: https://learn.microsoft.com/en-us/power-bi/connect-data/service-gateway-onprem | Introducción y metadato ms.date 2026-09-18 | Gateway usa conexiones salientes para fuentes no accesibles; no evidencia de gateway instalado |
| FV-03 | 3 | Microsoft (2026b), RLS: https://learn.microsoft.com/en-us/fabric/security/service-admin-row-level-security | Introducción, Use RLS with workspaces y ms.date 2026-05-13 | RLS restringe Viewer, no Admin/Member/Contributor; probar identidades antes de compartir |
| FV-04 | 3 | CodeIgniter Foundation (2022), Database reference: https://codeigniter.com/userguide3/database/index.html | Introducción, índice y pie Last updated Mar 03, 2022 | Soporte de acceso a datos y Query Builder; no demuestra versión instalada del ERP |
| FV-05 | 1 | DORA (2025), State of AI-assisted Software Development: https://dora.dev/research/2025/dora-report/ | Download the 2025 DORA Report y resumen | IA amplifica capacidades existentes; no puntúa esta organización ni fija metas del piloto |
| FV-06 | 3 | Scikit-learn developers (s. f.-a), Data leakage: https://scikit-learn.org/stable/common_pitfalls.html#data-leakage | §§12.2 y 12.2.1 | Información no disponible al predecir no debe intervenir en ajuste; separar referencia y evaluación |
| FV-07 | 3 | Scikit-learn developers (s. f.-b), MAPE: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_percentage_error.html | Definición, Returns y ejemplos | MAPE relativo en librería, multiplicar ×100 para porcentaje; inestable cerca de cero. Aquí se rechazan reales no positivos en lugar de epsilon |
| FV-08 | 3 | Python Software Foundation (s. f.), statistics: https://docs.python.org/3.12/library/statistics.html#statistics.median | Function details: median y advertencia NaN | Mediana como centro robusto; no certifica un estimador de construcción |
| FV-09 | 2 | CAPECE (s. f.), Observatorio: https://www.capece.org.pe/observatorio-ecommerce/ | Encabezado de edición | Página anuncia Comercio Electrónico Perú 2024–2025. No acredita las cifras H1 2026; no se descargó el reporte mediante formulario |
| FV-10 | 2 | Thoughtworks (2025), Data product thinking: https://www.thoughtworks.com/en-us/radar/techniques/data-product-thinking | Last updated Apr 02, 2025, bloque Apr 2025 y aviso de edición | Calidad, consumidores, metadatos y ciclo de vida. Blip no incluido en edición actual; no confundir con Vol. 33 completo |
| FV-11 | 5 | Boyagi (2025), Atlassian research: https://www.atlassian.com/blog/developer/developer-experience-report-2025 | Título, autor, July 9, 2025 y What can teams do? | Diagnosticar fricción con desarrolladores; complemento, no sustento único ni medición del caso |
| FV-12 | 3 | Postman (2025), State of the API: https://www.postman.com/state-of-api/2025/ | Introduction y APIs drive revenue | Página respalda 82 % con algún nivel API-first y 65 % con ingresos de programas API en encuesta; no se extrapolan a la constructora |
| FV-13 | 1 | UNMSM, FISI (2026), guía local `proyectoIntegrador (1).pdf` | pp. 3–8, 13–16 | Obligaciones, seis dimensiones, diseño S4, arquitectura S5 y revisión humana; autoridad normativa |

Postman se clasifica aquí como documentación/reporte propio de fabricante,
no como estándar ni muestra representativa de construcción peruana. CAPECE y
Thoughtworks se usan como observatorio/contexto; no son prueba del caso.

## CAPECE: cada afirmación afectada

Fuente histórica: `entregas/semana-02/TISG_E01_S02_ProyectoIntegrador_2026-09-18.pdf`.

| ID de corrección | Afirmación previa | Localización | Evidencia encontrada | Corrección vigente |
|---|---|---|---|---|
| CAP-01 | 37,6 % de volumen en billeteras, H1 2026 | p. 5, §2.5 | El enlace ofrece otra edición; no se localizó respaldo específico | Retirar cifra y aseveración de estándar de pago |
| CAP-02 | US$19 300 millones, H1 2026 | p. 8, §4.5 | Edición observada 2024–2025, sin apoyo para atribución H1 2026 | Retirar, no sustituir por un número distinto fuera de contexto |
| CAP-03 | Crecimiento 50,4 % | p. 8, §4.5 | No sustentado por el recurso atribuido | Retirar |
| CAP-04 | Más de 1 000 millones de transacciones | p. 8, §4.5 | No sustentado por el recurso atribuido | Retirar |
| CAP-05 | Billeteras como principal medio y mercado como confirmación de D-10 | pp. 8/12, §§4.5/6 | No se acredita esa inferencia con la edición enlazada | D-10 se justifica por alcance contractual supuesto, no mercado |
| CAP-06 | Referencia CAPECE (2026), resultados primer semestre 2026 | pp. 13/15, §§8/10 | Título visible 2024–2025; fecha editorial de página no acreditada | CAPECE (s. f.), Observatorio Ecommerce Perú 2024–2025; recuperación 25/10/2026 |

Texto sustitutivo disponible en Hito I v1.2 §3.2 y material complementario S2
v1.2. La página contiene otras cifras, pero no se incorporan: no se necesita
reemplazar una estadística no sustentada por otra para justificar un alcance
académico contractual. El original se conserva como antecedente, no fuente vigente.

## Borradores, enlaces genéricos y límites conservados

- NIST SSDF 1.2: se abrió https://csrc.nist.gov/pubs/sp/800/218/r1/ipd.
  Encabezado **Initial Public Draft**, publicado 17/12/2025, comentarios cerrados
  30/01/2026. No se declara final por haber terminado los comentarios. Fundamento
  activo: SSDF 1.1 final; borrador solo antecedente identificado.
- Thoughtworks: se usa el blip específico fechado 02/04/2025, no la portada que
  cambia de volumen. El Vol. 33 histórico no fue reinspeccionado íntegramente.
- Atlassian: se precisó artículo, autor y fecha, en vez de citar la portada general.
- Oracle/MySQL, CAPECO y el PDF de AACE: no se reinspeccionaron en esta corrección;
  siguen como antecedentes con límites señalados por la auditoría original.
  No se usan para demostrar carga, cifras sectoriales o metas MAPE de v1.2.
- Literatura académica S1/S4: se conserva su verificación anterior documentada
  en la auditoría; no se afirma nueva lectura completa en esta sesión.
- Se intentó acceder a `https://otexts.com/fpp3/accuracy.html`, pero devolvió una
  respuesta de desafío/captcha HTTP 202 sin el capítulo. **No se cita como fuente
  consultada para las nuevas métricas**. Se usaron las páginas accesibles FV-06/07.
- Las nuevas tolerancias de §5.2 son razonamientos internos posteriores; ninguna
  de estas fuentes garantiza 15 %, 30 %, 70 %, 80 % o cuatro semanas.

## Revisión humana pendiente

El equipo debe abrir los enlaces activos, comprobar fechas y el alcance de cada
inferencia, y aprobar o rechazar los supuestos. Este registro es comprobación
técnica con asistencia IA, no certificación de revisión humana ni aprobación docente.
