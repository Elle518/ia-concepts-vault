---
type: concept
tags:
  - ml
  - dl
  - review
---

## Definición

Los **hiperparámetros** son configuraciones elegidas antes o durante el entrenamiento que controlan cómo se entrena un modelo o qué arquitectura tiene. Son seleccionados por los usuarios para configurar el modelo y controlar su aprendizaje.

El rendimiento de un modelo depende en gran medida de los valores de sus hiperparámetros.

A diferencia de un [[Parámetro|parámetro]], un hiperparámetro no se aprende directamente mediante *[[Backpropagation|backpropagation]]* a partir de los datos de entrenamiento.

## Ejemplos

Hiperparámetros de entrenamiento:

- learning rate
- batch size
- número de épocas
- tasa de apredizaje
- weight decay
- dropout

Hiperparámetros de arquitectura:

- número de capas
- dimensión oculta
- número de attention heads
- tamaño del vocabulario

En generación con LLMs, también se habla de hiperparámetros de inferencia o *[[Parámetros de decoding|decoding]]*, como [[Temperatura|temperatura]], *[[Top-k sampling|top-k]]* o *[[Top-k sampling|top-p]]*.

## Tuning

Elegir buenos hiperparámetros puede afectar mucho al rendimiento, la estabilidad y el coste.

En modelos pequeños es común probar muchas configuraciones con *[[Grid search|grid search]]*, *[[Random search|random search]]* u [[Optimización bayesiana|optimización bayesiana]], es decir, probar diferentes conjuntos de hiperparámetros y seleccionar el que mejor funcione.

En modelos grandes, entrenar muchas veces puede ser inviable dado que consume muchísimos recursos, así que se usan experimentos de [[Scaling extrapolation|extrapolación a escala]]. Esto significa que, para muchos modelos, es posible que solo haya una oportunidad de conseguir el conjunto de hiperparámetros correcto para el modelo.

## Errores comunes

- Confundir parámetros aprendidos con hiperparámetros configurados.
- Ajustar hiperparámetros mirando el test set.
- Cambiar muchos hiperparámetros a la vez sin poder atribuir el efecto.
- Pensar que una configuración óptima en un dataset se transfiere siempre a otro.

## Preguntas

#flashcards/ml #flashcards/dl

**¿Qué es un hiperparámetro?**
?
![[#Definición]]

**¿Qué ejemplos de hiperparámetros existen?**
?
![[#Ejemplos]]

**¿Qué técnicas de selección de hiperparámetros existen?**
?
![[#Tuning]]

**¿Qué errores comunes aparecen al ajustar hiperparámetros?**
?
![[#Errores comunes]]
