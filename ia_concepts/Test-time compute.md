---
type: concept
tags:
  - llms
  - review
---

## Definición

***Test-time compute*** es el cómputo adicional que se asigna durante la inferencia para mejorar la calidad de la respuesta de un modelo.

En LLMs, suele consistir en generar varias respuestas, rutas de razonamiento o candidatos para una misma entrada y después seleccionar, agregar o verificar el mejor resultado.

La intuición es que no siempre conviene gastar todo el presupuesto en entrenar un modelo más grande. A veces puedes mejorar una respuesta concreta dejando que el modelo explore más opciones en el momento de responder.

Se denomina *test-time compute* porque la cantidad de resultados que se puede muestrear está determinada por la cantidad de cálculo que se puede asignar a cada llamada de inferencia.

Un modelo se considera robusto si no cambia drásticamente sus resultados con pequeñas variaciones en los datos de entrada. Cuanto menos robusto sea un modelo, más se puede beneficiar del muestreo de múltiples resultados.

## Funcionamiento

El patrón básico es:

1. generar varios candidatos para el mismo input
2. aumentar la diversidad usando distintos parámetros de [[Parámetros de decoding|decoding]], distintos prompts o estrategias de búsqueda
3. evaluar los candidatos con algún criterio
4. devolver el mejor candidato, una agregación de varios o el primer candidato válido

Una versión simple es *[[Best-of-N|best-of-N]]*, donde se generan $N$ salidas y se elige una, la que se considere que funciona mejor. Otra versión más estructurada puede usar una búsqueda, como *[[Beam search|beam search]]*, donde en lugar de generar todos los resultados de forma independiente, lo que podría incluir muchos candidatos menos prometedores, se genera un número fijo de los candidatos más prometedores (*beam*) en cada paso de la secuencia de generación. También se usan técnicas de razonamiento que exploran alternativas, como [[Tree of thoughts prompting|Tree of Thoughts]].

Una estrategia simple para aumentar la efectividad del *time-test compute* es aumentar la diversidad de los resultados, porque es más probable que un conjunto más diverso de opciones produzca mejores candidatos. Si se utiliza el mismo modelo para generar diferentes opciones, suele ser una buena práctica variar las variables de muestreo del modelo para diversificar sus resultados.

## Selección de candidatos

Hay varias formas de decidir qué salida usar:

- **Probabilidad o [[Logprobs|logprobs]]**.  
  - Si se trabaja con probabilidades, la probabilidad de una salida es el producto de las probabilidades de todos los tokens en la salida.
  - Si se trabaja con *logprob*, dado que el logaritmo de un producto es igual a una suma de logaritmos, el *logprob* de una secuencia de tokens es la suma del *logprob* de todos los tokens en la secuencia.
  - Con la suma, es probable que las secuencias más largas tengan un *logprob* total más bajo (los valores de *logprob* suelen ser negativos, porque el log de valores entre 0 y 1 es negativo). Para evitar sesgarse hacia secuencias cortas, podemos utilizar el logprob promedio dividiendo la suma de una secuencia por su longitud.
  - Después de muestrear múltiples resultados, elegimos el que tiene el promedio *logprob* por token más alto. Podemos establecer el parámetro `best_of` en un valor específico, digamos 10, para solicitar al modelo que devuelvan la salida con el *logprob* promedio más alto de 10 salidas diferentes.
- **Voto mayoritario**. Elegir la respuesta final más frecuente, como en [[Self-consistency prompting|self-consistency prompting]].
- **Verifier o reward model**. Puntuar cada candidato con otro modelo entrenado para detectar respuestas mejores.
- **Heurísticas de aplicación**. Por ejemplo, elegir la consulta SQL válida, la respuesta más corta si se busca concisión o el primer resultado que pase validaciones.
- **Elección humana**. Mostrar varias alternativas y dejar que el usuario elija.

El criterio depende de la tarea. En matemáticas o preguntas de opción múltiple suele tener sentido agregar respuestas finales. En generación abierta, puede ser más útil un *reward model*, una rúbrica o evaluación humana.

## Trade-offs

*Test-time compute* puede mejorar rendimiento sin cambiar los pesos del modelo, pero aumenta el coste y la [[Latencia|latencia]]. Generar dos respuestas suele costar aproximadamente el doble que generar una, salvo que se pueda reutilizar parte del procesamiento del *prompt* con técnicas como *[[Prompt caching|prompt caching]]*.

También hay un límite práctico. Muestrear más candidatos aumenta la probabilidad de encontrar una buena respuesta, pero también puede encontrar candidatos que engañen al verificador, añadir ruido o hacer que el coste sea inviable en producción.

Una variante útil para reducir latencia percibida es generar varios candidatos en paralelo y devolver el primero que sea válido. Esto no reduce necesariamente el coste, pero puede mejorar la experiencia si algunas generaciones tardan demasiado.

## Cuándo usarlo

Es especialmente útil cuando:

- la tarea tiene alto valor por respuesta
- el error es caro
- hay una respuesta verificable
- el modelo es poco robusto ante pequeñas variaciones
- se puede validar automáticamente la salida
- el coste adicional compensa frente a usar un modelo mayor

Suele ser menos atractivo para tareas simples, respuestas de bajo valor, sistemas con presupuestos estrictos de latencia o casos donde no existe un buen criterio para comparar candidatos.

## Relación con otros conceptos

[[Self-consistency prompting]] es una forma concreta de *test-time compute*: genera varias soluciones y agrega la respuesta final.

[[Tree of thoughts prompting]] también aumenta el cómputo en inferencia, pero lo usa para explorar y evaluar caminos de razonamiento, no solo para muestrear respuestas independientes.

[[Chain of thought prompting]] puede combinarse con *test-time compute*, porque generar varias cadenas de razonamiento permite comparar rutas alternativas. Aun así, más razonamiento visible no garantiza una respuesta correcta.

## Errores comunes

- Pensar que *test-time compute* es gratis porque no requiere reentrenar el modelo.
- Generar muchos candidatos sin un buen método para elegir entre ellos.
- Confundir mayor probabilidad con mayor corrección factual.
- Usarlo en tareas abiertas donde la agregación por voto no tiene sentido.
- Ignorar la latencia y el coste en producción.
- Escalar el número de muestras sin medir si la mejora marginal compensa.

## Preguntas

#flashcards/llms 

**¿Qué es *test-time compute* en LLMs?**
?
![[#Definición]]

**¿Cuál es el patrón básico de *test-time compute*?**
?
![[#Funcionamiento]]

**¿Qué métodos se pueden usar para elegir el mejor candidato en *test-time compute*?**
?
![[#Selección de candidatos]]

**¿Cuál es el principal trade-off de usar *test-time compute* en producción?**
?
![[#Trade-offs]]

**¿Cuándo suele ser útil aplicar *test-time compute*?**
?
![[#Cuándo usarlo]]

**¿Cómo se relaciona *self-consistency prompting* con *test-time compute*?**
?
![[#Relación con otros conceptos]]

**¿Qué errores comunes hay al usar *test-time compute*?**
?
![[#Errores comunes]]
