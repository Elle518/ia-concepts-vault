---
type: concept
tags:
  - ml
  - review
---

## Definición

***Grid search*** es una técnica de búsqueda de [[Hiperparámetros|hiperparámetros]] que prueba todas las combinaciones de valores definidos en una cuadrícula.

Después se selecciona la configuración con mejor rendimiento en validación.

*Grid search* consiste en probar sistemáticamente todas las opciones que hemos escrito.

Si queremos probar tres valores de *learning rate* y cuatro valores de *batch size*, entrenaremos 12 configuraciones.

## Cuándo usarlo

Puede ser útil cuando:

- hay pocos hiperparámetros
- cada entrenamiento es barato
- se quiere una búsqueda fácil de reproducir
- tenemos una idea razonable de rangos concretos

No escala bien cuando hay muchos hiperparámetros o valores posibles, porque el número de combinaciones crece muy rápido.

## Comparación

Frente a *[[Random search|random search]]*, *grid search* es más exhaustivo dentro de la cuadrícula definida, pero puede desperdiciar muchas pruebas en hiperparámetros poco importantes.

Frente a [[Optimización bayesiana|optimización bayesiana]], es más simple, pero menos eficiente cuando cada entrenamiento es caro.

## Preguntas

#flashcards/ml

**¿Qué es *grid search*?**
?
![[#Definición]]

**¿Cuándo tiene sentido usar *grid search*?**
?
![[#Cuándo usarlo]]

**¿Cómo se compara *grid search* con *random search* y optimización bayesiana?**
?
![[#Comparación]]
