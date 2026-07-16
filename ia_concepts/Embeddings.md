---
type: concept
tags:
  - ml
  - nlp
  - review
---

## Definición

Un ***embedding*** es una representación vectorial densa de un objeto, como una palabra, un documento o una imagen, cualquier dato puede tener su correspondiente *embedding*. Un *embedding* es una representación numérica que busca capturar el significado de los datos originales.

La idea es colocar objetos similares cerca entre sí en un espacio vectorial, de forma que la distancia o similitud entre vectores capture relaciones útiles para el modelo.

Un *embedding* convierte datos discretos o complejos en coordenadas numéricas. Una*embedding* se considera una representación de datos complejos en un espacio de menor dimensión.

El objetivo del algoritmo de *embeddings* es producir *embeddings* que capturen la esencia de los datos originales.

En términos generales, un algoritmo de *embeddings* se considera bueno si los textos más similares tienen *embeddings* más cercanas, medidas mediante la similitud del coseno u otras métricas relacionadas.

También puede evaluar la calidad de los *embeddings* en función de su utilidad para la tarea en cuestión. Un ejemplo de conjunto de pruebas que mide la calidad de los *embeddings* en múltiples tareas es [MTEB](https://huggingface.co/spaces/mteb/leaderboard) (*Massive Text Embedding Benchmark*).

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

Dado que los modelos suelen requerir que sus entradas se transformen primero en representaciones vectoriales, muchos modelos también incluyen un paso para generar *embeddings*.

Si tenemos acceso a las capas intermedias de estos modelos, podemos utilizarlas para extraer *embeddings*. Sin embargo, la calidad de estos *embeddings* podría no ser tan buena como la de las generadas por modelos de *embeddings* especializados.

## Joint embeddings

Una nueva frontera consiste en crear ***joint embeddings*** para datos de diferentes modalidades (como texto, imágenes, audio, etc.).

Un espacio de *joint embeddings* que puede representar datos de diferentes modalidades se denomina **espacio de *embeddings* multimodal** (*multimodal embedding space*).

En un espacio de *joint embeddings* de texto e imagen, el *embedding* de la imagen de un hombre pescando debería estar más cerca del *embedding* del texto “pescador” que del *embedding* del texto “desfile de moda”.

Este espacio de *joint embeddings* permite comparar y combinar incrustaciones de diferentes modalidades. Por ejemplo, esto posibilita la búsqueda de imágenes basada en texto. Dado un texto, ayuda a encontrar las imágenes más cercanas a dicho texto.

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
