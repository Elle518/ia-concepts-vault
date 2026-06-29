---
type: concept
tags:
  - llms
  - nlp
  - review
---

## Definición

El ***step-back prompting*** es una técnica de [[Prompt engineering|prompt engineering]] que pide al modelo razonar primero sobre el principio general del problema antes de resolver el caso concreto, es decir, que piense primero a un nivel más general antes de resolver el problema en detalle.

Sirve para evitar que el [[Modelo del lenguaje|modelo de lenguaje]] se quede atrapado demasiado pronto en detalles superficiales.

Es como preguntar primero "¿qué tipo de problema es este?" antes de empezar a calcular. Al identificar el marco general, la solución concreta suele ser más ordenada.

## Utilidad

Un prompt de *step-back* suele tener dos fases:

- identificar el principio, patrón o concepto general
- aplicar ese principio al caso específico

Ejemplo:

```text
Primero explica el principio general que aplica a este problema.
Después resuelve el caso concreto usando ese principio.
```

Puede ayudar en problemas complejos, ambiguos o poco familiares, especialmente cuando el modelo necesita abstraer antes de ejecutar.

## Errores comunes

- Añadir una fase de abstracción innecesaria a tareas simples.
- Pedir principios demasiado vagos y obtener respuestas genéricas.
- Confundir una explicación de alto nivel con una verificación real de la respuesta.

## Preguntas

#flashcards/llms #flashcards/nlp

**¿Qué es *step-back prompting*?**
?
![[#Definición]]

**¿Cuál es la utilidad del *step-back prompting*?**
?
![[#Utilidad]]

**¿Qué errores se suelen cometer en el *step-back prompting*?**
?
![[#Errores comunes]]
