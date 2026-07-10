---
type: concept
tags:
  - ml
  - llms
  - review
---

## Definición

***Logprobs***, abreviatura de probabilidades logarítmicas, son probabilidades en escala logarítmica. Se prefiere la escala logarítmica cuando se trabaja con las probabilidades de una red neuronal porque ayuda a reducir el **[[Underflow problem|problema de desbordamiento]]**.

El problema del desbordamiento se produce cuando un número es demasiado pequeño para representarse en un formato determinado, lo que hace que se redondee a cero.

Un modelo de lenguaje podría estar trabajando con un tamaño de vocabulario de 100.000, lo que significa que las probabilidades de muchos de los tokens pueden ser demasiado pequeñas para ser representadas por una máquina. Los números pequeños podrían redondearse a 0 y la escala logarítmica ayuda a reducir este problema.

Muchos proveedores de modelos no exponen los *logprobs* de sus modelos, o si lo hacen, la API de logprobs es limitada. Esta limitación probablemente se debe a razones de seguridad, ya que los *logprobs* expuestos de un modelo facilitan que otros repliquen el modelo.

## Cálculo

Si conocemos la probabilidad de un evento, su *logprob* se calcula aplicando el logaritmo:

$$\text{logprob}(x) = \log P(x)$$

Por ejemplo, si un token tiene probabilidad $0.2$:

$$\log(0.2) \approx -1.61$$

En un [[Modelo del lenguaje|modelo de lenguaje]], normalmente partimos de [[Logit|logits]], no de probabilidades. Primero se aplica [[Softmax|softmax]] para obtener la probabilidad de cada token:

$$P(x_i) = \frac{e^{z_i}}{\sum_j e^{z_j}}$$

Después se toma el logaritmo:

$$\log P(x_i) = \log \frac{e^{z_i}}{\sum_j e^{z_j}}$$

En la práctica suele calcularse directamente con **[[Log-softmax|log-softmax]]**, porque es más estable numéricamente que aplicar softmax y luego logaritmo.

Para una secuencia de tokens, la *logprob* total es la suma de las *logprobs* de cada token condicionado por los tokens anteriores:

$$\log P(x_1, \dots, x_T) = \sum_{t=1}^{T} \log P(x_t \mid x_{<t})$$

Como las *logprobs* suelen ser negativas, las secuencias largas tienden a tener una suma menor. Por eso, al comparar respuestas de distinta longitud, a veces se usa la *logprob* media por token.

## Preguntas

#flashcards/ml #flashcards/llms

**¿Qué son las *logprobs*?**
?
![[#Definición]]

**¿Cómo se calculan las *logprobs* de tokens y secuencias?**
?
![[#Cálculo]]
