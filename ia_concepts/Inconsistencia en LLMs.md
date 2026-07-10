---
type: concept
tags:
  - llms
  - nlp
  - review
---

## Definición

La **inconsistencia en LLMs** ocurre cuando un modelo genera respuestas muy diferentes para el mismo *[[Prompt engineering|prompt]]* o para *prompts* casi iguales.

No significa necesariamente que todas las respuestas sean falsas. El problema es que el comportamiento percibido por el usuario se vuelve inestable y difícil de confiar.

Es como preguntar dos veces lo mismo a un sistema y recibir dos criterios distintos sin que haya cambiado la información disponible.

## Tipos

Hay dos escenarios comunes:

- **Misma entrada, distinta salida**. El mismo *prompt* produce respuestas diferentes en ejecuciones distintas.
- **Pequeño cambio en la entrada, gran cambio en la salida**. Una variación mínima, como una mayúscula, un orden distinto o una palabra extra, altera mucho la respuesta.

El primer caso suele estar más relacionado con *[[Sampling|sampling]]* y los [[Parámetros de decoding|parámetros de generación]]. El segundo depende también de la sensibilidad del modelo al *prompt*, del contexto y de cómo interpreta la tarea.

## Mitigación

Para reducir inconsistencia con el mismo input:

- Fijar [[Temperatura|temperatura]], *top-p*, *top-k* y otros parámetros de *decoding*.
- Usar una [[Seed en generación|semilla]] fija si está disponible.
- Cachear respuestas para preguntas idénticas.
- Usar *prompts* y formatos más específicos.
- Validar las salidas con tests, parsers o reglas.

Para reducir inconsistencia ante entradas parecidas:

- Normalizar entradas
- Usar instrucciones estables
- Añadir ejemplos con *[[Few-shot prompting|few-shot prompting]]*
- Mantener memoria o contexto relevante
- Evaluar con conjuntos de *prompts* variados, no solo con un ejemplo ideal

## Limitaciones

Fijar parámetros ayuda, pero no garantiza una consistencia perfecta. Puede haber diferencias por *hardware*, paralelismo, cambios del proveedor, versiones del modelo o detalles internos de inferencia.

Además, hacer el sistema más consistente no implica hacerlo más correcto. Una respuesta cacheada o repetible puede seguir siendo incorrecta.

## Errores comunes

- Medir calidad con una sola ejecución por *prompt*.
- Asumir que temperatura 0 elimina toda variación.
- Confundir consistencia con factualidad.
- No probar *prompts* ligeramente perturbados.
- Resolver inconsistencia solo con parámetros sin mejorar instrucciones, contexto o evaluación.

## Preguntas

#flashcards/llms #flashcards/nlp

**¿Qué es la inconsistencia en LLMs?**
?
![[#Definición]]

**¿Qué dos tipos de inconsistencia pueden aparecer en LLMs?**
?
![[#Tipos]]

**¿Cómo se puede mitigar la inconsistencia en LLMs?**
?
![[#Mitigación]]

**¿Por qué fijar parámetros no garantiza consistencia perfecta en LLMs?**
?
![[#Limitaciones]]

**¿Qué errores comunes hay al evaluar inconsistencia en LLMs?**
?
![[#Errores comunes]]
