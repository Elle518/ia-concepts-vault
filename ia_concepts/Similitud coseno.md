---
type: concept
tags:
  - ml
  - nlp
  - review
---

## Definición

La **similitud coseno** mide el parecido entre dos vectores usando el coseno del ángulo entre ellos.

Es muy común para comparar [[Embeddings|embeddings]], especialmente en [[Búsqueda semántica|búsqueda semántica]], [[Sistemas de recomendación|recomendadores]] y sistemas de [[RAG]].

La similitud coseno se fija en la dirección de los vectores más que en su longitud. Si dos *embeddings* apuntan en una dirección parecida, se consideran similares aunque uno tenga una magnitud mayor que el otro.

## Fórmula

Para dos vectores $a$ y $b$:

$$\cos(a, b) = \frac{a \cdot b}{\|a\| \|b\|}$$

El resultado suele estar entre -1 y 1:

- 1 indica misma dirección
- 0 indica direcciones ortogonales
- -1 indica direcciones opuestas

En muchos modelos de *embeddings*, valores más altos indican mayor [[Similitud semántica|similitud semántica]].

## Errores comunes

- Interpretar similitud alta como equivalencia exacta.
- Comparar *embeddings* de modelos distintos sin comprobar compatibilidad.
- Olvidar normalizar vectores cuando se quiere que [[Dot product|dot product]] sea equivalente a similitud coseno.
- Evaluar retrieval solo mirando similitud, sin medir calidad de resultados.

## Preguntas

#flashcards/ml #flashcards/nlp

**¿Qué mide la similitud coseno?**
?
![[#Definición]]

**¿Cómo se calcula la similitud coseno?**
?
![[#Fórmula]]

**¿Qué errores comunes aparecen al usar similitud coseno?**
?
![[#Errores comunes]]
