---
type: concept
tags:
  - llms
  - metrics
  - ml
  - review
---

## Definición

La ***cross-entropy***, o **entropía cruzada**, mide cuántos [[Bit|bits]] o [[Nat|nats]] hacen falta, en promedio, para representar datos que siguen una distribución real $P$ usando una distribución aproximada $Q$.

Cuanto menor es la *cross-entropy*, mejor está asignando probabilidad el modelo a los eventos reales.

La *cross-entropy* mide el coste de usar el “mapa probabilístico” equivocado. Si el modelo asigna mucha probabilidad a lo que realmente ocurre, necesita poca información extra para explicar los datos. Si asigna poca probabilidad a los valores correctos, la *cross-entropy* sube.

## Fórmula

La [[Entropía|entropía]] y la entropía cruzada comparten la misma notación matemática, $H$. Si $P$ es la distribución real de los datos y $Q$ la distribución aprendida o estimada por el modelo, la entropía cruzada se calcula de la siguiente manera:

$$H(P, Q) = - \sum_x P(x)\log Q(x)$$

También puede descomponerse como:

$$H(P, Q) = H(P) + D_{KL}(P \| Q)$$

Así, podemos identificar en la fórmula dos componentes:

- La **entropía** propia de los datos, $H(P)$.
- La distancia entre la distribución real ($P$) y la distribución del modelo ($Q$), medida por la **[[Divergencia de Kullback–Leibler|divergencia de Kullback–Leibler]]**, $D_{KL}(P \| Q)$.

Si el modelo aprendiera perfectamente la distribución real, $Q = P$, entonces $D_{KL}(P \| Q)=0$ y la entropía cruzada coincidiría con la entropía de los datos.

Cuidado, la *cross-entropy* no es simétrica, es decir, $H(P,Q)$ no significa lo mismo que $H(Q,P)$.

## En modelos del lenguaje

Cuando entrenamos un [[Modelo del lenguaje|modelo del lenguaje]] en un conjunto de datos, nuestro objetivo es lograr que el modelo aprenda la distribución de estos datos de entrenamiento. En otras palabras, el objetivo es lograr que el modelo prediga lo que sigue en los datos de entrenamiento.

En modelos del lenguaje, la entropía cruzada se usa como métrica para medir lo difícil que le resulta al modelo predecir el siguiente [[Tokenización|token]] de un conjunto de datos.

Así, en un modelo autorregresivo, la entropía cruzada sobre un dataset mide la dificultad promedio de predecir el siguiente token, de modo que una *cross-entropy* baja significa que el texto evaluado es más predecible para el modelo.

La entropía cruzada depende de dos cosas:

- La predictibilidad del conjunto de datos, medido por la entropía de los datos de entrenamiento.
- Lo cerca que está la distribución aprendida por el modelo de la distribución real del conjunto de datos.

Por eso puede interpretarse como una medida de calidad probabilística del modelo sobre esos datos.

Un modelo de lenguaje se entrena para minimizar su entropía cruzada con respecto a los datos de entrenamiento. Si el modelo de lenguaje aprende perfectamente de sus datos de entrenamiento, la entropía cruzada del modelo será exactamente la misma que la entropía de los datos de entrenamiento, y la divergencia KL de $Q$ con respecto a $P$ será entonces 0. Podemos pensar en la entropía cruzada de un modelo como su aproximación a la entropía de sus datos de entrenamiento.

La [[Perplexity|perplexity]] está directamente relacionada con la *cross-entropy*, de modo que una menor *cross-entropy* implica menor *perplexity*.

## Diferencia con cross-entropy loss

La *cross-entropy* es una cantidad teórica o métrica entre distribuciones.

La [[Cross-entropy loss|cross-entropy loss]] es la función de pérdida concreta que se minimiza durante el entrenamiento de modelos, normalmente calculada sobre muestras o batches de muestras.

En la práctica están muy relacionadas: entrenar con *cross-entropy loss* minimiza una estimación empírica de la *cross-entropy* entre la distribución de datos y la distribución del modelo.

## Errores comunes

- Confundir entropía cruzada con entropía. La entropía mide la incertidumbre de una distribución, mientras que la entropía cruzada compara una distribución real con una aproximada.
- Tratarla como si fuera simétrica.
- Comparar valores de entropía cruzada entre datasets, vocabularios o tokenizadores distintos sin contexto.
- Confundir la métrica agregada sobre un dataset con la pérdida usada en cada paso de entrenamiento.

## Preguntas

#flashcards/llms #flashcards/ml #flashcards/metrics  

**¿Qué mide la *cross-entropy*?**
?
![[#Definición]]

**¿Cuál es la fórmula de la entropía cruzada? ¿Cómo se relacionan *cross-entropy*, entropía y divergencia KL?**
?
![[#Fórmula]]

**¿Qué mide la *cross-entropy* en modelos del lenguaje?**
?
![[#En modelos del lenguaje]]

**¿En qué se diferencia *cross-entropy* de *cross-entropy loss*?**
?
![[#Diferencia con cross-entropy loss]]

**¿Qué errores se suelen cometer con respecto a la *cross-entropy*?**
?
![[#Errores comunes]]
