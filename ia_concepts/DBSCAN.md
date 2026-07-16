---
type: concept
tags:
  - ml
  - review
---

## Definición

**DBSCAN** (*Density-Based Spatial Clustering of Applications with Noise*) es un algoritmo de *[[Clustering|clustering]]* basado en densidad.

Agrupa puntos que están en regiones densas y marca como ruido los puntos aislados.

A diferencia de [[k-Means|k-Means]], no requiere fijar el número de *clusters* de antemano.

DBSCAN busca zonas donde hay muchos puntos cerca unos de otros.

Si un punto tiene suficientes vecinos dentro de un radio, se considera parte de una región densa. Los *clusters* se forman conectando regiones densas cercanas.

Los puntos que no pertenecen a ninguna región densa se tratan como *outliers* o ruido.

## Parámetros principales

DBSCAN depende sobre todo de:

- `eps`: radio máximo para considerar que dos puntos son vecinos.
- `min_samples`: número mínimo de puntos necesarios para formar una región densa.

Un ***core point*** tiene al menos `min_samples` vecinos dentro de `eps`.

Un ***border point*** está cerca de un *core point*, pero no tiene suficientes vecinos propios.

Un ***noise point*** no pertenece a ningún *cluster*. No todos los puntos de ruido son errores de datos.

## Trade-offs

Ventajas:

- detecta *clusters* con formas no esféricas
- identifica *outliers*
- no necesita elegir $k$

Limitaciones:

- es sensible a la escala de las variables
- cuesta elegir `eps`
- funciona peor cuando los *clusters* tienen densidades muy diferentes
- puede degradarse en alta dimensionalidad

## Preguntas

#flashcards/ml

**¿Qué es DBSCAN?**
?
![[#Definición]]

**¿Qué significan `eps` y `min_samples` en DBSCAN?**
?
![[#Parámetros principales]]

**¿Qué ventajas y limitaciones tiene DBSCAN?**
?
![[#Trade-offs]]
