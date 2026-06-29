---
type: concept
tags:
  - llms
  - nlp
  - review
---

## Definición

El ***self-consistency prompting*** es una técnica de *[[Prompt engineering|prompt engineering]]* en la que se generan varias soluciones o trazas de razonamiento para la misma pregunta y se elige la respuesta más consistente entre ellas.

En vez de confiar en una única salida del [[Modelo del lenguaje|modelo de lenguaje]], se muestrean varias respuestas y se agrega el resultado, por ejemplo con voto mayoritario.

Es como pedir a varias personas que resuelvan el mismo problema de forma independiente. Si muchas llegan a la misma respuesta, aumenta la confianza en que esa respuesta sea correcta.

## Utilidad

Self-consistency suele combinarse con *[[Chain of thought prompting|chain-of-thought prompting]]*. El flujo típico es:

- generar varias cadenas de razonamiento para la misma entrada
- extraer la respuesta final de cada una
- seleccionar la respuesta más frecuente o más coherente

Funciona mejor en tareas donde hay una respuesta final verificable, como problemas de razonamiento, matemáticas, lógica o clasificación compleja. Aumenta el coste porque requiere varias llamadas o varias muestras del modelo.

## Errores comunes

- Usarlo en tareas abiertas donde no hay una respuesta claramente agregable.
- Pensar que la respuesta mayoritaria siempre es correcta.
- No controlar la diversidad del muestreo y obtener varias respuestas casi idénticas.
- Ignorar el coste extra de generar múltiples soluciones.

## Preguntas

#flashcards/llms #flashcards/nlp

**¿Qué es *self-consistency prompting*?**
?
![[#Definición]]

**¿Cómo se usa el *self-consistency prompting*?**
?
![[#Utilidad]]

**¿Qué limitación importante tiene *self-consistency prompting*?**
?
![[#Errores comunes]]
