---
type: concept
tags:
  - agents
  - review
---

## Definición

El **bucle de un agente** o *agent loop* es el ciclo repetido en el que un [[Agente de IA|agente]] observa el estado actual, decide una acción, ejecuta una herramienta si es necesario y usa el resultado como nueva observación.

Es la forma operativa de técnicas como [[ReAct prompting]]: razonar, actuar, observar y volver a decidir hasta cumplir una condición de parada.

Un agente no intenta adivinar toda la solución al principio. Da un paso, mira qué ocurrió y decide el siguiente. Es parecido a depurar: ejecutas un test, lees el error, cambias algo y vuelves a probar.

## Elementos del bucle

Un bucle típico incluye:

- **Decisión**: el modelo interpreta el contexto y decide la próxima acción
- **Acción**: emite una llamada a una herramienta si es necesario
- **Ejecución**: el [[Harness de agente|harness]] valida y ejecuta la llamada
- **Observación**: el resultado vuelve al contexto
- **Parada**: una regla, evaluador o usuario decide si la tarea terminó

## Tipos de bucles

El *loop* puede ser **síncrono**, cuando cada acción bloquea el bucle hasta terminar (*blocking execution*), o **asíncrono**, cuando lanza trabajos en segundo plano (*non-blocking execution*). También puede permitir llamadas paralelas (*parallel tool calls*), útiles para lecturas independientes pero arriesgadas si varias acciones escriben sobre los mismos recursos.

## Errores comunes

- No definir una condición de parada clara.
- Permitir *loops* largos sin límites de coste, tiempo o pasos.
- Confundir recuperación de errores con ausencia de errores.
- Ejecutar acciones paralelas que compiten por los mismos archivos o estados.

## Preguntas

#flashcards/agents

**¿Qué es el *agent loop*?**
?
![[#Definición]]

**¿Qué pasos componen un loop de agente típico?**
?
![[#Elementos del bucle]]

**¿Qué tipos de *agent loop* existen?**
?
![[#Tipos de bucles]]

**¿Qué riesgos aparecen si no se controla el *agent loop*?**
?
![[#Errores comunes]]
