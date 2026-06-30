---
type: concept
tags:
  - agents
  - review
---

## Definición

Un **agente de IA** es un sistema basado en un [[Modelo del lenguaje|LLM]] que ejecuta un [[Bucle de un agente|bucle de decisión]], puede usar herramientas y decide el siguiente paso a partir de las observaciones anteriores.

No es solo un *prompt* largo, el agente convierte una petición en una secuencia de acciones, como leer archivos, consultar documentación, llamar APIs, ejecutar código o pedir más contexto.

Un chatbot responde; un agente trabaja. Si se le pide “resume este texto”, quizá basta una llamada al modelo. Si se le pide “depura este fallo”, necesita inspeccionar archivos, ejecutar tests, observar errores y ajustar el plan.

La clave es que el camino no está totalmente definido de antemano.

## Elementos de un agente

Un agente suele tener:

- un modelo que decide
- un [[Harness de agente|harness]] o [[Runtime de agente|runtime]] que ejecuta llamadas a herramientas
- un conjunto de herramientas (*tools*) disponibles
- un estado en la ventana de contexto o fuera de ella
- criterios de parada
- [[Guardarraíles|guardarraíles]] para limitar acciones peligrosas

## Utilidad

Conviene usar agentes cuando la tarea es abierta, el siguiente paso depende del resultado del anterior y no es fácil escribir un *script* determinista. Si la tarea es cerrada y repetible, un *prompt* simple, una función o un pipeline clásico suele ser mejor.

## Errores comunes

- Llamar agente a cualquier wrapper sobre un LLM.
- Usar un agente para tareas que deberían ser scripts deterministas.
- Darle demasiadas herramientas sin permisos ni observabilidad.
- Medir solo si “parece haber terminado” en vez de validar artefactos externos.

## Preguntas

#flashcards/agents

**¿Qué es un agente de IA?**
?
![[#Definición]]

**¿Cuándo merece la pena usar un agente?**
?
![[#Utilidad]]

**¿Qué componentes suele tener un agente de IA?**
?
![[#Elementos de un agente]]

**¿Qué errores comunes aparecen al diseñar agentes?**
?
![[#Errores comunes]]
