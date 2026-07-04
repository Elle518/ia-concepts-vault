---
type: concept
tags:
  - dl
  - review
---

## Definición

Una **función de activación** es una transformación aplicada a la salida de una neurona o capa en una [[Red neuronal|red neuronal]].

Su papel principal es introducir no linealidad, permitiendo que la red aprenda relaciones más complejas que una simple transformación lineal.

Sin funciones de activación no lineales, apilar muchas capas lineales seguiría siendo equivalente a una sola capa lineal.

La activación permite que la red combine señales de formas más expresivas.

## Tipos de funciones de activación

Funciones de activación comunes:

- **[[ReLU]]**: devuelve cero para valores negativos y mantiene los positivos.
- **[[Sigmoid]]**: comprime valores entre 0 y 1.
- **[[Tanh]]**: comprime valores entre -1 y 1.
- **[[GELU]]**: habitual en arquitecturas Transformer.
- **[[Softmax]]**: convierte logits en una distribución de probabilidad, normalmente en la salida.

## Preguntas

#flashcards/dl

**¿Qué es una función de activación?**
?
![[#Definición]]

**¿Qué tipos de funciones de activación son comunes?**
?
![[#Tipos de funciones de activación]]
