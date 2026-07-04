---
type: concept
tags:
  - ml
  - dl
  - llms
  - review
---

## Definición

***Cross-entropy loss*** es una [[Función de pérdida|función de pérdida]] usada para comparar una distribución de probabilidad predicha con una distribución objetivo.

Es especialmente común en [[Clasificación|clasificación]] y en entrenamiento de [[Modelo del lenguaje|modelos de lenguaje]].

*Cross-entropy* penaliza mucho al modelo cuando asigna baja probabilidad a la respuesta correcta.

Si la clase correcta es "gato" y el modelo le da probabilidad 0.95, la pérdida será baja. Si le da probabilidad 0.01, la pérdida será alta.

## Fórmula

Para una distribución objetivo $y$ y una predicción $\hat{y}$:

$$H(y, \hat{y}) = - \sum_i y_i \log(\hat{y}_i)$$

Cuando la etiqueta es *[[One-hot encoding|one-hot]]*, la pérdida se reduce a:

$$-\log(p_{\text{clase correcta}})$$

Por eso, el modelo no solo debe acertar la clase, sino asignarle alta probabilidad.

## En modelos de lenguaje

En un modelo autorregresivo, *cross-entropy* se usa para entrenar al modelo a predecir el siguiente [[Tokenización|token]].

En cada posición, el modelo produce una distribución sobre el vocabulario. La pérdida penaliza que el token real tenga baja probabilidad.

La [[Perplexity|perplexity]] está directamente relacionada con la *cross-entropy*, ya que una menor *cross-entropy* implica menor perplexity.

## Preguntas

#flashcards/ml #flashcards/llms

**¿Qué es *cross-entropy loss*?**
?
![[#Definición]]

**¿Cómo se calcula *cross-entropy loss*?**
?
![[#Fórmula]]

**¿Para qué se usa cross-entropy en modelos de lenguaje?**
?
![[#En modelos de lenguaje]]
