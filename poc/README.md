# Pruebas de concepto (PoC)

## Estado

No se ejecutó una PoC productiva en Semana 1. La primera entrega define el caso, investiga tendencias y registra decisiones iniciales. Esta carpeta se utilizará cuando el curso requiera validar incertidumbres mediante experimentos.

## Propósito

Una PoC debe responder una pregunta específica y producir evidencia para adoptar, modificar o descartar una decisión. No debe presentarse como una solución productiva.

## Posibles PoC del caso

- Medir una estrategia de consulta analítica sin perjudicar el ERP transaccional.
- Construir indicadores de horas, metrados, costos y rendimientos sobre datos sintéticos.
- Comparar una arquitectura analítica ligera con una plataforma más compleja.
- Evaluar una explicación generada por IA con datos validados y revisión humana.
- Incorporar métricas de observabilidad para localizar cuellos de botella.

## Estructura por experimento

```text
poc/
└── POC-XX-nombre/
    ├── README.md
    ├── datos/
    ├── src/
    ├── pruebas/
    ├── resultados/
    └── evidencias/
```

## Plantilla mínima de una PoC

```md
# POC-XX — Nombre

## Pregunta
¿Qué incertidumbre se desea resolver?

## Hipótesis
Si se aplica X bajo las condiciones Y, se espera observar Z.

## Alcance y exclusiones
Indicar qué se prueba y qué no.

## Datos
Describir origen, anonimización, volumen y limitaciones.

## Métricas
Definir métricas y umbrales antes de ejecutar.

## Procedimiento
Explicar cómo puede reproducirse la prueba.

## Resultados
Registrar valores obtenidos sin ocultar resultados negativos.

## Limitaciones
Indicar qué no puede concluirse.

## Decisión
Adoptar, repetir, modificar, evaluar o descartar.
```

## Reglas

- Utilizar datos sintéticos, simulados o anonimizados.
- No conectar una PoC académica directamente con producción.
- Definir métricas antes de observar los resultados.
- Conservar código, configuración reproducible y evidencia.
- Registrar resultados negativos y limitaciones.
- Relacionar la conclusión con el Technology Radar y el Registro de Decisiones.

