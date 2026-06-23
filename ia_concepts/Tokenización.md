---
type: concept
tags:
  - nlp
  - review
---

## Definición

La **tokenización** se refiere al proceso de dividir un texto, como una palabra, una oración o un documento, en unidades más pequeñas llamadas **tokens**.

Estos tokens pueden ser palabras, subpalabras o caracteres, dependiendo del nivel de tokenización.

Un **token** es la unidad básica de un texto o un modelo del lenguaje, como una palabra, subpalabra o carácter, generada durante el proceso de tokenización.

Es uno de los pasos fundamentales en el preprocesamiento de los textos, el cual nos permite transformarlos en una forma que pueda ser utilizada por los algoritmos de aprendizaje automático.

Así, después de la tokenización, estos tokens a menudo se convierten en ***[[Embeddings|embeddings]]*** o vectores numéricos que ya sí que pueden ser procesados por los algoritmos de PLN.

## Tipos de tokenización

1. **[[Tokenización a nivel de palabras|Tokenización por palabras]]** → Divide el texto en palabras individuales. Por ejemplo, la oración `"La ciencia de datos es divertida"` se tokenizaría en `["La", "ciencia", "de", "datos", "es", "divertida"]`.
2. **[[Tokenización a nivel de subpalabras|Tokenización por subpalabras]]** → Divide el texto en subunidades significativas. Esto es útil para manejar palabras desconocidas o raras. Por ejemplo, en `"magníficamente"`, podríamos tokenizar en `["magnífica", "mente"]`.
3. **[[Tokenización a nivel de caracteres|Tokenización por caracteres]]** → Divide el texto en caracteres individuales, como `["D", "a", "t", "o", "s"]`.

### Tokens de subpalabras

Por lo general, los modelos de lenguaje utilizan **tokens de subpalabras** como unidad en lugar de palabras o caracteres por tres razones principales:

1. En comparación con los caracteres, los tokens de subpalabras permiten al modelo dividir las palabras en componentes significativos. Por ejemplo, “rápidamente” se puede dividir en “rápida” y “-mente”, conservando ambos componentes parte del significado de la palabra original.
2. Dado que hay menos tokens únicos que palabras únicas, esto reduce el tamaño del vocabulario del modelo, haciéndolo más eficiente.
3. Los tokens de subpalabras también ayudan al modelo a procesar palabras desconocidas. Por ejemplo, una palabra inventada como “googleando” podría dividirse en “google” y “-ando”, lo que ayuda al modelo a comprender su estructura.

Así, los tokens de subpalabras ofrecen un equilibrio entre tener menos unidades que las palabras y conservar más significado que los caracteres individuales.

## Desafíos en la tokenización

- **Ambigüedad**. En lenguajes como el chino, donde no hay espacios entre las palabras, tokenizar correctamente es más complejo.
- **Manejo de la puntuación**. Decidir si se trata la puntuación como tokens separados o se ignora.
- **Palabras compuestas**. En idiomas como el alemán, las palabras compuestas largas requieren un manejo especial para descomponerlas correctamente.

## Preguntas

¿Qué es la tokenización y por qué es importante en el procesamiento de lenguaje natural?
?
[[Tokenización#Definición]]

¿Cuáles son los diferentes tipos de tokenización?
?
[[Tokenización#Tipos de tokenización]]

¿Por qué los modelos de lenguaje utilizan tokens de subpalabras como unidad en lugar de palabras o caracteres?
?
[[Tokenización#Tokens de subpalabras]]

¿Cuáles son algunos desafíos comunes en la tokenización de textos?
?
[[Tokenización#Desafíos en la tokenización]]
