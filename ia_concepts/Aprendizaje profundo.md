---
type: concept
tags:
  - dl
  - review
---

## Definición

El **aprendizaje profundo** o *deep learning* (DL) es una subcategoría del **[[Aprendizaje automático|aprendizaje automático]]** o *machine learning* (ML) que utiliza **[[Red neuronal|redes neuronales]]** con múltiples capas para modelar patrones complejos en los datos.

Es particularmente efectivo para manejar grandes cantidades de datos. tanto estructurados como no estructurados (como imágenes, texto o audio).

## DL vs ML tradicional

La principal diferencia entre DL y el ML tradicional radica en su capacidad para la **extracción de características**. Los modelos de DL aprenden automáticamente características a partir de datos sin procesar, mientras que el ML tradicional a menudo requiere ingeniería manual de características.

Por ejemplo, para una tarea de clasificación de imágenes, un enfoque de ML tradicional podría implicar la extracción manual de características (como bordes o texturas) y luego usar un clasificador como SVM.

Por su parte, un enfoque de DL (utilizando una CNN) tomaría como entrada imágenes sin procesar y aprendería automáticamente a extraer estas características a través de las capas convolucionales, reduciendo significativamente la necesidad de extracción manual de características.

El DL destaca al trabajar con grandes conjuntos de datos y problemas complejos (**escalabilidad**), como el reconocimiento de imágenes o el procesamiento del lenguaje natural. Los algoritmos de ML tradicionales pueden tener dificultades con la misma complejidad y escala de datos.

En cuanto a la **interpretabilidad del modelo**, los modelos tradicionales de ML suelen ser más interpretables que los modelos de DL, que se consideran más como "cajas negras" debido a su complejidad y la dificultad para entender cómo toman decisiones.

Por último, los modelos de DL generalmente requieren **más tiempo y recursos computacionales** para entrenarse que los modelos tradicionales de ML. Esto normalmente se maneja con *hardware* especializado como las GPU.

## Preguntas

#flashcards/dl 

¿Qué es el aprendizaje profundo?
?
[[Aprendizaje profundo#Definición]]

¿Cómo difiere el aprendizaje profundo del aprendizaje automático tradicional?
?
[[Aprendizaje profundo#DL vs ML tradicional]]
