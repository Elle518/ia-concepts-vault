---
type: concept
tags:
  - llms
  - metrics
  - review
---

## Definición

La **evaluación pairwise con LLM judge** consiste en pedir a un modelo juez que compare dos respuestas para el mismo input y elija cuál es mejor.

Es un subtipo de [[AI as a judge]] y suele ser más estable que asignar puntuaciones absolutas.

Suele ser más fácil decidir cuál de dos respuestas es mejor que decidir si una respuesta merece un 7 o un 8. Por eso la comparación por pares se usa mucho cuando se quieren ordenar modelos o respuestas.

## Cuándo usarla

Es útil para:

- comparar dos modelos
- elegir entre dos versiones de un *prompt*
- construir rankings de respuestas
- recoger preferencias para [[RLHF]] o evaluación de producto

## Limitaciones

Puede ser sensible al orden de presentación de las respuestas.

No produce directamente una puntuación absoluta, sino una preferencia relativa.

Si hay muchos modelos o respuestas, el número de comparaciones puede crecer mucho.

## Preguntas

#flashcards/llms #flashcards/metrics

**¿Qué es la evaluación *pairwise* con LLM judge?**
?
![[#Definición]]

**¿Cuándo conviene usar evaluación *pairwise*?**
?
![[#Cuándo usarla]]

**¿Qué limitaciones tiene la evaluación *pairwise*?**
?
![[#Limitaciones]]
