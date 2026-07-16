---
type: concept
tags:
  - llms
  - nlp
  - review
---

## Definición

***Chunking*** es el proceso de dividir documentos o textos largos en fragmentos más pequeños llamados *chunks*.

En sistemas de [[RAG]], se usa para indexar, recuperar y pasar al modelo solo las partes relevantes de una fuente.

La intuición es cortar un libro en secciones manejables. Si alguien hace una pregunta, es más fácil recuperar la página o párrafo relevante que enviar el libro entero.

## Tipos de chunking

Los tipos de *chunking* más usados son:

- ***[[Fixed-size chunking]]***: divide el texto en fragmentos de tamaño fijo, normalmente por caracteres o tokens.
- ***[[Sliding window chunking]]***: usa *chunks* solapados para preservar contexto entre cortes.
- ***[[Recursive chunking]]***: intenta cortar primero por separadores grandes, como secciones o párrafos, y baja a separadores más pequeños solo si hace falta.
- ***[[Semantic chunking]]***: agrupa frases o párrafos según cambios de significado usando *embeddings* u otra señal semántica.
- ***[[Structure-based chunking]]***: respeta la estructura del documento, como títulos, secciones, tablas, listas o bloques de código.
- ***[[Hierarchical chunking]]***: indexa chunks pequeños pero mantiene chunks padre más grandes para recuperar contexto ampliado.

En la práctica, muchos sistemas combinan varias estrategias. Por ejemplo, pueden hacer *structure-based chunking* por secciones y después aplicar *recursive chunking* con solapamiento dentro de cada sección.

## Decisiones importantes

Al hacer *chunking* hay que decidir:

- tamaño de *chunk*
- solapamiento entre *chunks*
- unidad de corte: tokens, párrafos, secciones o estructura semántica
- metadatos asociados
- estrategia para tablas, código o listas

*Chunks* demasiado pequeños pierden contexto. *Chunks* demasiado grandes añaden ruido y pueden empeorar el retrieval.

## En RAG

El *chunking* afecta directamente a la calidad del [[Búsqueda semántica|retrieval]].

Si el fragmento recuperado no contiene suficiente contexto, el modelo puede responder mal. Si contiene demasiado, puede saturar la [[Ventana de contexto|ventana de contexto]] o introducir información irrelevante.

## Errores comunes

- Usar un tamaño fijo sin mirar la estructura del documento.
- Ignorar metadatos como título, sección o fuente.
- Cortar tablas o código de forma que pierdan significado.
- Recuperar demasiados chunks y provocar [[Context rot|context rot]].
- Evaluar RAG sin evaluar la estrategia de *chunking*.

## Preguntas

#flashcards/llms #flashcards/nlp 

**¿Qué es *chunking*?**
?
![[#Definición]]

**¿Qué decisiones importan al hacer *chunking*?**
?
![[#Decisiones importantes]]

**¿Qué tipos de *chunking* son habituales en RAG?**
?
![[#Tipos de chunking]]

**¿Cómo afecta el *chunking* a un sistema RAG?**
?
![[#En RAG]]

**¿Qué errores comunes hay al hacer *chunking*?**
?
![[#Errores comunes]]
