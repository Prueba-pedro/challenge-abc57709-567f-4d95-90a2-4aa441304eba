# Desarrollo de una API REST para gestión de transacciones bancarias

Necesitamos desarrollar una API REST que gestione transacciones en un sistema bancario. La API debe permitir la creación, lectura, actualización y eliminación de transacciones. Además, debe manejar adecuadamente los errores y asegurar la consistencia de los datos. Los actores involucrados son el originador de créditos, el motor antifraude y el core bancario. La API debe soportar un throughput de 1 500 solicitudes por segundo en hora pico y garantizar una latencia menor a 500ms para el 99% de las solicitudes. Los modos de falla a considerar incluyen timeout del core bancario mayor a 2s y respuestas 5xx del motor antifraude.

## Informacion General

| Campo | Valor |
|-------|-------|
| **Tema** | API REST en el dominio de banca y fintech |
| **Nivel** | junior-l1 |
| **Tipo** | practical |
| **Tiempo estimado** | 8 horas |

## Fases del Reto

### Fase 0: Configuración del Proyecto

**Objetivo:** Obtener el proyecto base funcional enviando el Código Base a un asistente de IA, que lo analizará, corregirá errores y generará un ZIP listo para usar.

**Tiempo estimado:** 15-30 minutos

**Instrucciones:**

- Asegúrate de tener instalado para ejecutar el proyecto: Un IDE o editor de código.
- Copia todo el contenido del campo **Código Base** de este reto — incluyendo el texto de instrucciones que aparece al inicio.
- Abre un asistente de IA (Claude en claude.ai, ChatGPT o Gemini — se recomienda Claude), pega el contenido copiado en el chat y envíalo.
- El asistente analizará los archivos, corregirá errores y generará un archivo ZIP descargable. Descárgalo y extráelo en la carpeta donde quieras trabajar.
- Verifica que el proyecto arranca sin errores.

**Entregable:** El proyecto compila/arranca sin errores.

<details>
<summary>Pistas de conocimiento</summary>

- Copia el Código Base completo incluyendo el texto de instrucciones al inicio — esas instrucciones le indican al asistente exactamente qué hacer con los archivos.
- Si el asistente no genera el ZIP automáticamente al terminar el análisis, escríbele: "genera el ZIP ahora".
- Si el proyecto tiene errores al arrancar, comparte el mensaje de error con el mismo asistente para que lo corrija.

</details>

### Fase 1: Definición de endpoints y modelos de datos

**Objetivo:** Establecer los endpoints necesarios y los modelos de datos para la gestión de transacciones.

**Tiempo estimado:** 2 horas

**Instrucciones:**

- Identificar los endpoints requeridos para la creación, lectura, actualización y eliminación de transacciones.
- Definir los modelos de datos necesarios para representar las transacciones, incluyendo atributos como ID, monto, fecha, estado y relaciones con otros modelos (ej. cuenta, usuario).
- Asegurar que los modelos de datos cumplan con las restricciones del dominio (ej. montos positivos, fechas válidas).

**Entregable:** Documentación de los endpoints y modelos de datos, incluyendo diagramas de relaciones y restricciones.

<details>
<summary>Pistas de conocimiento</summary>

- Considera las relaciones entre transacciones y otros modelos del dominio.
- Piensa en las validaciones necesarias para asegurar la consistencia de los datos.

</details>

### Fase 2: Implementación de endpoints y manejo de errores

**Objetivo:** Implementar los endpoints definidos y manejar adecuadamente los errores.

**Tiempo estimado:** 3 horas

**Instrucciones:**

- Implementar los endpoints para la creación, lectura, actualización y eliminación de transacciones.
- Manejar adecuadamente los errores, incluyendo timeouts y respuestas 5xx, asegurando la resiliencia del sistema.
- Asegurar que la API cumpla con las especificaciones de rendimiento (throughput y latencia).

**Entregable:** Código implementado para los endpoints, incluyendo manejo de errores y pruebas unitarias.

<details>
<summary>Pistas de conocimiento</summary>

- Considera el uso de mecanismos de reintento y caché para mejorar la resiliencia.
- Piensa en cómo puedes medir y asegurar el cumplimiento de las especificaciones de rendimiento.

</details>

### Fase 3: Integración con sistemas externos y pruebas de carga

**Objetivo:** Integrar la API con sistemas externos y realizar pruebas de carga para asegurar el cumplimiento de las especificaciones de rendimiento.

**Tiempo estimado:** 3 horas

**Instrucciones:**

- Integrar la API con el motor antifraude y el core bancario.
- Realizar pruebas de carga para asegurar que la API cumpla con las especificaciones de rendimiento (throughput y latencia).
- Documentar los resultados de las pruebas y cualquier ajuste realizado.

**Entregable:** Código integrado con sistemas externos y documentación de las pruebas de carga realizadas.

<details>
<summary>Pistas de conocimiento</summary>

- Considera el uso de herramientas de pruebas de carga para simular el throughput y latencia requeridos.
- Piensa en cómo puedes ajustar la API para mejorar el rendimiento si no cumple con las especificaciones.

</details>

## Dimensiones Evaluadas

- **queEs**: ¿Qué son los endpoints y modelos de datos en el contexto de una API REST para gestión de transacciones bancarias?
- **paraQueSirve**: ¿Para qué sirven los endpoints y modelos de datos en una API REST para gestión de transacciones bancarias?
- **comoSeUsa**: ¿Cómo se usan los endpoints y modelos de datos para gestionar transacciones en un sistema bancario?
- **erroresComunes**: ¿Cuáles son los errores comunes que pueden ocurrir al implementar una API REST para gestión de transacciones bancarias y cómo se manejan?
- **queDecisionesImplica**: ¿Qué decisiones implica la integración de una API REST con sistemas externos y la realización de pruebas de carga para asegurar el cumplimiento de las especificaciones de rendimiento?

## Criterios de Evaluacion

- Definición clara y concisa de los endpoints y modelos de datos.
- Implementación adecuada de los endpoints y manejo de errores.
- Integración exitosa con sistemas externos y cumplimiento de las especificaciones de rendimiento.

---

*Reto generado automaticamente por Challenge Generator - Pragma*
