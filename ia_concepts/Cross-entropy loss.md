---
type: concept
tags:
  - dl
  - llms
  - ml
  - review
---

## Definición

***Cross-entropy loss*** es una [[Función de pérdida|función de pérdida]] usada para entrenar modelos que predicen distribuciones de probabilidad.

Es especialmente común en [[Clasificación|clasificación]] y en entrenamiento de [[Modelo del lenguaje|modelos de lenguaje]].

Penaliza mucho al modelo cuando asigna baja probabilidad a la respuesta correcta. Si la clase correcta es "gato" y el modelo le da probabilidad 0.95, la pérdida será baja. Si le da probabilidad 0.01, la pérdida será alta.

La pérdida (*loss*) es la versión operativa, calculada sobre muestras o batches de muestras, de la métrica *[[Cross-entropy|cross-entropy]]*.

## Fórmula

Para una distribución objetivo $y$ y una predicción $\hat{y}$:

$$H(y, \hat{y}) = - \sum_i y_i \log(\hat{y}_i)$$

Cuando la etiqueta es *[[One-hot encoding|one-hot]]*, la pérdida se reduce a:

$$-\log(p_{\text{clase correcta}})$$

Por eso, el modelo no solo debe acertar la clase, sino asignarle alta probabilidad.

## En modelos de lenguaje

En un modelo autorregresivo, *cross-entropy loss* se usa para entrenar al modelo a predecir el siguiente [[Tokenización|token]].

En cada posición, el modelo produce una distribución sobre el vocabulario. La pérdida penaliza que el token real tenga baja probabilidad.

Durante el entrenamiento, se calcula la pérdida token a token y después se promedia sobre la secuencia o el batch.

Minimizar esta pérdida empuja al modelo a asignar más probabilidad a los tokens observados en los datos.

## Diferencia con cross-entropy

La *[[Cross-entropy|cross-entropy]]* es una métrica o cantidad teórica entre distribuciones.

La *cross-entropy loss* es la función que se implementa y minimiza durante el entrenamiento.

En muchos contextos se usa *”cross-entropy”* como abreviatura de *“cross-entropy loss”*, pero conviene distinguirlas cuando se habla de evaluación frente a optimización.

## Errores comunes

- Confundir la pérdida de entrenamiento con la métrica agregada sobre un conjunto de datos.
- Pensar que una pérdida baja en entrenamiento garantiza buena generalización.
- Aplicar *[[Softmax|softmax]]* manualmente antes de una implementación que ya espera *[[Logit|logits]]*.
- Comparar pérdidas entre problemas con vocabularios, tokenizadores o escalas distintas sin contexto.

## Preguntas

#flashcards/dl  #flashcards/llms #flashcards/ml 

**¿Qué es *cross-entropy loss*?**
?
![[#Definición]]

**¿Cómo se calcula *cross-entropy loss*?**
?
![[#Fórmula]]

**¿Para qué se usa *cross-entropy loss* en modelos de lenguaje?**
?
![[#En modelos de lenguaje]]

**¿En qué se diferencia *cross-entropy loss* de *cross-entropy*?**
?
![[#Diferencia con cross-entropy]]

**¿Qué errores comunes aparecen al usar *cross-entropy loss*?**
?
![[#Errores comunes]]
