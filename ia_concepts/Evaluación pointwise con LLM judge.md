---
type: concept
tags:
  - llms
  - metrics
  - review
---

## Definición

La **evaluación *pointwise* con LLM judge** consiste en pedir a un modelo juez que evalúe una única respuesta de forma aislada.

El juez suele devolver una puntuación, una etiqueta o una explicación según los criterios dados.

Es un subtipo de [[AI as a judge]].

Es como pedir a un corrector que puntúe una respuesta sin compararla con otras. Por ejemplo, el juez puede puntuar de 1 a 5 la utilidad, factualidad o claridad de una respuesta.

## Cuándo usarla

Es útil cuando:

- solo hay una respuesta candidata por entrada
- se quieren métricas independientes por criterio
- se necesita una puntuación absoluta
- se quiere monitorizar calidad a lo largo del tiempo

## Limitaciones

Las puntuaciones absolutas suelen ser inestables.

Dos jueces pueden usar la escala de forma distinta, y el mismo juez puede cambiar su criterio si el *prompt* no es preciso.

Por eso conviene usar rúbricas claras, ejemplos calibrados y, si es posible, varias evaluaciones por muestra.

## Preguntas

#flashcards/llms #flashcards/metrics

**¿Qué es la evaluación *pointwise* con LLM judge?**
?
![[#Definición]]

**¿Cuándo conviene usar evaluación *pointwise*?**
?
![[#Cuándo usarla]]

**¿Qué limitaciones tiene la evaluación *pointwise*?**
?
![[#Limitaciones]]
