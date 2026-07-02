---
type: concept
tags:
  - ml
  - review
---

## Definición

El **aprendizaje supervisado** es un tipo de [[Aprendizaje automático|machine learning]] en el que el modelo aprende a partir de ejemplos etiquetados.

Cada ejemplo de entrenamiento contiene una entrada y una respuesta esperada. El objetivo es aprender una función que pueda predecir la salida correcta para datos nuevos.

Es como estudiar con ejercicios resueltos. El modelo ve el enunciado y también la respuesta correcta.

Si entrenamos con fotos etiquetadas como "perro" o "gato", el modelo puede aprender a clasificar nuevas fotos. Si entrenamos con historiales de compra y gasto real, puede aprender a predecir gasto futuro.

## Tipos de aprendizaje supervisado

Las dos tareas principales son:

- [[Clasificación]]: predice una categoría discreta, como spam/no spam.
- [[Regresión]]: predice un valor numérico continuo, como precio, demanda o gasto.

## Funcionamiento

En aprendizaje supervisado tenemos pares $(x, y)$, donde $x$ representa las features de entrada e $y$ la etiqueta o valor objetivo.

El entrenamiento ajusta los parámetros del modelo para minimizar una función de pérdida entre las predicciones y las etiquetas reales. Después se evalúa en datos no vistos para medir generalización.

## Preguntas

#flashcards/ml

**¿Qué es el aprendizaje supervisado?**
?
![[#Definición]]

**¿Cómo funciona el aprendizaje supervisado?**
?
![[#Funcionamiento]]

**¿Cuáles son las dos tareas principales del aprendizaje supervisado?**
?
![[#Tipos de aprendizaje supervisado]]
