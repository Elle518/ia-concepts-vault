---
type: concept
tags:
  - ml
  - llms
  - review
---

## Definición

Un ***benchmark*** es un conjunto de tareas, datos y métricas usado para comparar modelos o sistemas bajo condiciones controladas.

Sirve para estimar su rendimiento relativo, detectar regresiones y comunicar resultados de forma comparable.

La intuición es el de un examen común, donde si varios modelos responden las mismas preguntas con la misma métrica, podemos compararlos con más rigor.

## Componentes

Un *benchmark* suele definir:

- un dataset o conjunto de prompts
- un protocolo de evaluación
- una métrica principal
- particiones de datos
- condiciones de ejecución
- la forma de reportar resultados

En LLMs, también importa fijar los [[Parámetros de decoding|parámetros de decoding]], la versión del modelo y el criterio de evaluación.

## Limitaciones

Un *benchmark* mide lo que está diseñado para medir, no la calidad completa del sistema.

Puede saturarse, filtrarse en datos de entrenamiento, no representar casos reales o favorecer modelos optimizados específicamente para ese test.

Por eso conviene combinar *benchmarks* públicos con evaluaciones internas del caso de uso.

Los *benchmarks* de evaluación disponibles públicamente han demostrado ser inadecuados para evaluar los [[Modelo del lenguaje|modelos fundacionales]]. Idealmente, estos *benchmarks* deberían abarcar toda la gama de capacidades de los modelos y, a medida que la IA avanza, deben evolucionar para ponerse al día.

Un *benchmark* se satura para un modelo una vez que este alcanza la puntuación perfecta. En el caso de los modelos fundacionales, los *benchmarks* se están saturando rápidamente:

- GLUE (*General Language Understanding Evaluation*) se publicó en 2018 y se saturó en tan solo un año, lo que hizo necesaria la introducción de SuperGLUE en 2019.
- NaturalInstructions (2021) fue reemplazado por SuperNaturalInstructions (2022).
- MMLU (2020) fue reemplazado en gran medida por MMLU-Pro (2024).

## Errores comunes

- Confundir una buena puntuación en un *benchmark* con un buen rendimiento en producción.
- Comparar resultados sin las mismas condiciones de evaluación.
- Ignorar contaminación de datos.
- Optimizar para el *benchmark* y olvidar la tarea real.
- No mirar ejemplos de error, solo la métrica agregada.

## Preguntas

#flashcards/ml #flashcards/llms 

**¿Qué es un *benchmark*?**
?
![[#Definición]]

**¿Qué componentes suele tener un *benchmark*?**
?
![[#Componentes]]

**¿Qué limitaciones tienen los *benchmarks*?**
?
![[#Limitaciones]]

**¿Qué errores comunes hay al interpretar *benchmarks*?**
?
![[#Errores comunes]]
