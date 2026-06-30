---
type: concept
tags:
  - agents
  - review
---

## Definición

El ***runtime* de un agente** es el entorno de ejecución donde vive el [[Agente de IA|agente]] mientras realiza una tarea.

Proporciona recursos como ejecución de código, acceso a herramientas, estado, colas, concurrencia, límites de tiempo, aislamiento y mecanismos de observabilidad.

Si el *[[Harness de agente|harness]]* es la lógica que decide cómo operar el agente, el *runtime* es el taller donde esa lógica se ejecuta. Define qué puede correr, con qué permisos, durante cuánto tiempo y con qué recursos.

## Explicación técnica

Un *runtime* puede ser tan simple como un proceso local que llama al modelo y ejecuta herramientas, o tan complejo como una plataforma distribuida con workers, colas, sandboxes y almacenamiento persistente.

Responsabilidades habituales:

- ejecutar el *[[Bucle de un agente|agent loop]]*
- gestionar sesiones, estado y checkpoints
- limitar CPU, memoria, tiempo, red y filesystem
- coordinar llamadas síncronas, asíncronas o paralelas
- aislar ejecuciones con *[[Sandboxing de agentes|sandboxing]]*
- inyectar credenciales efímeras o permisos acotados
- emitir trazas, logs y métricas para [[Observabilidad de agentes|observabilidad]]

## Runtime vs LLM

Debemos distinguir el *runtime* del modelo, cambiar el LLM no resuelve problemas de ejecución, permisos, aislamiento o recuperación ante fallos.

## Errores comunes

- Diseñar el agente como si siempre corriera en un notebook o script local.
- No limitar tiempo, coste o número de pasos.
- Compartir estado mutable entre agentes sin aislamiento.
- Dar credenciales permanentes al entorno de ejecución.

## Preguntas

#flashcards/agents

**¿Qué es el *runtime* de un agente?**
?
![[#Definición]]

**¿Qué responsabilidades tiene un runtime de agentes?**
?
![[#Explicación técnica]]

**¿Por qué runtime y modelo no son lo mismo?**
?
![[#Runtime vs LLM]]

**¿Qué errores comunes aparecen al diseñar un *runtime* de agentes?**
?
![[#Errores comunes]]
