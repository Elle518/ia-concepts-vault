---
type: concept
tags:
  - ml
  - review
---

## Definición

Un **árbol de decisión** es un modelo que predice dividiendo los datos mediante reglas sucesivas sobre las variables.

Cada nodo interno aplica una condición, cada rama representa una respuesta a esa condición y cada hoja contiene una predicción.

Puede usarse tanto en [[Clasificación|clasificación]] como en [[Regresión|regresión]].

Un árbol de decisión se parece a una serie de preguntas:

- ¿La edad es mayor que cierto valor?
- ¿El usuario ha comprado antes?
- ¿La probabilidad estimada supera un umbral?

Cada respuesta lleva a otra pregunta hasta llegar a una decisión final.

## Funcionamiento

Durante el entrenamiento, el algoritmo busca las divisiones que separen mejor los datos.

En clasificación suelen usarse criterios como [[Entropía|entropía]] o [[Impureza Gini|impureza Gini]]. En regresión se suelen elegir divisiones que reduzcan el error, por ejemplo [[MSE]].

El árbol crece recursivamente hasta cumplir algún criterio de parada, como profundidad máxima, mínimo de muestras por hoja o falta de mejora suficiente.

## Ventajas y limitaciones

Ventajas:

- son fáciles de interpretar
- manejan relaciones no lineales
- requieren poco preprocesamiento
- pueden capturar interacciones entre variables

Limitaciones:

- sobreajustan con facilidad si crecen demasiado
- son sensibles a pequeños cambios en los datos
- suelen generalizar peor que *ensembles* como [[Random forest|random forest]]
- generan fronteras de decisión por cortes rectangulares
- un árbol interpretable no siempre es un buen modelo
- es necesario ajustar bien sus hiperparámetros, como limitar profundidad o tamaño mínimo de hoja, para que no sobreajusten
- las divisiones profundas no tienen necesariamente que ser reglas robustas.

## Preguntas

#flashcards/ml

**¿Qué es un árbol de decisión?**
?
![[#Definición]]

**¿Cómo aprende un árbol de decisión sus splits?**
?
![[#Funcionamiento]]

**¿Qué ventajas y limitaciones tienen los árboles de decisión?**
?
![[#Ventajas y limitaciones]]
