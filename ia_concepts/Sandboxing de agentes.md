---
type: concept
tags:
  - agents
  - review
---

## Definición

El ***sandboxing* de [[Agente de IA|agentes]]** consiste en aislar qué archivos, comandos, red, credenciales y recursos del sistema puede usar un agente durante su ejecución.

Es una capa de [[Guardarraíles|guardarraíles]] que limita el impacto cuando una decisión del agente, una herramienta o una instrucción externa falla.

No se trata de convencer al agente de que sea prudente, sino de poner límites que existen aunque el agente se equivoque. Si no puede leer secretos ni acceder a red, muchas consecuencias graves dejan de ser posibles.

## Funcionamiento

Un *sandbox* típico permite leer el proyecto, escribir solo en rutas autorizadas y usar red únicamente bajo reglas explícitas. También bloquea directorios de credenciales como `.ssh`, `.aws`, `.docker` o archivos privados del sistema.

Para más aislamiento, el agente puede ejecutarse dentro de un contenedor sin red y con el proyecto montado de forma controlada. En producción, los agentes que ejecutan código generado pueden requerir *sandboxes* por ejecución, credenciales efímeras y límites de CPU, memoria y tiempo.

## Errores comunes

- Confiar solo en instrucciones de *prompt* para controlar acceso.
- Dar red y credenciales por defecto.
- Ejecutar código no fiable en el host.
- Pensar que el *sandboxing* sustituye permisos, hooks o revisión.

## Preguntas

#flashcards/agents 

**¿Qué es el *sandboxing* de agentes?**
?
![[#Definición]]

**¿Qué tipos de acceso suele limitar un sandbox?**
?
![[#Funcionamiento]]

**¿Qué errores comunes aparecen al aislar agentes?**
?
![[#Errores comunes]]

