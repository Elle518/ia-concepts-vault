---
type: concept
tags:
  - llms
  - metrics
  - review
---

## Definición

La **evaluación subjetiva en LLMs** mide respuestas cuya calidad depende de un juicio evaluativo, no solo de una regla exacta.

Es común en tareas abiertas como resumen, escritura, asistencia conversacional, razonamiento largo o análisis de documentos.

En evaluación automática, la forma más habitual es usar *[[AI as a judge]]*.

## Subtipos

Dentro del  *AI as a judge*, los subtipos más comunes son:

- [[Evaluación pointwise con LLM judge]]
- [[Evaluación pairwise con LLM judge]]
- [[Evaluación con rúbrica]]

También puede existir evaluación humana subjetiva, pero no es automática.

## Riesgos

El resultado puede cambiar según:

- el modelo juez
- el prompt del juez
- la rúbrica
- el orden de las respuestas
- la [[Temperatura|temperatura]] y otros [[Parámetros de decoding|parámetros de decoding]]
- la claridad del criterio de evaluación

Por eso conviene calibrarla con ejemplos, medir consistencia y combinarla con evaluaciones exactas cuando sea posible.

## Preguntas

#flashcards/llms #flashcards/metrics

**¿Qué es la evaluación subjetiva en LLMs?**
?
![[#Definición]]

**¿Qué subtipos incluye la evaluación subjetiva automática?**
?
![[#Subtipos]]

**¿Qué riesgos tiene la evaluación subjetiva en LLMs?**
?
![[#Riesgos]]
