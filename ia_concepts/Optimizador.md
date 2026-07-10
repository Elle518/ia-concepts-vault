---
type: concept
tags:
  - ml
  - dl
  - review
---

## Definición

Un **optimizador** es el algoritmo que actualiza los [[Parámetro|parámetros]] de un modelo para reducir una [[Función de pérdida|función de pérdida]].

En redes neuronales, usa los gradientes calculados por [[Backpropagation|backpropagation]] para decidir cómo mover los pesos.

Si la función de pérdida indica cuánto se equivoca el modelo, el optimizador decide cómo corregirlo. Es como bajar por una superficie buscando un valle: los gradientes indican la pendiente y el optimizador decide el tamaño y la dirección de cada paso.

## Ejemplos

Optimizadores comunes:

- **[[SGD]]**: actualiza pesos siguiendo el gradiente estimado en batches.
- **[[SGD con momentum]]**: suaviza actualizaciones acumulando dirección.
- **[[Adam]]**: adapta el tamaño de actualización por parámetro usando momentos del gradiente.
- **[[AdamW]]**: variante de Adam con [[Weight decay|weight decay]] desacoplado, muy usada en *deep learning* moderno.

El *[[Tasa de aprendizaje|learning rate]]* suele ser el [[Hiperparámetros|hiperparámetro]] más importante del optimizador.

## Errores comunes

- Confundir optimizador con *backpropagation*.
- Usar un *learning rate* demasiado alto y hacer inestable el entrenamiento.
- Usar un *learning rate* demasiado bajo y entrenar demasiado lento.
- Cambiar de optimizador sin revisar [[Regularización|regularización]], *[[Batch size|batch size]]* y *[[Scheduler|scheduler]]*.

## Preguntas

#flashcards/ml #flashcards/dl

**¿Qué es un optimizador?**
?
![[#Definición]]

**¿Qué optimizadores son comunes en deep learning?**
?
![[#Ejemplos]]

**¿Qué errores comunes aparecen al configurar un optimizador?**
?
![[#Errores comunes]]
