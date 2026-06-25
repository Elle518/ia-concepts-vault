---
type: concept
tags:
  - llms
  - nlp
  - review
---

## Definición

Los **parámetros de *decoding*** son los ajustes que controlan cómo un [[Modelo del lenguaje|modelo de lenguaje]] transforma sus probabilidades internas en una salida concreta.

No cambian los pesos del modelo ni añaden conocimiento nuevo. Afectan a la forma de seleccionar tokens durante la generación, influyendo en la diversidad, consistencia, longitud y repetición de la respuesta.

## Utilidad

La intuición es que el modelo no escribe una respuesta directamente: predice distribuciones de probabilidad sobre posibles siguientes tokens.

Los parámetros de *decoding* deciden cómo convertir esas distribuciones en texto. Para una tarea factual puede interesar una generación más estable, mientras que para una tarea creativa puede interesar más variedad.

Por eso, ajustar el *decoding* es una parte importante de construir sistemas con LLMs, junto con el [[Prompt engineering|prompt engineering]], la evaluación y el diseño del contexto.

## Parámetros principales

Los parámetros más comunes son:

- **[[Temperatura]]**. Controla cuánto se aplana o concentra la distribución de probabilidades.
- **[[Top-k sampling]]**. Limita el muestreo a los $k$ tokens más probables.
- **[[Top-p sampling]]**. Limita el muestreo al conjunto mínimo de tokens que acumula una probabilidad $p$.
- **[[Greedy decoding]]**. Elige siempre el token más probable en cada paso.
- **Longitud máxima**. Limita cuántos tokens puede generar el modelo.
- **[[Penalizaciones por repetición]]**. Reducen la probabilidad de repetir tokens, frases o patrones.
- **[[Stop sequences]]**. Indican secuencias donde la generación debe detenerse.

## Explicación técnica

En un modelo autorregresivo, la generación ocurre token a token. En cada paso, el modelo calcula una distribución:

$$P(x_t \mid x_{<t})$$

Los parámetros de *decoding* modifican o restringen esa distribución antes de seleccionar el siguiente token.

Algunos parámetros cambian la forma de la distribución, como la [[Temperatura|temperatura]]. Otros filtran candidatos, como [[Top-k sampling|top-k]] y [[Top-p sampling|top-p]]. Otros afectan a cuándo se detiene la generación o a qué patrones se penalizan.

La elección de estos parámetros suele ser un *trade-off* entre precisión, diversidad, coste, latencia y reproducibilidad.

## Uso práctico

Para tareas de extracción, clasificación, generación de JSON o código, suelen preferirse configuraciones más conservadoras: baja temperatura, límites claros de longitud y formato bien especificado.

Para *brainstorming*, escritura creativa o generación de variantes, puede ser útil permitir más diversidad aumentando la temperatura o con un *sampling* más abierto.

En producción, los parámetros de *decoding* deben evaluarse con ejemplos reales. Un ajuste que funciona en una demo puede fallar cuando cambian el dominio, el *prompt* o la distribución de las entradas.

## Errores comunes

- Intentar resolver la falta de contexto o conocimiento solo cambiando parámetros de *decoding*.
- Subir la temperatura esperando un mejor razonamiento, cuando principalmente aumenta la aleatoriedad.
- Ajustar un parámetro aislado sin considerar su interacción con otros.
- No fijar límites de longitud o secuencias de parada en tareas con un formato esperado.
- Evaluar una configuración con pocos ejemplos y asumir que generaliza.

## Preguntas

#flashcards/llms #flashcards/nlp

**¿Qué son los parámetros de *decoding* en un LLM?**
?
![[#Definición]]

**¿Para qué sirven los parámetros de *decoding* en un LLM?**
?
![[#Utilidad]]

**¿Cuáles son algunos parámetros de *decoding* comunes en un LLM?**
?
![[#Parámetros principales]]

**¿Cómo afectan técnicamente los parámetros de *decoding* a la generación en un LLM?**
?
![[#Explicación técnica]]

**¿Qué configuraciones de parámetros en un LLM suelen convenir para tareas factuales o estructuradas? ¿Y para tareas más creativas?**
?
![[#Uso práctico]]

**¿Qué errores comunes hay al ajustar parámetros de *decoding* en un LLM?**
?
![[#Errores comunes]]

**¿Qué parámetros deberíamos ajustar si un LLM repite palabras o entra en bucle?**
?
Cuando un LLM repite palabras o entra en bucles, normalmente ajustaremos los **parámetros de decodificación**. En concreto:
- **Bajar la temperatura** si el modelo está generando texto demasiado inestable o errático.
- **Ajustar *top-p* o *top-k*** para limitar el espacio de tokens candidatos y evitar elecciones poco probables.
- **Aumentar *frequency penalty*** para penalizar tokens que ya han aparecido muchas veces.
- **Aumentar *presence penalty*** para favorecer que el modelo introduzca información nueva.
- **Usar *repetition penalty*** si el framework lo permite, especialmente en modelos open-source.
- **Añadir un límite de longitud** o condiciones de parada para cortar generaciones degeneradas.
- **Añadir secuencias explícitas de parada**.
- También puede ayudar modificar el prompt para ser más específicos.
