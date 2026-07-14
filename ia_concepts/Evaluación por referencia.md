---
type: concept
tags:
  - llms
  - metrics
  - nlp
  - review
---

## Definición

La **evaluación por referencia** o *reference-based evaluation* compara la salida generada por un modelo con una o varias respuestas esperadas. Es una forma de [[Evaluación exacta en LLMs|evaluación exacta]].

Cada ejemplo suele tener el formato `(input, referencia)`, aunque puede haber varias referencias válidas para la misma entrada.

Las respuestas generadas que son más similares a las respuestas de referencia se consideran mejores.

## Subtipos

Hay cuatro formas de medir la similitud entre dos textos abiertos:

1. Pedir a un evaluador (humano o de IA) que juzgue si dos textos son iguales.
2. [[Exact match]]: si la respuesta generada coincide exactamente con una de las respuestas de referencia.
3. [[Similitud léxica]]: qué tan similar se ve la respuesta generada con las respuestas de referencia.
4. [[Similitud semántica]]: qué tan cerca está la respuesta generada de las respuestas de referencia en significado (semántica)

Las respuestas de referencia también se llaman *ground truths*, respuestas canónicas o respuestas esperadas.

Las 3 últimas son métricas diseñadas a mano. Las puntuaciones por coincidencia exacta son binarias (coinciden o no), mientras que las otras dos puntuaciones están en una escala móvil (por ejemplo, entre 0 y 1 o entre –1 y 1).

A pesar de la facilidad de uso y la flexibilidad de la IA como método de evaluación, las métricas de similitud diseñadas a mano todavía se utilizan ampliamente en la industria por su naturaleza exacta.

## Cuándo usarla

Funciona bien cuando hay respuestas correctas conocidas, como traducción, QA con respuestas cortas, extracción de información, *captioning* o tareas con datasets anotados.

También permite comparar modelos de forma repetible si se fija el dataset y la métrica.

## Limitaciones

Dado que este enfoque de evaluación requiere datos de referencia, se ve obstaculizado por la cantidad y la rapidez con la que se pueden generar datos de referencia. Los datos de referencia suelen ser generados por humanos y cada vez más por IA.

Utilizar datos generados por humanos como referencia significa que tratamos el desempeño humano como el *[[Gold standard|gold standard]]*, y el desempeño de la IA se mide en comparación con el desempeño humano.

Los datos generados por humanos pueden ser costosos y llevar mucho tiempo, lo que lleva a muchos a utilizar la IA para generar datos de referencia. Es posible que los datos generados por IA aún necesiten ser revisados por humanos, pero el trabajo necesario para revisarlos es mucho menor que el trabajo necesario para generar datos de referencia desde cero.

La calidad de la evaluación depende de la calidad y cobertura de las referencias.

En tareas abiertas puede haber muchas respuestas correctas que no aparecen en el dataset. En ese caso, una salida válida puede recibir mala puntuación.

Las referencias también pueden estar incompletas, ser incorrectas o reflejar sesgos humanos.

## Preguntas

#flashcards/llms #flashcards/metrics 

**¿Qué es la evaluación por referencia?**
?
![[#Definición]]

**¿Qué subtipos tiene la evaluación por referencia?**
?
![[#Subtipos]]

**¿Cuándo conviene usar evaluación por referencia?**
?
![[#Cuándo usarla]]

**¿Qué limitaciones tiene la evaluación por referencia?**
?
![[#Limitaciones]]
