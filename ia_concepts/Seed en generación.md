---
type: concept
tags:
  - llms
  - nlp
  - review
---

## Definición

La ***seed* en generación** es un valor usado para inicializar el generador de números pseudoaleatorios que participa en el *[[Sampling|sampling]]* de una salida.

Si el sistema permite fijarla, la misma *seed* con el mismo *prompt*, modelo y parámetros puede ayudar a obtener resultados más reproducibles.

La intuición es fijar el punto de partida de la aleatoriedad. No elimina la distribución probabilística del modelo, pero hace que el muestreo siga el mismo camino cuando todo lo demás permanece igual.

## Uso en LLMs

En generación con LLMs, la *seed* puede usarse junto con:

- [[Temperatura|temperatura]]
- [[Top-p sampling|top-p]] y [[Top-p sampling|top-k]]
- límites de longitud
- versión fija del modelo
- prompt y contexto idénticos

Esto es útil para *[[Debugging|debugging]]*, evaluación, demos reproducibles y análisis de regresiones.

## Limitaciones

Una *seed* fija no garantiza reproducibilidad perfecta en todos los proveedores o entornos.

La salida puede cambiar si cambia el modelo, el tokenizer, la infraestructura, el paralelismo, el *hardware*, el orden de operaciones numéricas o cualquier parámetro de *[[Parámetros de decoding|decoding]]*.

Además, una respuesta reproducible no es necesariamente correcta. Solo significa que el sistema tiende a repetirla bajo las mismas condiciones.

## Errores comunes

- Pensar que fijar la *seed* vuelve determinista todo el sistema.
- Cambiar el *prompt* o el modelo y esperar la misma salida.
- No registrar el resto de parámetros de generación.
- Confundir reproducibilidad con calidad.
- Depender de una *seed* para producción en vez de diseñar validación y evaluación.

## Preguntas

#flashcards/llms #flashcards/nlp 

**¿Qué es la *seed* en generación con LLMs?**
?
![[#Definición]]

**¿Para qué sirve fijar una *seed* en generación?**
?
![[#Uso en LLMs]]

**¿Qué limitaciones tiene fijar la *seed*?**
?
![[#Limitaciones]]

**¿Qué errores comunes hay al usar *seed* en generación?**
?
![[#Errores comunes]]
