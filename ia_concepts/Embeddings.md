---
type: concept
tags:
  - ml
  - nlp
  - review
---

## Definición

Un ***embedding*** es una representación vectorial densa de un objeto, como una palabra, un documento, una imagen, un usuario o un producto.

La idea es colocar objetos similares cerca entre sí en un espacio vectorial, de forma que la distancia o similitud entre vectores capture relaciones útiles para el modelo.

Un *embedding* convierte datos discretos o complejos en coordenadas numéricas.

Por ejemplo, en NLP, palabras como "perro" y "gato" deberían quedar más cerca entre sí que "perro" y "aeropuerto", porque aparecen en contextos más parecidos.

## Usos

Los embeddings se usan para:

- búsqueda semántica y [[RAG]]
- recomendadores
- [[Clasificación|clasificación]] y [[Clustering|clustering]]
- detección de duplicados
- recuperación de ejemplos similares
- representación de tokens en [[Modelo del lenguaje|modelos de lenguaje]]

En un sistema de *retrieval*, normalmente se calcula un *embedding* de la consulta y se buscan documentos con *embeddings* cercanos usando [[Similitud coseno|similitud coseno]], [[Dot product|dot product]] o [[Distancia euclídea|distancia euclídea]].

## Errores comunes

- Pensar que *embeddings* cercanos siempre implican equivalencia semántica exacta.
- Comparar *embeddings* generados por modelos distintos como si compartieran el mismo espacio.
- Ignorar que la calidad del *embedding* depende del modelo y del dominio.
- Usar *embeddings* sin evaluar si recuperan ejemplos útiles para la tarea final.

## Preguntas

#flashcards/nlp #flashcards/ml

**¿Qué es un *embedding*?**
?
![[#Definición]]

**¿Para qué se usan los *embeddings*?**
?
![[#Usos]]

**¿Qué errores comunes aparecen al trabajar con *embeddings*?**
?
![[#Errores comunes]]
