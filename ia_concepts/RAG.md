---
type: concept
tags:
  - llms
  - nlp
  - review
---

## Definición

**RAG** o **recuperación aumentada por generación** (*retrieval-augmented generation*) es una arquitectura que combina recuperación de información con generación de texto. Antes de responder, el sistema busca información relevante en una fuente externa y la usa como contexto para el modelo.

La idea es reducir dependencia exclusiva de la memoria paramétrica del modelo y anclar la respuesta en datos recuperados.

Es como dejar que el modelo consulte apuntes antes de contestar. En lugar de confiar solo en lo que “se sabe de memoria”, primero mira la documentación relevante y luego redacta la respuesta.

## Componentes de un RAG

Un flujo RAG típico incluye:

- segmentación o [[Chunking|chunking]]
- generación de [[Embeddings|embeddings]]
- búsqueda en un [[Índice|índice]] o *[[Vector store|vector store]]*
- selección de contexto relevante
- generación condicionada por ese contexto

## Utilidad

RAG es útil cuando el conocimiento cambia, cuando queremos reducir alucinaciones o cuando necesitamos citar una base documental concreta. Su calidad depende tanto del modelo generador como del sistema de recuperación.

## Errores comunes

- Pensar que RAG arregla automáticamente malas fuentes o mala recuperación.
- Recuperar demasiados fragmentos y saturar el contexto.
- No evaluar por separado retrieval y generación.
- Confundir RAG con *fine-tuning*.

## Preguntas

#flashcards/llms #flashcards/nlp

**¿Qué es RAG?**
?
![[#Definición]]

**¿Qué componentes suele tener un sistema RAG?**
?
![[#Componentes de un RAG]]

**¿Cuándo es útil implementar un sistema RAG?**
?
![[#Utilidad]]

**¿Qué errores se suelen cometer en RAG?**
?
![[#Errores comunes]]

