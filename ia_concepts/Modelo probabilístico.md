---
type: concept
tags:
  - ml
  - llms
  - review
---

## Definición

Un **modelo probabilístico** es un modelo que representa [[Incertidumbre|incertidumbre]] mediante probabilidades.

En vez de producir necesariamente una única salida fija, asigna probabilidades a varias salidas posibles. En un [[Modelo del lenguaje|modelo de lenguaje]], esto significa estimar qué tokens o secuencias son más probables dado un contexto.

La intuición es que el modelo no dice solo “esta es la respuesta”, sino “estas son las continuaciones plausibles y esta es su probabilidad relativa”.

## En LLMs

Los LLMs son probabilísticos porque generan texto a partir de distribuciones sobre tokens. En cada paso, el modelo produce *[[Logit|logits]]*, estos se convierten en probabilidades y una estrategia de *[[Sampling|sampling]]* decide qué token se elige.

Esta naturaleza probabilística permite generar respuestas variadas, reformular ideas y ser útil en tareas creativas. Pero también hace que el modelo pueda producir salidas distintas ante el mismo *[[Prompt engineering|prompt]]* o ante variaciones pequeñas de la entrada.

Por eso la generación probabilística está relacionada con:

- Las [[Inconsistencia en LLMs|inconsistencias]]
- Las [[Alucinación en LLMs|alucinaciones]]
- La sensibilidad a los [[Parámetros de decoding|parámetros de decoding]]
- La dificultad de reproducibilidad

## Comparación con modelo determinista

Un [[Modelo determinista|modelo determinista]] produce la misma salida si recibe la misma entrada y el mismo estado.

Un modelo probabilístico puede tener varias salidas posibles. Incluso si una respuesta es muy probable, otras respuestas con probabilidad no nula también pueden aparecer si el proceso de generación las selecciona.

En producción, el objetivo no siempre es eliminar la probabilidad, sino controlarla para obtener:

- Más estabilidad para extracción, clasificación o código.
- Más diversidad para *brainstorming*, redacción o generación de alternativas.

## Errores comunes

- Pensar que una salida probable es necesariamente correcta.
- Atribuir toda alucinación solo al *sampling*, las causas también dependen del entrenamiento, supervisión, contexto y evaluación.
- Subir aleatoriedad esperando mejor razonamiento.
- Ignorar que la creatividad y la inconsistencia vienen del mismo espacio de posibles respuestas.

## Preguntas

#flashcards/ml #flashcards/llms

**¿Qué es un modelo probabilístico?**
?
![[#Definición]]

**¿Por qué los LLMs se consideran probabilísticos?**
?
![[#En LLMs]]

**¿En qué se diferencia un modelo probabilístico de un modelo determinista?**
?
![[#Comparación con modelo determinista]]

**¿Qué errores comunes hay al interpretar modelos probabilísticos?**
?
![[#Errores comunes]]
