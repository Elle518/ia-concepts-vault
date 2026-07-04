---
type: concept
tags:
  - dl
  - ml
  - review
---

## Definición

***Backpropagation*** es el algoritmo usado para calcular cómo debe cambiar cada [[Parámetro|parámetro]] de una [[Red neuronal|red neuronal]] para reducir la [[Función de pérdida|función de pérdida]].

Calcula [[Gradiente|gradientes]] propagando el error desde la salida hacia las capas anteriores.

Primero la red hace una predicción. Después se mide cuánto se ha equivocado.

*Backpropagation* reparte la responsabilidad de ese error entre las capas y pesos de la red, indicando en qué dirección habría que mover cada parámetro para mejorar.

## Funcionamiento

El entrenamiento de una red neuronal suele seguir este ciclo:

1. **Forward pass**: la entrada atraviesa la red y se obtiene una predicción.
2. **[[Función de pérdida|Loss]]**: se compara la predicción con el objetivo real.
3. **Backward pass**: se calculan gradientes usando la [[Regla de la cadena|regla de la cadena]].
4. **Actualización**: un [[Optimizador|optimizador]] usa esos gradientes para modificar los pesos.

*Backpropagation* no decide por sí solo cuánto actualizar los pesos. Eso lo controla el optimizador y sus [[Hiperparámetros|hiperparámetros]], como el *[[Tasa de aprendizaje|learning rate]]*.

## Errores comunes

- Confundir *backpropagation* con el optimizador.
- Pensar que *backpropagation* solo funciona en redes profundas.
- Olvidar que calcula gradientes, no garantiza encontrar el [[Mínimos global y local|mínimo global.]]
- Ignorar problemas como gradientes que [[Exploding gradients|explotan]] o [[Vanishing gradients|desaparecen]].

## Preguntas

#flashcards/dl #flashcards/ml

**¿Qué es *backpropagation*?**
?
![[#Definición]]

**¿Cuáles son los pasos básicos de entrenamiento con *backpropagation*?**
?
![[#Funcionamiento]]

**¿Qué errores comunes se comenten en *backpropagation*?**
?
![[#Errores comunes]]
