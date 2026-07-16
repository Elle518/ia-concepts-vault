---
type: concept
tags:
  - llms
  - metrics
  - review
---

## Definición

La **evaluación con rúbrica** usa criterios explícitos para juzgar una respuesta de un LLM.

La rúbrica puede ser aplicada por humanos o por un [[AI as a judge|LLM judge]].

En evaluación automática, se usa para hacer más consistente la [[Evaluación subjetiva en LLMs|evaluación subjetiva]].

En vez de pedir “evalúa si esta respuesta es buena”, se definen criterios concretos. Por ejemplo:

- factualidad
- completitud
- claridad
- seguridad
- adherencia al formato
- utilidad para el usuario

Esto reduce la ambigüedad y facilita comparar resultados.

## Diseño de una buena rúbrica

Una buena rúbrica debe:

- definir cada criterio con claridad
- separar dimensiones que no sean equivalentes
- especificar la escala de puntuación
- incluir ejemplos de respuestas buenas, medias y malas
- indicar qué hacer ante errores críticos, como alucinaciones o incumplimiento de formato

## Limitaciones

Una rúbrica no elimina por completo la subjetividad. Si los criterios son vagos, el juez seguirá interpretándolos de forma variable.

También puede haber conflictos entre dimensiones: una respuesta puede ser útil pero incompleta, o clara pero factualmente incorrecta.

## Preguntas

#flashcards/llms #flashcards/metrics 

**¿Qué es la evaluación con rúbrica?**
?
![[#Definición]]

**¿Cómo se diseña una buena rúbrica de evaluación?**
?
![[#Diseño de una buena rúbrica]]

**¿Qué limitaciones tiene la evaluación con rúbrica?**
?
![[#Limitaciones]]
