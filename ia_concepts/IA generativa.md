---
type: concept
tags:
  - llms
  - ml
  - review
---

## Definición

La **IA generativa** o *generative AI* es una familia de sistemas de IA capaces de crear contenido nuevo, como texto, imágenes, audio, vídeo, código o datos sintéticos.

En la práctica moderna suele basarse en [[Modelo fundacional|modelos fundacionales]], como [[Modelo del lenguaje|modelos de lenguaje]] grandes, modelos de difusión o modelos multimodales.

## Modelo discriminativo vs generativo

Un [[Modelo discriminativo|modelo discriminativo]] suele responder "qué clase es esto". Un [[Modelo generativo|modelo generativo]] intenta producir algo nuevo que encaje con lo aprendido.

Por ejemplo, un clasificador puede decir si una reseña es positiva; un modelo generativo puede escribir una respuesta, resumir la reseña o crear variantes de un texto.

## Funcionamiento

La IA generativa aprende patrones de una distribución de datos y usa esos patrones para generar nuevas muestras plausibles.

En modelos de lenguaje autorregresivos, generar texto suele consistir en predecir el siguiente [[Tokenización|token]] repetidamente a partir del contexto. En modelos de imagen, una técnica común es aprender a generar una imagen a partir de ruido condicionado por un *prompt*.

La capacidad generativa no garantiza veracidad. El modelo puede producir contenido fluido pero incorrecto, incompleto o no fundamentado.

## Preguntas

#flashcards/ml #flashcards/llms

**¿Qué es la IA generativa?**
?
![[#Definición]]

**¿Cómo se diferencia un modelo generativo de uno discriminativo?**
?
![[#Modelo discriminativo vs generativo]]

**¿Cómo funciona la IA generativa?**
?
![[#Funcionamiento]]
