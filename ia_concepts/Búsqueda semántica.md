---
type: concept
tags:
  - nlp
  - llms
  - review
---

## Definición

La **búsqueda semántica** (*semantic search*) es una técnica de recuperación que busca resultados por significado, no solo por coincidencia exacta de palabras.

Suele representar consultas y documentos como *[[Embeddings|embeddings]]* y recuperar los vectores más cercanos.

La intuición es que una búsqueda por “coche barato” pueda encontrar “vehículo económico”, aunque no comparta las mismas palabras.

## Funcionamiento

Un flujo típico es:

1. convertir documentos en *embeddings*
2. guardarlos en un índice o *[[Vector store|vector store]]*
3. convertir la consulta en *embedding*
4. buscar documentos cercanos con una [[Métricas de similitud|métrica de similitud]]
5. devolver o reordenar los resultados

Las métricas comunes incluyen [[Similitud coseno|similitud coseno]], [[Dot product|dot product]] y [[Distancia euclídea|distancia euclídea]].

## Uso en RAG

En [[RAG]], la búsqueda semántica se usa para recuperar fragmentos relevantes antes de generar una respuesta.

Su calidad depende del modelo de *embeddings*, del *[[Chunking|chunking]]*, del dominio, del índice y de cómo se evalúa la relevancia.

## Errores comunes

- Pensar que búsqueda semántica siempre supera [[Búsqueda por palabras clave|búsqueda por palabras clave]].
- No evaluar retrieval por separado de generación.
- Usar *embeddings* de un dominio distinto sin validación.
- Recuperar resultados parecidos semánticamente pero irrelevantes para la intención.
- No combinar con filtros, metadatos o búsqueda léxica cuando hacen falta.

## Preguntas

#flashcards/nlp #flashcards/llms 

**¿Qué es la búsqueda semántica?**
?
![[#Definición]]

**¿Cómo funciona una búsqueda semántica típica?**
?
![[#Funcionamiento]]

**¿Cómo se usa la búsqueda semántica en RAG?**
?
![[#Uso en RAG]]

**¿Qué errores comunes hay al usar búsqueda semántica?**
?
![[#Errores comunes]]
