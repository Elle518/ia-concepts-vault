---
type: concept
tags:
  - llms
  - nlp
  - review
---

## Definición

***Sliding window chunking*** divide un texto en chunks de tamaño fijo con solapamiento entre *chunks* consecutivos.

Es una variante de *[[Fixed-size chunking|fixed-size chunking]]* pensada para reducir la pérdida de contexto en los límites de cada fragmento.

La intuición es mover una ventana por el documento: cada *chunk* comparte una parte con el anterior y con el siguiente.

Es útil cuando las respuestas pueden depender de información situada justo antes o después del corte.

También ayuda en documentos narrativos, documentación técnica y textos donde las ideas se extienden durante varios párrafos.

## Funcionamiento

Se definen dos parámetros:

- ***window size***: tamaño de cada *chunk*
- ***stride***: cuánto avanza la ventana entre *chunks*

Si el *chunk* tiene 500 tokens y el *stride* es 400, cada *chunk* comparte 100 tokens con el anterior.

## Trade-offs

El solapamiento mejora continuidad, pero aumenta:

- número de *chunks*
- coste de *embeddings*
- tamaño del índice
- redundancia en resultados recuperados

Demasiado solapamiento puede hacer que el retriever devuelva *chunks* casi idénticos y desperdicie espacio de la [[Ventana de contexto|ventana de contexto]].

Si usamos un solapamiento alto hay que medir la redundancia y, seguramente, deduplicar resultados muy parecidos.

No debería aplicarse a tablas o código sin respetar bloques lógicos.

## Preguntas

#flashcards/llms #flashcards/nlp

**¿Qué es *sliding window chunking*?**
?
![[#Definición]]

**¿Qué parámetros controla el *sliding window chunking*?**
?
![[#Funcionamiento]]

**¿Qué trade-offs introduce el solapamiento entre chunks?**
?
![[#Trade-offs]]
