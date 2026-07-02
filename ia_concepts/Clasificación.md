---
type: concept
tags:
  - ml
  - review
---

## Definición

La **clasificación** es una tarea de [[Aprendizaje supervisado|aprendizaje supervisado]] en la que el modelo predice una categoría discreta.

Ejemplos típicos son detectar si un email es spam, decidir si una imagen contiene un gato o un perro, o clasificar una reseña como positiva, negativa o neutral.

Clasificar significa elegir una etiqueta entre varias opciones posibles. La pregunta no es "cuánto vale", sino "a qué clase pertenece".

## Tipos de clasificación

En clasificación, la variable objetivo es categórica. Puede ser:

- **Binaria**: dos clases, como fraude/no fraude.
- **Multiclase**: más de dos clases excluyentes, como idioma del texto.
- **Multietiqueta**: varias clases pueden ser verdaderas a la vez, como tags de un documento.

## Modelos de clasificación

Modelos comunes para clasificación incluyen regresión logística, árboles de decisión, random forests, gradient boosting, SVMs y [[Red neuronal|redes neuronales]].

## Métricas de clasificación

La evaluación suele usar métricas como *accuracy*, precision, *recall*, F1, ROC-AUC o matriz de confusión, según el coste de falsos positivos y falsos negativos.

## Preguntas

#flashcards/ml

**¿Qué es una tarea de clasificación?**
?
![[#Definición]]

**¿Qué tipos de clasificación existen?**
?
![[#Tipos de clasificación]]

**¿Qué métricas se suelen usar en tareas de clasificación?**
?
![[#Métricas de clasificación]]

**¿Qué modelos se suelen usar en tareas de clasificación?**
?
![[#Modelos de clasificación]]
