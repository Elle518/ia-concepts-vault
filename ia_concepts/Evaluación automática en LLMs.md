---
type: concept
tags:
  - llms
  - metrics
  - review
---

## Definición

La **evaluación automática en LLMs** consiste en medir la calidad de las respuestas de un [[Modelo fundacional|modelo fundacional]] sin depender exclusivamente de evaluadores humanos.

Es necesaria porque las respuestas de los LLMs suelen ser abiertas, variadas y costosas de revisar manualmente.

El objetivo no es eliminar por completo la evaluación humana, sino automatizar partes repetibles del proceso para comparar modelos, detectar regresiones y validar sistemas antes de producción.

## Tipos principales

Hay dos grandes tipos de evaluación automática:

- **[[Evaluación exacta en LLMs|Evaluación exacta]]**: produce un juicio sin ambigüedad bajo una regla definida. Por ejemplo, una respuesta pasa o falla un test, coincide exactamente con una referencia o supera un umbral de similitud.
- **[[Evaluación subjetiva en LLMs|Evaluación subjetiva]]**: produce un juicio dependiente del evaluador, del *prompt*, de la rúbrica o del modelo que se usa como juez.

La diferencia clave es si el resultado queda determinado por una regla verificable o por una valoración.

## Evaluación exacta

La evaluación exacta se usa cuando podemos definir una comprobación automática clara.

Sus subtipos más comunes son:

- ***[[Functional correctness]]***: comprobar si la salida cumple la funcionalidad esperada.
- **[[Evaluación por referencia]]**: comparar la salida con respuestas de referencia.

A su ves, dentro de la evaluación por referencia son comunes:
- ***[[Exact match]]***: exigir coincidencia exacta con una respuesta esperada.
- **[[Similitud léxica]]**: medir solapamiento superficial de tokens, palabras o n-grams.
- **[[Similitud semántica]]**: medir cercanía de significado usando [[Embeddings|embeddings]].

Este tipo de evaluación es más reproducible, pero puede fallar en tareas abiertas donde hay muchas respuestas correctas.

## Evaluación subjetiva

La evaluación subjetiva se usa cuando la calidad no se puede decidir solo con una regla exacta.

El subtipo más común en evaluación automática es *[[AI as a judge]]*, donde otro modelo evalúa la respuesta.

Dentro de *AI as a judge* son comunes:

- **[[Evaluación pointwise con LLM judge]]**: puntuar una respuesta de forma aislada.
- **[[Evaluación pairwise con LLM judge]]**: comparar dos respuestas y elegir la mejor.
- **[[Evaluación con rúbrica]]**: evaluar con criterios explícitos, como factualidad, utilidad, seguridad o formato.

Es flexible para tareas abiertas, pero menos estable, ya que el resultado puede cambiar según el modelo juez, el *prompt*, la rúbrica y el orden de las respuestas.

## Cuándo usar cada tipo

Usaremos evaluación exacta cuando el objetivo pueda verificarse de forma automática: código, SQL, extracción estructurada, preguntas cerradas o respuestas cortas.

Usaremos evaluación subjetiva cuando la calidad dependa de criterios difíciles de reducir a una regla: resumen, redacción, utilidad, tono, razonamiento, factualidad compleja o preferencias de usuario.

En sistemas reales suele convenir combinar ambas, es decir, usar tests exactos para requisitos estrictos y jueces automáticos o humanos para calidad abierta.

## Errores comunes

- Usar solo métricas exactas para tareas abiertas.
- Usar solo *AI as a judge* sin calibrarlo contra humanos o ejemplos etiquetados.
- Comparar modelos sin fijar los *prompts*, [[Parámetros de decoding|parámetros de decoding]], el dataset y el protocolo.
- Optimizar para una métrica que no representa el comportamiento esperado en producción.
- Confundir evaluación automática con evaluación completa del sistema.

## Preguntas

#flashcards/llms #flashcards/metrics 

**¿Qué es la evaluación automática en LLMs?**
?
![[#Definición]]

**¿Cuáles son los dos tipos principales de evaluación automática en LLMs?**
?
![[#Tipos principales]]

**¿Qué subtipos incluye la evaluación exacta en LLMs?**
?
![[#Evaluación exacta]]

**¿Qué subtipos incluye la evaluación subjetiva en LLMs?**
?
![[#Evaluación subjetiva]]

**¿Cuándo conviene usar evaluación exacta y cuándo evaluación subjetiva?**
?
![[#Cuándo usar cada tipo]]

**¿Qué errores comunes aparecen en evaluación automática de LLMs?**
?
![[#Errores comunes]]
