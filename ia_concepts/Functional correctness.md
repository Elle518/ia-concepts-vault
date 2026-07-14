---
type: concept
tags:
  - llms
  - metrics
  - review
---

## Definición

***Functional correctness*** evalúa si la salida de un sistema cumple la funcionalidad esperada. También se denomina **corrección funcional**.

En vez de medir si la respuesta se parece a una referencia, comprueba si funciona. Es una forma de [[Evaluación exacta en LLMs|evaluación exacta]] cuando el comportamiento esperado puede verificarse automáticamente.

La corrección funcional es la métrica definitiva para evaluar el rendimiento de cualquier aplicación, ya que mide si esta cumple con su propósito. Sin embargo, medir la corrección funcional no siempre es sencillo, y su medición no se puede automatizar fácilmente.

Si pedimos a un modelo que escriba una función `gcd(a, b)`, no basta con que el código parezca correcto. La evaluación consiste en ejecutar el código con casos de prueba y comprobar si devuelve los resultados esperados.

La misma idea aplica a SQL, agentes, bots de juego, planificación o cualquier tarea con un objetivo medible.

## Ejemplos

La generación de código es un ejemplo de una tarea en la que se puede automatizar la medición de la corrección funcional. La corrección funcional en programación a veces se denomina ***execution accuracy***.

En generación de código, se ejecutan *[[Test unitarios|unit tests]]* sobre el código generado.

En text-to-SQL, se puede ejecutar la query generada y comparar el resultado con el esperado.

En un bot de juego, se puede medir el score conseguido.

En una tarea de optimización, se puede medir si el sistema reduce coste, tiempo o energía.

## pass@k

En *[[Benchmark|benchmarks]]* de código, como HumanEval o MBPP, es común usar `pass@k`.

Un problema de referencia viene con un conjunto de casos de prueba. Cada caso de prueba consta de un escenario que el código debe ejecutar y el resultado esperado para ese escenario.

Para cada problema se generan `k` soluciones. El problema se considera resuelto si al menos una de esas soluciones pasa todos los tests.

Si un modelo resuelve 5 de 10 problemas generando 3 soluciones por problema, su `pass@3` es 50%.

En general, `pass@1` suele ser menor que `pass@3`, y `pass@3` menor que `pass@10`, porque generar más intentos aumenta la probabilidad de acierto, es decir, de éxito a la hora de completar la tarea.

## Limitaciones

- Requiere definir tests o criterios verificables.
- Los tests pueden ser incompletos y aceptar soluciones incorrectas.
- Puede ser más fácil evaluar el resultado final que evaluar una parte intermedia del proceso. Imaginemos que queremos evaluar la capacidad de alguien para jugar al ajedrez. Es más fácil evaluar el resultado final del juego (ganar/perder/tablas) que evaluar solo un movimiento.
- No aplica bien a tareas abiertas sin objetivo medible claro.

## Preguntas

#flashcards/llms #flashcards/metrics 

**¿Qué mide *functional correctness*?**
?
![[#Definición]]

**¿Qué tipos de tareas se pueden evaluar usando *functional correctness*?**
?
![[#Ejemplos]]

**¿Qué es `pass@k`?**
?
![[#pass@k]]

**¿Qué limitaciones tiene *functional correctness*?**
?
![[#Limitaciones]]
