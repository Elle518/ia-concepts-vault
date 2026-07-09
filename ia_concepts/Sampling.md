---
type: concept
tags:
  - llms
  - ml
  - nlp
  - review
---

## Definición

**Sampling** es el proceso por el que un modelo elige una salida concreta a partir de una distribución de probabilidad sobre posibles salidas.

Dada una entrada, una red neuronal produce una salida calculando primero las probabilidades de los posibles resultados. En un modelo de clasificación, los posibles resultados son las clases disponibles. En un modelo de lenguaje, para generar el siguiente token, el modelo calcula primero la distribución de probabilidad sobre todos los tokens del vocabulario.

En [[Modelo del lenguaje|modelos de lenguaje]], *sampling* suele referirse a cómo se selecciona el siguiente token durante la generación. Esta elección puede hacer que las respuestas sean más deterministas, más variadas, más creativas o más inconsistentes.

Un modelo no genera texto eligiendo directamente una única palabra “correcta”. En cada paso calcula qué tokens son más o menos probables.

Si el contexto es “Mi color favorito es”, el modelo puede asignar más probabilidad a “azul” o “rojo” que a “tenedor”. El *sampling* decide si se elige siempre el token más probable o si se permite escoger otros tokens según su probabilidad.

## Funcionamiento

En una red neuronal, la salida previa a las probabilidades suele ser un vector de *[[Logit|logits]]*. En un modelo de lenguaje, hay un *logit* por cada token del vocabulario.

Los *logits* no son probabilidades, pueden ser negativos y no suman 1. Para convertirlos en una distribución de probabilidad se suele aplicar *[[Softmax|softmax]]*:

$$p_i = \frac{e^{x_i}}{\sum_j e^{x_j}}$$

Después, el sistema selecciona el siguiente token usando una estrategia de *[[Parámetros de decoding|decoding]]*. Por ejemplo:

- ***[[Greedy sampling]]*** elige siempre el resultado o token más probable. Esto suele funcionar bien en tareas de clasificación, sin embargo, en un modelo de lenguaje, genera resultados poco interesantes.
- ***[[Top-k sampling]]*** muestrea solo entre los $k$ tokens más probables.
- ***[[Top-p sampling]]*** muestrea entre el conjunto mínimo de tokens que acumula una probabilidad $p$.
- **[[Temperatura]]** modifica cuánta aleatoriedad tiene la distribución antes de muestrear.

## Por qué importa

El *sampling* explica por qué un mismo modelo puede producir respuestas distintas ante el mismo *[[Prompt engineering|prompt]]*.

Elegir bien la estrategia de *sampling* puede mejorar mucho el comportamiento de una aplicación sin cambiar los pesos del modelo. Para tareas factuales o estructuradas suele interesar un *sampling* más conservador. Para *brainstorming* o escritura creativa puede interesar permitir más diversidad.

La parte importante es que más aleatoriedad no significa mejor razonamiento. Solo cambia cómo se explora la distribución de salidas posibles.

## Errores comunes

- Confundir *sampling* con conocimiento del modelo. El *sampling* decide cómo elegir una salida, no añade información nueva.
- Pensar que una respuesta determinista es necesariamente correcta.
- Subir la temperatura esperando más precisión, cuando normalmente aumenta la variabilidad.
- Ajustar *sampling* sin evaluar ejemplos reales del caso de uso.
- Ignorar que los parámetros de *sampling* interactúan entre sí.

## Preguntas

#flashcards/llms #flashcards/nlp

**¿Qué es sampling en un modelo de lenguaje?**
?
![[#Definición]]

**¿Cuál es la intuición detrás del sampling?**
?
![[#Intuición]]

**¿Cómo pasa un modelo de logits a probabilidades antes de hacer sampling?**
?
![[#Funcionamiento]]

**¿Por qué importa elegir bien la estrategia de sampling?**
?
![[#Por qué importa]]

**¿Qué errores comunes aparecen al ajustar sampling?**
?
![[#Errores comunes]]
