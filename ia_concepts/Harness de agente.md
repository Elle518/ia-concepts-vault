---
type: concept
tags:
  - agents
  - review
---

## Definición

El ***harness* de un [[Agente de IA|agente]]** es la capa de aplicación que envuelve al [[Modelo del lenguaje|LLM]] y convierte sus decisiones en acciones controladas.

Se encarga de construir el contexto, exponer herramientas, interpretar llamadas del modelo, validar acciones, ejecutar pasos del [[Bucle de un agente|agent loop]] y devolver observaciones al modelo.

Es el “pegamento” entre el modelo y el mundo externo.

El modelo decide qué quiere hacer, pero no debería tocar el sistema directamente. El *harness* traduce esa intención a una llamada concreta, comprueba si está permitida, la ejecuta y empaqueta el resultado para el siguiente turno.

Sin *harness*, un agente sería solo texto sugiriendo acciones.

## Responsabilidades del harness

Un *harness* suele implementar:

- ensamblado del *system prompt*, memoria y contexto relevante
- definición de herramientas y schemas
- parsing de tool calls o [[Structured output prompting|salidas estructuradas]]
- validación de argumentos
- aplicación de [[Permisos en agentes|permisos]] y [[Hooks en agentes|hooks]]
- ejecución de herramientas mediante APIs, CLI o [[Model Context Protocol|MCP]]
- manejo de errores, retries y límites
- logging para [[Observabilidad de agentes|observabilidad]]

## Harness vs runtime

La diferencia con el [[Runtime de agente|runtime]] es que el *harness* describe la lógica de control del agente, mientras que el runtime es el entorno que lo ejecuta y le da recursos.

## Errores comunes

- Dejar que el modelo genere comandos libres sin validación.
- Mezclar lógica de negocio, permisos y prompts sin separación clara.
- No registrar tool calls ni errores.
- Pensar que el *harness* sustituye al *[[Sandboxing de agentes|sandboxing]]* o a los tests.

## Preguntas

#flashcards/agents

**¿Qué es el *harness* de un agente?**
?
![[#Definición]]

**¿Qué responsabilidades suele tener un *agent harness*?**
?
![[#Responsabilidades del harness]]

**¿En qué se diferencia el *harness* del *runtime* de un agente?**
?
![[#Harness vs runtime]]

**¿Qué errores comunes aparecen al diseñar el *harness* de un agente?**
?
![[#Errores comunes]]

