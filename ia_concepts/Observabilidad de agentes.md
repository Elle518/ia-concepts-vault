---
type: concept
tags:
  - agents
  - review
---

## Definición

La **observabilidad de agentes** es la capacidad de entender qué hizo un agente, por qué falló, cuánto costó y si produjo un resultado correcto.

Incluye *logging*, *tracing*, *replay/debugging* y métricas.

Un agente puede ejecutar muchos pasos antes de dar una respuesta. Sin observabilidad, solo ves el resultado final; con observabilidad puedes reconstruir la ruta: prompts, herramientas, errores, tiempos, costes y decisiones.

## Capas de observabilidad

Capas principales:

- ***Logging***: registro append-only de prompts, respuestas, tool calls, errores, latencia, tokens, modelo y session ID.
- ***Tracing***: estructura navegable del run, normalmente como árbol de llamadas y subagentes.
- ***Replay***: rerun de una sesión con respuestas grabadas o llamadas frescas para depurar regresiones.
- **Métricas**: latencia, coste, tokens, número de tool calls, fallos y señales de resultado.

Las métricas proxy ayudan a detectar loops, costes anómalos o herramientas rotas. Para medir éxito real hace falta anclarlo a artefactos externos: tests en CI, PR mergeada, deploy estable, evaluación humana o datos de negocio.

## Errores comunes

- Registrar solo la respuesta final.
- No guardar versión de modelo, prompt o herramientas.
- Medir "task complete" como si fuera éxito real.
- No poder reproducir un fallo porque faltan inputs o tool outputs.

## Preguntas

#flashcards/agents 

**¿Qué es la observabilidad de agentes?**
?
![[#Definición]]

**¿Qué diferencia hay entre logging, tracing, replay y métricas en la observabilidad de agentes?**
?
![[#Capas de observabilidad]]

**¿Qué errores comunes dificultan depurar agentes?**
?
![[#Errores comunes]]
