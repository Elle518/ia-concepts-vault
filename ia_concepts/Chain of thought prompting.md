---
type: concept
tags:
  - llms
  - nlp
  - review
---

## Definición

El ***chain-of-thought prompting*** (*CoT prompting*) es una técnica de [[Prompt engineering|prompting]] en la que se incentiva al modelo a descomponer un problema en pasos intermedios antes de dar la respuesta final.

La idea es hacer explícito un razonamiento que, en lugar de comprimirse en una sola respuesta, se organiza como una secuencia de pasos más manejable.

Es como pedirle a alguien que enseñe el desarrollo de un ejercicio, no solo el resultado. Cuando una tarea tiene varios saltos lógicos, dividirla suele ayudar a reducir errores.

## Utilidad

CoT suele funcionar mejor en tareas con:

- razonamiento multietapa
- problemas aritméticos o lógicos
- preguntas con dependencias intermedias
- tareas donde una explicación paso a paso mejora la trazabilidad

Puede aparecer de forma explícita, pidiendo pasos intermedios, o de manera más indirecta usando *prompts* que fuerzan descomposición. En producción, a veces interesa más la calidad de la respuesta que exponer todo el razonamiento, así que hay que distinguir entre el razonamiento interno del modelo y lo que queremos mostrar al usuario.

## Errores comunes

- Pensar que más razonamiento visible siempre implica mejor respuesta.
- Usar CoT en tareas simples donde añade coste sin aportar valor.
- Confundir la explicación generada con una prueba real de corrección.

## Preguntas

#flashcards/llms #flashcards/nlp 

**¿Qué es *chain-of-thought prompting*?**
?
![[#Definición]]

**¿En qué tipos de tareas suele ser útil el *chain-of-thought prompting*?**
?
![[#Utilidad]]

**¿Qué errores debemos evitar en *chain-of-thought prompting***
?
![[#Errores comunes]]

