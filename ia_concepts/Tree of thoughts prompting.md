---
type: concept
tags:
  - llms
  - nlp
  - review
---

## Definición

***Tree of Thoughts prompting*** (ToT) es una técnica de *[[Prompt engineering|prompt engineering]]* que extiende *[[Chain of thought prompting|chain-of-thought prompting]]* (CoT) explorando varios caminos de razonamiento en forma de árbol.

En lugar de seguir una única cadena lineal, el modelo genera alternativas, las evalúa y continúa con las ramas más prometedoras.

Es como resolver un problema de planificación dibujando varias opciones en una pizarra. Si una opción lleva a un callejón sin salida, se puede volver atrás y probar otra.

## Utilidad

ToT separa el razonamiento en estados intermedios llamados *thoughts*. Para cada estado, el sistema puede:

- proponer varios siguientes pasos
- evaluar qué ramas parecen más prometedoras
- descartar ramas débiles
- retroceder si una rama no funciona

*[[Chain of thought prompting]]*  sigue una única vía de razonamiento, la cual puede ser errónea. ToT explora múltiples vías, las evalúa y puede retroceder si es necesario. Si una vía conduce a un callejón sin salida, ToT puede cambiar a otra rama.

Esto hace que ToT sea más útil en tareas de planificación, optimización, búsqueda, decisión y problemas donde conviene comparar varias estrategias. Suele ser más costoso que CoT porque requiere generar y evaluar más alternativas.

## Errores comunes

- Usarlo para tareas simples donde una respuesta directa basta.
- Confundir exploración de ramas con garantía de corrección.
- No definir un criterio claro para evaluar cada rama.
- Olvidar que aumenta latencia y coste.

## Preguntas

#flashcards/llms #flashcards/nlp

**¿Qué es *Tree of Thoughts prompting*?**
?
![[#Definición]]

**¿Para qué se usa normalmente el *Tree of Thoughts prompting*?**
?
![[#Utilidad]]

**¿Qué errores comunes se suelen cometer en *Tree of Thoughts prompting*?**
?
![[#Errores comunes]]
