---
type: concept
tags:
  - llms
  - metrics
  - nlp
  - review
---

## Definición

***Exact match*** evalúa si la respuesta generada coincide exactamente con una respuesta de referencia.

Normalmente produce una puntuación binaria: coincide o no coincide.

Es un subtipo de [[Evaluación por referencia|evaluación por referencia]] y, a su vez, de [[Evaluación exacta en LLMs|evaluación exacta]].

## Cuándo usarlo

Funciona bien en tareas con respuestas cortas y cerradas:

- preguntas de matemáticas simples
- trivia
- opción múltiple
- extracción de campos estructurados
- respuestas canónicas muy concretas

Por ejemplo, si la referencia es `5`, la respuesta `5` es correcta.

## Variantes

Una variante flexible acepta respuestas que contienen la referencia.

Por ejemplo, si la referencia es `5`, podría aceptar `La respuesta es 5`.

Esto ayuda con diferencias de formato, pero puede aceptar errores. Si la referencia es `1929`, una respuesta como `Anne Frank nació el 12 de septiembre de 1929` contiene el año correcto, pero la fecha completa es falsa.

## Limitaciones

En tareas abiertas rara vez funciona bien.

Una traducción, un resumen o una explicación pueden ser correctos aunque no coincidan exactamente con las referencias disponibles.

Cuanto más larga y compleja sea la respuesta, más difícil es enumerar todas las respuestas válidas para una cierta entrada.

## Preguntas

#flashcards/llms #flashcards/metrics #flashcards/nlp 

**¿Qué mide *exact match*?**
?
![[#Definición]]

**¿Cuándo conviene usar *exact match*?**
?
![[#Cuándo usarlo]]

**¿Qué riesgo tiene aceptar respuestas que contienen la referencia en *exact match*?**
?
![[#Variantes]]

**¿Qué limitaciones tiene *exact match*?**
?
![[#Limitaciones]]
