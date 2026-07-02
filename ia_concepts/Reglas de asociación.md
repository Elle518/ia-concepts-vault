---
type: concept
tags:
  - ml
  - review
---

## Definición

Las **reglas de asociación** son técnicas de [[Aprendizaje no supervisado|aprendizaje no supervisado]] que buscan relaciones frecuentes entre elementos o eventos.

Se usan para descubrir patrones del tipo "si ocurre A, suele ocurrir B", como productos que se compran juntos.

La idea clásica es el análisis de cesta de la compra. Si muchos clientes que compran pasta también compran salsa, el sistema puede detectar esa relación y usarla para recomendaciones, promociones o colocación de productos.

Una regla de asociación suele expresarse como:

$$A \Rightarrow B$$

donde $A$ es el antecedente y $B$ el consecuente.

## Métricas de reglas de asociación

Las métricas más habituales son:

- **[[Support]]**: frecuencia con la que aparece la combinación en el dataset.
- **[[Confidence]]**: probabilidad de ver $B$ cuando aparece $A$.
- **[[Lift]]**: cuánto más probable es ver $B$ con $A$ frente a verlo por azar.

## Algoritmos de asociación

Un algoritmo clásico para extraer reglas de asociación es **[[Apriori]]**, que genera conjuntos frecuentes y deriva reglas a partir de ellos.

## Preguntas

#flashcards/ml

**¿Qué son las reglas de asociación?**
?
![[#Definición]]

**¿Cuál es algoritmos suelen usarse para reglas de asociación?**
?
![[#Algoritmos de asociación]]

**¿Qué métricas se usan en las reglas de asociación?**
?
![[#Métricas de reglas de asociación]]
