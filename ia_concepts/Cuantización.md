---
type: concept
tags:
  - llms
  - ml
  - review
---

## Definición

La **cuantización** es una técnica que representa números de un modelo con menos precisión, por ejemplo usando 8 bits o 4 bits en vez de 16 o 32.

En modelos de *machine learning* se usa para reducir memoria, acelerar inferencia y facilitar despliegues en *hardware* limitado.

La idea es aproximar pesos o activaciones con formatos más pequeños manteniendo una calidad aceptable.

Un modelo grande guarda millones o miles de millones de números. Si cada número ocupa menos espacio, el modelo cabe mejor en memoria y puede moverse más rápido entre memoria y cómputo.

El coste es que la representación es menos precisa y puede introducir error numérico.

## Tipos habituales

- ***Post-training quantization***: se cuantiza un modelo ya entrenado.
- ***Quantization-aware training***: se entrena simulando la cuantización para que el modelo se adapte.
- ***Weight-only quantization***: se cuantizan solo los pesos.
- ***Activation quantization***: también se cuantizan activaciones intermedias.

En LLMs, la cuantización de pesos a 8-bit o 4-bit es común para reducir el coste de inferencia.

## Trade-offs

La cuantización reduce el uso de memoria y puede mejorar la latencia, pero puede afectar a la calidad.

El impacto depende de:

- número de bits
- método de cuantización
- tamaño del modelo
- sensibilidad de ciertas capas
- *hardware* disponible

No toda cuantización acelera automáticamente, es decir, cuantizar no siempre mejora la latencia. Si el *hardware* o las librerías no soportan bien el formato, puede reducir memoria sin mejorar velocidad.

Hay que tener cuidado con usar demasiada poca precisión en capas sensibles.

## Preguntas

#flashcards/ml #flashcards/llms

**¿Qué es la cuantización en modelos de *machine learning*?**
?
![[#Definición]]

**¿Qué tipos de cuantización son habituales?**
?
![[#Tipos habituales]]

**¿Qué *trade-offs* tiene cuantizar un modelo?**
?
![[#Trade-offs]]
