---
type: concept
tags:
  - ml
  - review
---

## Definición

La **entropía** mide la incertidumbre de una distribución de probabilidad.

En *machine learning* aparece en clasificación, árboles de decisión, funciones de pérdida, [[Active learning|active learning]] y modelos probabilísticos.

Si una distribución está muy concentrada en una opción, hay poca incertidumbre y la entropía es baja.

Si la probabilidad está repartida entre muchas opciones parecidas, hay más incertidumbre y la entropía es alta.

## Fórmula

Para una distribución discreta $p$, la entropía se define como:

$$H(p) = - \sum_i p_i \log p_i$$

En clasificación, una predicción $[0.99, 0.01]$ tiene baja entropía. Una predicción $[0.5, 0.5]$ tiene mayor entropía porque el modelo está menos seguro.

## Usos en ML

- En [[Árbol de decisión|árboles de decisión]], puede usarse para medir impureza y elegir divisiones.
- En [[Active learning|active learning]], **entropy sampling** selecciona ejemplos con alta incertidumbre.
- En [[Modelo del lenguaje|modelos de lenguaje]], la entropía de la distribución sobre tokens indica qué tan concentrada o abierta está la predicción.
- En [[Cross-entropy loss|cross-entropy loss]], se compara la distribución predicha con la distribución objetivo.

## Preguntas

#flashcards/ml

**¿Qué mide la entropía?**
?
![[#Definición]]

**¿Cómo se calcula la entropía de una distribución discreta?**
?
![[#Fórmula]]

**¿Dónde aparece la entropía en *machine learning*?**
?
![[#Usos en ML]]
