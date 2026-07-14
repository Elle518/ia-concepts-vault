---
type: concept
tags:
  - llm
  - ml
  - nlp
  - review
---

## Definición

La **entropía** mide la [[Incertidumbre|incertidumbre]] de una distribución de probabilidad.

En *machine learning* aparece en tareas de [[Clasificación|clasificación]], [[Árbol de decisión|árboles de decisión]], [[Función de pérdida|funciones de pérdida,]] *[[Active learning|active learning]]* y [[Modelo probabilístico|modelos probabilísticos]].

Si una distribución está muy concentrada en una opción, hay poca incertidumbre y la entropía es baja.

Si la probabilidad está repartida entre muchas opciones parecidas, hay más incertidumbre y la entropía es alta.

## Fórmula

Para una [[Distribución discreta|distribución discreta]] $p$, la entropía se define como:

$$H(p) = - \sum_i p_i \log p_i$$

En clasificación, una predicción $[0.99, 0.01]$ tiene baja entropía. Una predicción $[0.5, 0.5]$ tiene mayor entropía porque el modelo está menos seguro.

## Usos en ML

- En **árboles de decisión**, puede usarse para medir [[Impureza|impureza]] y elegir divisiones.
- En ***active learning***, *entropy sampling* selecciona ejemplos con alta incertidumbre.
- En los **[[Modelo del lenguaje|modelos de lenguaje]],** la entropía de la distribución sobre tokens indica qué tan concentrada o abierta está la predicción.
- En ***[[Cross-entropy loss|cross-entropy loss]]***, se compara la distribución predicha con la distribución objetivo.

## Entropía en modelos del lenguaje

La entropía mide cuánta información, en promedio, contiene un [[Tokenización|token]]. Cuanto mayor sea la entropía, más información contiene cada token y más bits se necesitan para representarlo.

Veamos un ejemplo sencillo para ilustrarlo. Imaginemos que queremos crear un lenguaje para describir posiciones dentro de un cuadrado:

- Si el lenguaje tiene solo dos tokens, cada token podría, por ejemplo, indicar si la posición es superior o inferior. Como solo hay dos tokens, un bit es suficiente para representarlos. Por lo tanto, la entropía de este lenguaje es 1.
- Si el lenguaje tiene cuatro tokens, cada token proporciona una posición más específica, por ejemplo, superior izquierda, superior derecha, inferior izquierda o inferior derecha. Sin embargo, como ahora hay cuatro tokens y necesitamos dos bits para representarlos. La entropía de este lenguaje es 2.

El segundo lenguaje tiene mayor entropía, ya que cada token contiene más información, pero requiere más bits para su representación. 

Intuitivamente, la entropía mide la dificultad de predecir lo que viene a continuación en un idioma. Cuanto menor sea la entropía de un idioma (menos información contiene cada palabra), más predecible será.

## Preguntas

#flashcards/llms #flashcards/ml #flashcards/nlp 

**¿Qué mide la entropía?**
?
![[#Definición]]

**¿Cómo se calcula la entropía de una distribución discreta?**
?
![[#Fórmula]]

**¿Dónde aparece la entropía en *machine learning*?**
?
![[#Usos en ML]]

**¿Qué mide la entropía en los modelos del lenguaje?**
?
![[#Entropía en modelos del lenguaje]]
