# Material complementario S2 — Modelo de negocio v1.2

UNMSM — FISI — Ingeniería de Software. Tendencias en Ingeniería de Software y Gestión.
Grupo 1. Semana 2, revisión integrada al Hito I S5. Versión v1.2. Fecha 25/10/2026.
Estado: **Pendiente de validación humana**. Elaboración propia con asistencia de IA.

Sustituye para uso vigente `entregas/semana-02/Grupo 1 - Proyecto - S2.pdf`, que
permanece histórico. No se reutilizan sus fotos ni iconos de procedencia no identificada.
Fuente del contenido: Hito I v1.2, §§2–3/8. No se afirma que el PDF original fue editado.
Los SVG por lámina son editables; el PDF nuevo se genera directamente, no por Office.

## Lámina 1. Business Model Canvas AS-IS

| Bloque | Contenido del escenario |
|---|---|
| Socios | Proveedores, subcontratistas, proyectistas y entidades financieras |
| Actividades | Presupuestar, ejecutar, tarear, medir, comprar, valorizar y atender posventa contractual |
| Propuesta de valor | Obras/unidades conforme a alcance, plazo, calidad y obligaciones contractuales |
| Relación con clientes | Contrato, reuniones de avance, valorizaciones y posventa |
| Segmentos | Contratantes privados y compradores inmobiliarios; públicos solo cuando corresponda |
| Recursos | Personal, equipos, capital, ERP propio e históricos; cantidades no confirmadas |
| Canales | Comerciales supuestos: fuerza/sala de ventas e invitaciones; digitales supuestos: web, redes, portales y correo al cliente |
| Costos | Mano de obra, materiales, subcontratos, equipos, logística, administración y TI |
| Ingresos | Contratos valorizados, venta de unidades y adicionales reconocidos; no SaaS ni monetización de APIs |

El bloque Segmentos responde quién compra, no cómo llega. Fuerza de ventas,
licitaciones/invitaciones y web son canales del escenario, no clientes.

## Lámina 2. Ingresos, costos, eficiencia y valor

Ingresos: contratos, unidades y adicionales reconocidos. La posventa no se agrega
como nuevo flujo sin contrato. Costos: mano de obra, materiales, equipos y soporte.
P-01/P-03 proponen eficiencia y menos reprocesos; no prometen ingresos nuevos.
P-02 puede mejorar valor percibido; no garantiza ventas ni ahorro inmediato.

## Lámina 3. Canales, actores y dependencias

Comerciales: fuerza/sala de ventas e invitaciones del escenario. Digitales de
mercado: web, redes, portales y correo al cliente, supuestos por validar.
ERP: soporte interno, recurso operativo, no canal comercial al cliente.
Clientes: contratantes/compradores. Socios: proveedores/subcontratistas.
Habilitadores: banca y TI. Regulación depende del contrato/tratamiento de datos.
ERP propio CodeIgniter/MySQL: aclaración del equipo. Hosting, licencias y contratos
API con banca/OSE: desconocidos; no integraciones existentes demostradas.

## Lámina 4. Oportunidades proporcionales

SaaS como consumo potencial, condicionado a costo y permisos; no comercializar ERP.
Plataforma acotada a participantes; no marketplace abierto ni efectos de red asumidos.
APIs para integración pertinente; no obligación de exponer API para un piloto CSV.
e-Business para compras/documentación. e-Commerce solo captación/reserva/pago como
propuesta futura según contrato. Se retiran las cifras CAPECE no respaldadas de H1 2026.

## Lámina 5. Tres propuestas y criterio de avance

P-01: históricos gobernados para presupuesto; riesgo de calidad; protocolo S4 v1.2
sin resultados nuevos. P-02: portal acotado; riesgo de confidencialidad; fuera del
primer TO-BE. P-03: abastecimiento integrado; riesgo de terceros; diagnosticar
capacidad antes de diseñar APIs. Continuar solo con evidencia y revisión humana.

Referencias del material: Postman (2025), 2025 State of the API Report,
https://www.postman.com/state-of-api/2025/; Thoughtworks (2025, 2 de abril), Data product
thinking, https://www.thoughtworks.com/en-us/radar/techniques/data-product-thinking;
Souppaya, M., Scarfone, K., & Dodson, D. (2022), SSDF 1.1 (NIST SP 800-218),
https://doi.org/10.6028/NIST.SP.800-218. Alcance y verificación: Hito I v1.2 §12.
