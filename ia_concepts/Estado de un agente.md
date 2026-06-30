---
type: concept
tags:
  - agents
  - review
---

## Definición

El **estado de un agente**  o *agent state* es toda la información que determina qué sabe el [[Agente de IA|agente]] y qué puede hacer en un momento dado.

Incluye lo que está dentro de la [[Ventana de contexto|ventana de contexto]] y lo que vive fuera de ella, como archivos, bases de datos, memoria persistente o sistemas de búsqueda.

El contexto es la mesa de trabajo del agente: solo puede razonar directamente con lo que está encima. El resto del proyecto está en estanterías, puede consultarlo con herramientas, pero primero tiene que traerlo a la mesa.

## Tipos de estado

Hay dos tipos principales de estado:

- **Estado en contexto**: mensajes, *system prompt*, llamadas a herramientas y observaciones visibles para el modelo.
- **Estado externo**: archivos, bases de datos, índices, logs, memoria y documentación que el modelo no ve hasta recuperarla.

La ventana de contexto tiene un límite estricto de tokens y un límite flexible asociado al [[Context rot|context rot]]. Por eso, en agentes reales conviene dejar en contexto solo lo necesario para la siguiente decisión y guardar el progresos o persistir aquello que pueda ser útil en el futuro bases de datos, archivos, logs, etc.

En los [[Sistema multiagente|sistemas multiagente]], el **estado compartido** hace que debamos tener cuidado: dos agentes pueden leer el mismo archivo sin problema, pero dos agentes escribiendo el mismo recurso pueden pisarse.

## Errores comunes

- Meter todo el proyecto en contexto esperando mejores resultados.
- Guardar el progreso solo en la conversación.
- No distinguir entre memoria persistente y contexto visible.
- Permitir que varios agentes escriban el mismo estado sin aislamiento.

## Preguntas

#flashcards/agents

**¿Qué es el estado de un agente?**
?
![[#Definición]]

**¿Qué diferencia hay entre estado en contexto y estado externo?**
?
![[#Tipos de estado]]

**¿Qué errores se comenten en relación al estado de un agente?**
?
![[#Errores comunes]]

