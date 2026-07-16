---
type: concept
tags:
  - llms
  - nlp
  - review
---

## Definición

***Fixed-size chunking*** consiste en dividir un texto en fragmentos de tamaño fijo, normalmente medido en caracteres, palabras o tokens.

Es una estrategia simple de *[[Chunking|chunking]]* usada en sistemas de [[RAG]] cuando se quiere una segmentación rápida y fácil de controlar.

La intuición es cortar el documento cada cierto número de tokens sin intentar entender demasiado su estructura.

## Funcionamiento

Se define un tamaño máximo, por ejemplo 500 tokens, y se divide el documento en bloques de ese tamaño.

A veces se añade solapamiento entre *chunks* para no perder contexto en los bordes. Si el solapamiento es importante para la estrategia, se habla de [[Sliding window chunking|sliding window chunking]].

## Cuándo usarlo

Tiene sentido como *baseline* porque:

- es fácil de implementar
- produce *chunks* de tamaño predecible
- controla bien el coste de *embeddings* y contexto
- funciona razonablemente en documentos homogéneos

Es útil para una primera versión de un pipeline RAG antes de invertir en estrategias más complejas.

## Limitaciones

El problema principal es que puede cortar ideas, tablas, listas o código por la mitad.

También ignora títulos, secciones y cambios semánticos. Un *chunk* puede quedarse sin el contexto necesario para entenderse, o mezclar partes no relacionadas.

A la hora de elegir el tamaño de *chunk*, ya que un tamaño fijo óptimo no sirve para todos los dominios, es necesario evaluar el retrieval para evaluar si los chunks son interpretables.

No conviene usarlo en documentos muy estructurados ya que no respetará las secciones.

## Preguntas

#flashcards/llms #flashcards/nlp

**¿Qué es *fixed-size chunking*?**
?
![[#Definición]]

**¿Cómo funciona el *fixed-size chunking*?**
?
![[#Funcionamiento]]

**¿Cuándo tiene sentido usar *fixed-size chunking*?**
?
![[#Cuándo usarlo]]

**¿Qué limitaciones tiene *fixed-size chunking*?**
?
![[#Limitaciones]]
