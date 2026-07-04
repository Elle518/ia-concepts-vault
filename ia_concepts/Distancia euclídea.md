---
type: concept
tags:
  - ml
  - metric
  - review
---

## Definición

La **distancia euclídea** mide la distancia en línea recta entre dos puntos en un espacio vectorial.

Se corresponde con la distancia geométrica habitual y es una métrica básica en *machine learning*.

En dos dimensiones, es la longitud de la línea recta entre dos puntos. En más dimensiones, se generaliza sumando las diferencias al cuadrado por cada coordenada.

## Fórmula

Para dos vectores $a$ y $b$:

$$d(a, b) = \sqrt{\sum_i (a_i - b_i)^2}$$

Cuanto menor es la distancia, más cerca están los puntos según esta métrica.

## Cuándo tener cuidado

La distancia euclídea es sensible a la escala de las características. Si una variable tiene valores mucho mayores que otra, puede dominar la distancia.

Por eso suele ser importante aplicar [[Escalado|escalado]] o [[Normalización|normalización]] antes de usar métodos basados en distancias.

En alta dimensión, las distancias pueden volverse menos informativas porque muchos puntos tienden a estar a distancias parecidas.

## Preguntas

#flashcards/metrics #flashcards/ml

**¿Qué mide la distancia euclídea?**
?
![[#Definición]]

**¿Cómo se calcula la distancia euclídea entre dos vectores?**
?
![[#Fórmula]]

**¿Por qué hay que tener cuidado con la escala al usar distancia euclídea?**
?
![[#Cuándo tener cuidado]]
