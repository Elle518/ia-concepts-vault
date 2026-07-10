---
type: concept
tags:
  - ml
  - review
---

## Definición

***Tree-structured Parzen Estimator*** (**TPE**) es un modelo sustituto usado en [[Optimización bayesiana|optimización bayesiana]] para elegir nuevas configuraciones de [[Hiperparámetros|hiperparámetros]].

En lugar de modelar directamente el rendimiento esperado dado un conjunto de hiperparámetros, TPE modela qué configuraciones son más probables entre los buenos resultados y cuáles son más probables entre los malos resultados.

La intuición es separar los experimentos anteriores en configuraciones prometedoras y no prometedoras. Luego se buscan nuevos puntos que se parezcan más al grupo bueno que al grupo malo.

## Funcionamiento

TPE divide las observaciones anteriores según un umbral de rendimiento:

- un grupo de configuraciones con buenos resultados
- un grupo de configuraciones con resultados peores

Después estima dos distribuciones:

- $l(x)$: probabilidad de una configuración $x$ entre los buenos resultados
- $g(x)$: probabilidad de una configuración $x$ entre los malos resultados

La siguiente configuración se elige favoreciendo puntos donde la relación entre ambas distribuciones sugiere alta probabilidad de mejora.

## Por qué se llama tree-structured

El nombre viene de su capacidad para manejar espacios de búsqueda condicionales o jerárquicos.

Por ejemplo, si elegimos `optimizer = Adam`, aparecen hiperparámetros como `beta1` y `beta2`; si elegimos `optimizer = SGD`, aparece `momentum`. El espacio no es una cuadrícula plana, sino un árbol de decisiones.

Esto hace que TPE sea práctico en herramientas de tuning donde hay hiperparámetros categóricos, condicionales y rangos mixtos.

## Comparación con procesos gaussianos

Los [[Proceso gaussiano|procesos gaussianos]] modelan una función de rendimiento con incertidumbre, y suelen funcionar bien en espacios continuos y con pocas evaluaciones.

TPE suele ser más flexible en espacios de hiperparámetros mixtos, categóricos o condicionales. Por eso aparece en herramientas de tuning como alternativa práctica para búsquedas complejas.

La idea clave es que ambos son modelos sustitutos, pero hacen supuestos distintos sobre cómo modelar el espacio de búsqueda.

## Errores comunes

- Pensar que TPE prueba configuraciones al azar sin aprender de resultados anteriores.
- Confundir TPE con una función de adquisición concreta, TPE es el modelo usado para guiar la búsqueda.
- Usarlo sin definir rangos y distribuciones razonables para los hiperparámetros.
- Asumir que siempre supera a [[Random search|random search]]; depende del presupuesto, el espacio y el ruido de evaluación.

## Preguntas

#flashcards/ml

**¿Qué es TPE en optimización bayesiana?**
?
![[#Definición]]

**¿Cómo funciona TPE a alto nivel?**
?
![[#Funcionamiento]]

**¿Por qué TPE se llama *tree-structured*?**
?
![[#Por qué se llama tree-structured]]

**¿En qué se diferencia TPE de un proceso gaussiano?**
?
![[#Comparación con procesos gaussianos]]

**¿Qué errores comunes hay al usar TPE?**
?
![[#Errores comunes]]
