---
type: concept
tags:
  - nlp
  - review
---

## Definición

La ***perplexity*** o **perplejidad** es una métrica que mide lo bien que un [[Modelo del lenguaje|modelo de lenguaje]] predice una secuencia de texto, es decir, mide el grado de sorpresa o incertidumbre del modelo ante un texto.

De forma intuitiva, indica **cuántas opciones razonables está considerando el modelo en cada predicción**. Cuanto más baja es la *perplexity*, mejor: significa que el modelo está menos “perplejo” y asigna mayor probabilidad al texto correcto.

Así, una *perplexity* baja indica que el modelo predice bien el texto, mientras que una *perplexity* alta indica que el texto le resulta más difícil o improbable.

Por ejemplo, si un modelo tiene una *perplexity* de 10, puede interpretarse aproximadamente como que, en promedio, el modelo duda entre unas 10 opciones posibles en cada paso.

## Fórmula de la *perplexity*

Formalmente, si la [[Entropía|entropía]] media del modelo es $H$, la *perplexity* se define como:

$$\text{Perplexity} = e^H$$

O, usando logaritmo en base 2:

 $$\text{Perplexity} = 2^H$$

En modelos de lenguaje también suele expresarse como:

$$\text{PPL}(w_1, \dots, w_N) =  
\exp\left(  
-\frac{1}{N}  
\sum_{i=1}^{N}  
\log P(w_i \mid w_1, \dots, w_{i-1})  
\right)$$

donde el modelo asigna una probabilidad al token correcto en cada posición.

## Preguntas

#flashcards/nlp 

¿Qué es la *perplexity*?
?
[[Perplexity#Definición]]

¿Cómo se calcula la *perplexity*?
?
[[Perplexity#Fórmula de la *perplexity*]]