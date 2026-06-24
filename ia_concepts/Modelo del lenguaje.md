---
type: concept
tags:
  - llms
  - nlp
  - review
---

## Definición

Un **modelo de lenguaje** codifica información estadística sobre uno o más idiomas.

Intuitivamente, esta información nos indica la probabilidad de que una palabra aparezca en un contexto determinado. Por ejemplo, en el contexto “Mi color favorito es __”, un modelo de lenguaje que codifica el espñol debería predecir “azul” con más frecuencia que “coche”.

## Modelado del lenguaje

El **modelado del lenguaje** es la tarea de construir un modelo capaz de asignar probabilidades a secuencias de palabras, tokens o caracteres.

Dicho de forma sencilla, consiste en entrenar un sistema para que aprenda **qué secuencias de lenguaje son más probables que otras**. Por ejemplo, después de la frase:

> “El cielo es de color…”

un modelo de lenguaje debería asignar más probabilidad a “azul” que a “tenedor”.

En la práctica, un modelo de lenguaje suele aprender a predecir el siguiente token a partir del contexto anterior:

$$P(w_t \mid w_1, w_2, \dots, w_{t-1})$$

Es decir, la probabilidad de la palabra o token actual $w_t$ dado todo lo que ha aparecido antes.

El modelado del lenguaje es la base de muchas tareas de NLP, como generación de texto, traducción automática, autocompletado, corrección ortográfica, resumen automático o chatbots.

En resumen, modelar el lenguaje significa aprender la estructura estadística del lenguaje para poder estimar qué textos son más probables y generar o evaluar secuencias lingüísticas.

## Aprendizaje autosupervisado

Los modelos del lenguaje generalmente se entrenan usando [[Aprendizaje autosupervisado|aprendizaje autosupervisado]] o autosupervisión (*self-supervision*).

El aprendizaje autosupervisado permite que los modelos de lenguaje aprendan de secuencias de texto sin necesidad de etiquetas. Dado que las secuencias de texto están presentes en todas partes (libros, publicaciones de blogs, artículos y comentarios de Reddit), es posible generar una enorme cantidad de datos de entrenamiento, lo que permite que los modelos de lenguaje escalen hasta convertirse en grandes modelos del lenguaje (LLMs).

## Vocabulario

El conjunto de todos los tokens con los que un modelo puede trabajar constituye su **vocabulario**. Se puede utilizar un número reducido de tokens para construir una gran cantidad de palabras distintas, de forma similar a como se pueden utilizar unas pocas letras del alfabeto para formar muchas palabras. 

El método de [[Tokenización|tokenización]] y el tamaño del vocabulario los deciden los desarrolladores del modelo.

## Tipos de modelos del lenguaje

Existen dos tipos principales de modelos de lenguaje, y se diferencian en la información que utilizan para predecir un token:

### Modelo del lenguaje enmascarado

Un **modelo del lenguaje enmascarado** (*masked language model*) se entrena para predecir tokens faltantes en cualquier parte de una secuencia, utilizando el contexto anterior y posterior a dichos tokens.

En esencia, este modelo se entrena para completar la información faltante. Por ejemplo, dado el contexto “Mi __ favorito es el azul”, un modelo de lenguaje enmascarado debería predecir que la palabra faltante probablemente sea "color".

Un ejemplo conocido de este tipo de modelo es BERT.

Actualmente, los modelos del lenguaje enmascarados se utilizan comúnmente para tareas no generativas, como el análisis de sentimientos y la clasificación de texto. También son útiles para tareas que requieren la comprensión del contexto general, como la depuración de código, donde un modelo necesita comprender tanto el código anterior como el posterior para identificar errores.

### Modelo del lenguaje autorregresivo

Un **modelo de lenguaje autorregresivo** (*autoregressive language model*) se entrena para predecir el siguiente token en una secuencia, utilizando únicamente los tokens anteriores. Predice lo que sigue en “Mi color favorito es __”.

Un modelo autorregresivo puede generar continuamente un token tras otro. Hoy en día, los modelos de lenguaje autorregresivos son los modelos preferidos para la generación de texto y, por esta razón, son mucho más populares que los modelos de lenguaje enmascarados.

Los resultados de los modelos de lenguaje son abiertos. Un modelo de lenguaje puede usar su vocabulario fijo y finito para construir un número infinito de posibles resultados. Un modelo que puede generar resultados abiertos se denomina **[[Modelos generativos|modelo generativo]]**, de ahí el término **IA generativa**.

Es importante tener en cuenta que las sugerencias de autocompletado son predicciones basadas en probabilidades y no se garantiza su exactitud, es decir, que sean correctas.

## Grandes modelos del lenguaje

El tamaño de un modelo se suele medir por su número de [[Parámetro|parámetros]]. En general, aunque no siempre es así, cuantos más parámetros tenga un modelo, mayor será su capacidad para aprender los comportamientos deseados.

El problema es que lo que hoy se considera un modelo grande del lenguaje (*large languaje model* o LLM), mañana podría considerarse pequeño. 

Hoy en día, un modelo con 100 mil millones de parámetros se considera grande.

Los modelos más grandes tienen mayor capacidad de aprendizaje y, por lo tanto, requieren más datos de entrenamiento para maximizar su rendimiento. Si bien es posible entrenar un modelo grande con un conjunto de datos pequeño, esto supondría un desperdicio de recursos computacionales. Se podrían haber obtenido resultados similares o incluso mejores con modelos más pequeños.

Parece contradictorio que los modelos más grandes requieran más datos de entrenamiento. Si un modelo es más potente, ¿no debería necesitar menos ejemplos para aprender? Sin embargo, no buscamos que un modelo grande iguale el rendimiento de un modelo pequeño con los mismos datos. Buscamos maximizar el rendimiento del modelo.

## Preguntas

#flashcards/nlp 

**¿Qué es un modelo del lenguaje?**
?
![[#Definición]]

**¿Qué se entiende por modelado del lenguaje?**
?
![[#Modelado del lenguaje]]

**¿Qué representa el vocabulario de un modelo del lenguaje?**
?
![[#Vocabulario]]

**¿Qué tipos de modelos del lenguaje existen?**
?
![[#Tipos de modelos del lenguaje]]

**¿Qué son los llamados grandes modelos del lenguaje (LLMs)?**
?
![[#Grandes modelos del lenguaje]]