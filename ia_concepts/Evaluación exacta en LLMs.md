---
type: concept
tags:
  - llms
  - metrics
  - review
---

## Definición

La **evaluación exacta en LLMs** mide respuestas mediante reglas automáticas que producen un resultado determinado y reproducible.

Una respuesta puede ser correcta o incorrecta, pasar o fallar un test, coincidir con una referencia o alcanzar una puntuación calculada de forma exacta.

Es especialmente útil cuando la tarea tiene un objetivo verificable.

## Subtipos

Los subtipos principales son:

- *[[Functional correctness]]*
- [[Evaluación por referencia]]. Y dentro de esta:
  - *[[Exact match]]*
  - [[Similitud léxica]]
  - [[Similitud semántica]]

Aunque la [[Similitud semántica|similitud semántica]] depende del modelo de *[[Embeddings|embeddings]]* usado, una vez fijados los *embeddings* y la métrica, el cálculo es exacto.

## Ventajas y limitaciones

La principal ventaja es la reproducibilidad, ya que dos ejecuciones con el mismo protocolo deberían dar el mismo resultado.

La limitación es que muchas tareas de LLMs son abiertas. Una respuesta puede ser válida aunque no coincida con una referencia, o puede parecer similar a la referencia sin ser realmente correcta.

## Preguntas

#flashcards/llms #flashcards/metrics

**¿Qué es la evaluación exacta en LLMs?**
?
![[#Definición]]

**¿Qué subtipos incluye la evaluación exacta?**
?
![[#Subtipos]]

**¿Qué ventaja y qué limitación tiene la evaluación exacta?**
?
![[#Ventajas y limitaciones]]
