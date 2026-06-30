---
type: concept
tags:
  - agents
  - review
---

## Definición

Los ***workflow files reutilizables*** son instrucciones de procedimientos que un agente carga bajo demanda para una tarea concreta, como revisar código, depurar, escribir tests o generar documentación.

Suelen implementarse como [[Agent skills|skills]], [[Agent hooks|hooks]], [[Agent rules|reglas]] o [[Agent commands|comandos]] con metadatos que indican cuándo deben usarse.

El [[Agent config files|config file]] dice al agente “cómo trabajamos siempre”, un *workflow* reutilizable dice “cómo se hace cierta clase de tarea”.

## Elementos

Un workflow reutilizable suele tener:

- nombre y descripción como señal de routing (metadatos)
- reglas de activación por tipo de tarea o ruta
- pasos concretos que el agente debe seguir
- criterios de finalización o verificación

Son útiles porque reducen variabilidad y permiten capturar buenas prácticas. Funcionan mejor cuando son curados por humanos y específicos del dominio.

## Errores comunes

- Hacer *workflows* tan vagos que no cambian el comportamiento.
- Cargar demasiados *workflows* para una sola tarea.
- No incluir criterios de verificación.
- Confundirlos con memoria o documentación del proyecto.

## Preguntas

#flashcards/agents 

**¿Qué son los *workflow files* reutilizables para agentes?**
?
![[#Definición]]

**¿Qué elementos suele tener un *workflow files* reutilizables para agentes?**
?
![[#Elementos]]

**¿Qué hace que un *workflow file* reutilizable sea poco útil?**
?
![[#Errores comunes]]
