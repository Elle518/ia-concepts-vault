---
type: concept
tags:
  - dl
  - review
---

## Definición

Una **red neuronal** es un modelo de [[Aprendizaje automático|machine learning]] formado por capas de unidades o neuronas artificiales que transforman una entrada en una salida.

Cada conexión tiene [[Parámetro|parámetros]] aprendibles, normalmente pesos y sesgos, que se ajustan durante el entrenamiento para minimizar una función de pérdida.

Una red neuronal aprende una cadena de transformaciones.

Las primeras capas pueden detectar patrones simples y las capas posteriores combinan esos patrones para resolver una tarea más compleja, como clasificar una imagen, predecir una serie temporal o generar texto.

## Componentes básicos

- **Capa de entrada**: recibe las características, tokens, píxeles o señales originales.
- **Capas ocultas**: aplican transformaciones aprendidas.
- **[[Función de activación]]**: introduce no linealidad para que la red pueda representar relaciones complejas.
- **Capa de salida**: produce logits, probabilidades, *embeddings* o valores numéricos según la tarea.
- **[[Función de pérdida]]**: mide el error entre la predicción y el objetivo.

El entrenamiento suele usar *[[Backpropagation|backpropagation]]* para calcular gradientes y un [[Optimizador|optimizador]] para actualizar los pesos.

## Preguntas

#flashcards/dl #flashcards/ml

**¿Qué es una red neuronal?**
?
![[#Definición]]

**¿Qué componentes básicos tiene una red neuronal?**
?
![[#Componentes básicos]]
