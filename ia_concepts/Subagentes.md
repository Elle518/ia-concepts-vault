---
type: concept
tags:
  - agents
  - review
---

## Definición

Los **subagentes** son [[Agente de IA|agentes]] delegados con un alcance limitado, un *prompt* propio, un conjunto de herramientas restringido y normalmente una [[Ventana de contexto|ventana de contexto]] separada.

El agente principal les encarga una tarea y recibe de vuelta un resultado comprimido, no todo el razonamiento intermedio.

Un subagente es como pedir a alguien que investigue una parte concreta y te devuelva un resumen accionable. El beneficio no es solo paralelizar, sino mantener limpio el contexto principal.

Un subagente se define normalmente con un pequeño archivo Markdown y un encabezado YAML.

## Utilidad

Los subagents son útiles para:

- revisar muchos archivos en paralelo
- hacer búsquedas independientes
- separar roles como seguridad, tests o documentación
- ejecutar tareas con modelos más baratos o herramientas limitadas

Cada subagente debería tener un contrato claro: qué recibe, qué puede tocar, qué debe devolver y qué no debe hacer. Si varios subagentes escriben en el mismo repo, suelen necesitar aislamiento con [[Worktree|worktrees]], ramas separadas o entornos temporales.

## Errores comunes

- Delegar tareas demasiado ambiguas.
- Pasar tanto contexto al subagente que la separación deja de aportar valor.
- Permitir escrituras paralelas sin aislamiento.
- No verificar el resumen devuelto por el subagente.

## Preguntas

#flashcards/agents

**¿Qué es un *subagente*?**
?
![[#Definición]]

**¿Qué ventajas tiene usar subagents?**
?
![[#Utilidad]]

**¿Qué riesgos aparecen con subagentes paralelos?**
?
![[#Errores comunes]]
