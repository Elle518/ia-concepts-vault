---
type: concept
tags:
  - ml
  - llms
  - review
---

## Definición

Un **modelo determinista** es un modelo o sistema que, dadas las mismas entradas y el mismo estado, produce siempre la misma salida.

No hay variación aleatoria en el resultado. Si todo se mantiene igual, la salida se puede predecir de forma exacta.

La intuición es una función matemática clásica, en la que si introduces el mismo valor dos veces, obtienes el mismo resultado dos veces.

## En LLMs

Los [[Modelo del lenguaje|modelos de lenguaje]] suelen comportarse de forma menos determinista porque generan texto mediante *[[Sampling|sampling]]* sobre una distribución de probabilidad.

Aun así, un sistema con LLM puede intentar acercarse a un comportamiento determinista usando:

- *[[Greedy decoding]]*
- [[Temperatura]] baja o cercana a 0
- [[Parámetros de decoding]] fijos
- [[Seed en generación]] fija cuando el proveedor lo permite
- [[Caché de respuestas]] para entradas idénticas

Esto mejora la reproducibilidad, pero no siempre garantiza salidas idénticas. Puede seguir habiendo no determinismo por detalles de infraestructura, paralelismo, *hardware* o implementación del proveedor.

## Comparación con modelo probabilístico

Un modelo determinista intenta mapear cada entrada a una salida estable.

Un [[Modelo probabilístico|modelo probabilístico]], en cambio, modela una distribución de posibles salidas. En generación de texto, eso permite creatividad y diversidad, pero también introduce variabilidad, [[Inconsistencia en LLMs|inconsistencias]] y riesgo de [[Alucinación en LLMs|alucinaciones]].

## Errores comunes

- Pensar que temperatura 0 garantiza reproducibilidad perfecta en cualquier API.
- Confundir salida estable con salida correcta.
- Usar un LLM para tareas que deberían resolverse con reglas, funciones o pipelines deterministas.
- Ignorar que un sistema completo puede dejar de ser determinista aunque una parte del *pipeline* sí lo sea.

## Preguntas

#flashcards/ml #flashcards/llms

**¿Qué es un modelo determinista?**
?
![[#Definición]]

**¿Cómo se puede hacer que un sistema con LLM sea más determinista?**
?
![[#En LLMs]]

**¿En qué se diferencia un modelo determinista de un modelo probabilístico?**
?
![[#Comparación con modelo probabilístico]]

**¿Qué errores comunes hay al buscar determinismo en LLMs?**
?
![[#Errores comunes]]
