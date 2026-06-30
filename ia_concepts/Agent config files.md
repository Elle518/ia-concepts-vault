---
type: concept
tags:
  - agents
  - review
---

## Definición

Los ***agent config files*** son archivos de configuración, normalmente en Markdown, que un agente carga al inicio de una sesión para conocer las reglas del proyecto, convenciones, límites y preferencias de trabajo.

Ejemplos habituales son `AGENTS.md`, `CLAUDE.md` o reglas equivalentes de un IDE agente.

Un agente sin configuración trabaja con hábitos promedio aprendidos durante el entrenamiento. Un *config file* le dice cómo se trabaja en este repo: qué comandos usar, qué no tocar, cómo probar y qué reglas son obligatorias.

## Contenido 

Un buen *config file* contiene instrucciones estables y específicas:

- gestor de paquetes y comandos de test/lint
- límites sobre edición, commits, secretos o red
- estilo de código y convenciones locales
- reglas de seguridad que siempre aplican

## Context rot

Como vive en el contexto de cada sesión, compite por atención con la tarea actual. Debe ser corto, revisado y actualizado cuando cambia el proyecto. Instrucciones genéricas o demasiado largas empeoran el [[Context rot|context rot]].

## Errores comunes

- Convertir el config file en una documentación extensa.
- Incluir consejos genéricos que no cambian el comportamiento.
- No revisarlo al clonar repositorios externos.
- Confiar en él como si sustituyera permisos, sandboxing o tests.

## Preguntas

#flashcards/agents

**¿Qué es un *agent config file*?**
?
![[#Definición]]

**¿Qué debería contener un buen *config file* para agentes?**
?
![[#Contenido]]

**¿Por qué un config file demasiado largo puede perjudicar al agente?**
?
![[#Context rot]]

**¿Qué errores comunes se cometen con los *agents config files*?**
?
![[#Errores comunes]]

