---
type: concept
tags:
  - llms
  - nlp
  - review
---

## Definición

El ***zero-shot prompting*** es una técnica de *[[Prompt engineering|prompt engineering]]* que consiste en pedirle a un [[Modelo del lenguaje|modelo de lenguaje]] que haga una tarea sin darle ejemplos previos de esa tarea en el *prompt*.

La idea es evaluar o aprovechar la capacidad general del modelo para seguir instrucciones y generalizar a partir de su preentrenamiento.

Es como pedirle a alguien que resuelva un problema nuevo solo con la descripción, sin mostrarle casos de ejemplo. Si el modelo entiende bien la tarea, puede responder correctamente aunque no haya visto ejemplos en el *prompt*.

Un ejemplo sería: “Clasifica el sentimiento del siguiente texto como positivo o negativo: ‘Me encantó la película’”.  No se le da ningún ejemplo pero aún así el modelo responde correctamente.

## Elementos del prompt

En *zero-shot*, el *prompt* suele contener:

- la instrucción de la tarea
- contexto mínimo
- formato de salida esperado

## Utilidad

Este enfoque es útil cuando:

- queremos probar la capacidad general del modelo
- la tarea es fácil
- no tenemos ejemplos disponibles
- buscamos una solución rápida y barata de mantener

Suele rendir peor que *[[Few-shot prompting|few-shot]]* en tareas ambiguas, muy específicas o con formato estricto.

## Errores comunes

Algunos errores comunes que se cometen en *zero-shot prompting* son:

- Asumir que *zero-shot* significa “sin conocimiento previo”.
- Usarlo en tareas donde unos pocos ejemplos mejorarían mucho la precisión.
- No fijar el formato de salida y luego culpar al modelo por respuestas inconsistentes.

## Preguntas

#flashcards/llms #flashcards/nlp

**¿Qué es *zero-shot prompting*?**
?
![[#Definición]]

**¿Cuándo tiene sentido usar *zero-shot prompting*?**
?
![[#Utilidad]]

**¿Qué elementos suele incluir un *prompt* en *zero-shot prompting*?**
?
![[#Elementos del prompt]]

**¿Qué errores se suelen cometer en *zero-shot prompting*?**
?
![[#Errores comunes]]
