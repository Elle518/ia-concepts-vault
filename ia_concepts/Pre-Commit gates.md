---
type: concept
tags:
  - agents
  - review
---

## Definición

Los ***pre-commit gates*** son controles automáticos que se ejecutan antes de aceptar o guardar cambios generados por un humano o por un [[Agente de IA|agente de IA]].

Su objetivo es bloquear cambios que no cumplen requisitos mínimos de calidad, seguridad o formato antes de que lleguen al repositorio.

Son una forma de convertir reglas de ingeniería en una barrera ejecutable.

Un agente puede escribir código rápido, pero eso no significa que el cambio sea correcto. Un *pre-commit gate* actúa como una puerta: si el cambio rompe el formateo, falla tests básicos o introduce patrones peligrosos, no pasa.

No intenta juzgar si la solución es perfecta, sino detectar errores antes de que se propaguen.

## Elementos de un pre-commit gate

Un *pre-commit gate* puede incluir:

- formateo automático
- linting
- tests unitarios rápidos
- comprobación de tipos
- detección de secretos
- reglas de seguridad sobre dependencias o comandos
- validación de archivos generados
- revisión de cambios prohibidos en rutas sensibles

En sistemas con agentes, estos *gates* son especialmente útiles porque el [[Harness de agente|harness]] o el [[Runtime de agente|runtime]] pueden ejecutarlos después de una edición y antes de continuar. También pueden combinarse con [[Hooks en agentes|hooks]], [[Permisos en agentes|permisos]] y [[Sandboxing de agentes|sandboxing]].

La regla práctica es que un *pre-commit gate* debe ser rápido, determinista y accionable. Si tarda demasiado o falla de forma opaca, los usuarios y agentes tenderán a saltárselo.

## Errores comunes

- Meter tests lentos o frágiles en el *gate* local.
- Tratar el *pre-commit gate* como sustituto de CI.
- Bloquear cambios sin explicar cómo corregirlos.
- Permitir que el agente ignore el *gate* después de fallar.
- No versionar la configuración del *gate* junto al código.

## Preguntas

#flashcards/agents

**¿Qué son los *pre-commit gates*?**
?
![[#Definición]]

**¿Qué tipos de comprobaciones suelen incluir los *pre-commit gates*?**
?
![[#Elementos de un pre-commit gate]]

**¿Qué errores comunes aparecen al diseñar *pre-commit gates*?**
?
![[#Errores comunes]]

