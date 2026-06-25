---
type: concept
tags:
  - llms
  - nlp
  - review
---

## Definición

***Top-k sampling*** es una estrategia de [[Parámetros de decoding|decoding]] en la que un [[Modelo del lenguaje|modelo de lenguaje]] solo puede elegir el siguiente token entre los $k$ tokens más probables.

El resto de tokens se descartan antes de hacer el muestreo. Así se reduce la probabilidad de generar continuaciones muy improbables sin hacer la salida completamente determinista.

## Utilidad

La idea es limitar el espacio de elección del modelo.

Si $k$ es pequeño, el modelo tiene pocas opciones y la generación suele ser más estable. Si $k$ es grande, el modelo puede explorar más alternativas, pero también aumenta el riesgo de elegir tokens menos adecuados.

Por ejemplo, con $k = 5$, el modelo solo muestrea entre los 5 tokens más probables en cada paso, aunque el vocabulario completo tenga decenas de miles de tokens.

## Explicación técnica

En cada paso de generación, el modelo produce una distribución de probabilidad sobre todo su vocabulario. Con *top-k sampling*:

1. se ordenan los tokens por probabilidad,
2. se conservan solo los $k$ tokens más probables,
3. se reasignan las probabilidades dentro de ese subconjunto,
4. se muestrea el siguiente token a partir de esa nueva distribución.

Esto se suele combinar con [[Temperatura|temperatura]]. La temperatura modifica la forma de la distribución, mientras que *top-k* limita cuántos tokens pueden participar en el muestreo.

## Comparación con top-p

En *top-k*, el número de candidatos es fijo. Siempre se consideran $k$ tokens, aunque la distribución esté muy concentrada o muy dispersa.

En [[Top-p sampling|top-p sampling]], el número de candidatos cambia dinámicamente: se conservan tantos tokens como sean necesarios para acumular una probabilidad total $p$.

Por eso, *top-p* suele adaptarse mejor a contextos donde algunas predicciones son muy obvias y otras son más abiertas.

## Errores comunes

- Pensar que un $k$ más alto siempre mejora la calidad. En realidad, aumenta la diversidad, no necesariamente la corrección.
- Usar un $k$ muy bajo en tareas creativas, haciendo que la salida sea repetitiva o demasiado predecible.
- Usar un $k$ muy alto en tareas factuales, permitiendo tokens poco probables que pueden degradar la respuesta.
- Confundir *top-k* con [[Greedy decoding|greedy decoding]]. *Top-k* sigue muestreando y *greedy decoding* elige siempre el token más probable.

## Preguntas

#flashcards/llms #flashcards/nlp

**¿Qué es *top-k sampling*?**
?
![[#Definición]]

**¿Cuál es la utilidad de *top-k sampling*?**
?
![[#Utilidad]]

**¿Cómo se calcula el *top-k sampling*?**
?
![[#Explicación técnica]]

**¿En qué se diferencia *top-k* de *top-p sampling*?**
?
![[#Comparación con top-p]]

**¿Qué errores comunes hay al usar *top-k sampling*?**
?
![[#Errores comunes]]
