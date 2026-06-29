---
type: concept
tags:
  - llms
  - nlp
  - review
---

## Definición

***Automatic Prompt Engineering*** (*APE*) es una técnica de [[Prompt engineering|prompt engineering]] en la que los *prompts* se generan, prueban y optimizan automáticamente en lugar de escribirse solo de forma manual.

El sistema crea varios candidatos de *prompt*, los evalúa sobre ejemplos y selecciona los que producen mejores resultados.

Es como hacer búsqueda de [[Hiperparámetros|hiperparámetros]], pero aplicada al texto del *prompt*. En vez de ajustar a mano una instrucción, se prueban variantes y se comparan con criterios medibles.

## Funcionamiento

Un flujo de APE suele incluir:

- generar candidatos de *prompt*
- ejecutarlos sobre un conjunto de entradas de prueba
- comparar las salidas con métricas o criterios de evaluación
- seleccionar o refinar los prompts con mejor rendimiento

Los criterios pueden incluir exactitud, consistencia, cumplimiento del formato, tasa de alucinaciones, coste o preferencia humana. APE es útil cuando hay muchas tareas similares, un conjunto de evaluación representativo y necesidad de optimizar a escala.

## Errores comunes

- Optimizar *prompts* sobre pocos ejemplos y [[Sobreajuste|sobreajustar]] el *prompt*.
- Elegir el mejor *prompt* por intuición en vez de usar evaluación.
- Ignorar coste, latencia o robustez fuera del conjunto de prueba.
- Pensar que APE sustituye la evaluación humana en tareas ambiguas.

## Preguntas

#flashcards/llms #flashcards/nlp

**¿Qué es *Automatic Prompt Engineering*?**
?
![[#Definición]]

**¿Cómo se elige el mejor prompt en *Automatic Prompt Engineering*?**
?
![[#Funcionamiento]]

**¿Qué riesgo aparece si se optimiza un *prompt* con pocos ejemplos?**
?
![[#Errores comunes]]
