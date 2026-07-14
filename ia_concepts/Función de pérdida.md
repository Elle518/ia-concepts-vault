---
type: concept
tags:
  - ml
  - dl
  - review
---

## Definición

Una **función de pérdida** (*loss function*) mide cuánto se equivoca un modelo en sus predicciones.

Durante el entrenamiento, el objetivo suele ser ajustar los [[Parámetro|parámetros]] del modelo para minimizar esa pérdida.

La función de pérdida convierte el error del modelo en un número. Si el número es alto, la predicción es mala según el criterio elegido. Si es bajo, la predicción se acerca más al objetivo.

## Ejemplos

La pérdida depende del tipo de problema:

- En [[Regresión|regresión]], son comunes [[MSE]] y [[MAE]].
- En [[Clasificación|clasificación]], es común [[Cross-entropy loss|cross-entropy loss]].
- En modelos de lenguaje, se suele entrenar prediciendo el siguiente token con [[Cross-entropy loss|cross-entropy loss]].

La elección de la función de pérdida define qué significa “mejorar” para el modelo.

## Errores comunes

- Confundir la pérdida de entrenamiento con la métrica final de negocio.
- Optimizar una pérdida que no refleja bien el coste real de los errores.
- Comparar valores de pérdida entre problemas distintos sin contexto.
- Olvidar que una pérdida baja en entrenamiento puede coexistir con [[Sobreajuste|sobreajuste]].

## Preguntas

#flashcards/ml #flashcards/dl

**¿Qué es una función de pérdida?**
?
![[#Definición]]

**¿Qué ejemplos de funciones de pérdida son comunes?**
?
![[#Ejemplos]]

**¿Qué errores comunes aparecen al elegir o interpretar una función de pérdida?**
?
![[#Errores comunes]]
