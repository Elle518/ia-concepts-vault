---
type: concept
tags:
  - agents
  - review
---

## Definición

Los **patrones multiagente** son formas recurrentes de coordinar varios [[Agente de IA|agentes]] especializados para resolver una tarea que sería demasiado larga, amplia o heterogénea para un único agente.

Los patrones más comunes son *planner/executor*, *router/specialist* y *map-reduce*.

Es como organizar un equipo pequeño: alguien planifica, alguien ejecuta, especialistas revisan partes concretas y una persona integra el resultado. La dificultad no es solo repartir trabajo, sino hacer buenos traspasos.

## Patrones habituales

Patrones habituales:

- **Planner/executor**: un agente genera el plan y otro lo ejecuta con herramientas.
- **Router/specialist**: un router decide qué especialista debe resolver cada petición.
- **Map-reduce**: varios agentes procesan partes independientes y un agregador fusiona resultados.

## Beneficios vs coste

El beneficio principal es reducir contexto y especializar comportamiento. Cada agente puede tener un *prompt*, herramientas y modelo más acotados. El coste está en la coordinación: [[Agent handoff|handoffs]] ambiguos, resúmenes incompletos, duplicación de trabajo y conflictos de escritura.

## Errores comunes

- Añadir agentes cuando bastaba dividir mejor el prompt.
- No definir qué información debe pasar en cada handoff.
- Usar especialistas sin criterios claros de routing.
- Confiar demasiado en el agregador de resultados.

## Preguntas

#flashcards/agents

**¿Qué son los patrones multiagente?**
?
![[#Definición]]

**¿Qué diferencia hay entre *planner/executor*, *router/specialist* y *map-reduce*?**
?
![[#Patrones habituales]]

**¿Cuáles son los principales beneficios y costes de los patrones multiagente**
?
![[#Beneficios vs coste]]

**¿Cuáles son los principales errores en patrones multiagente?**
?
![[#Errores comunes]]

