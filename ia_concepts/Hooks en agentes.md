---
type: concept
tags:
  - agents
  - review
---

## Definición

Los ***hooks* en agentes** son manejadores que se ejecutan automáticamente en puntos concretos del workflow del agente, por ejemplo antes de ejecutar una herramienta o después de modificar un archivo.

Un caso especialmente importante es el *pre-tool hook*, que inspecciona una acción antes de que llegue al sistema real.

El modelo propone una acción, el hook es el control de última milla que puede revisarla, bloquearla o transformarla antes de que ocurra.

## Utilidad

Los hooks pueden validar:

- comandos de *shell*
- llamadas a herramientas o MCP
- escrituras de archivos
- formatos de salida
- políticas de seguridad

Para seguridad, un pre-tool hook puede detectar patrones como `curl | sh`, rutas sospechosas, transporte inseguro, manipulación de entorno, caracteres homoglifos o intentos de leer secretos. Debe verse como complemento de [[Permisos en agentes|permisos]] y *[[Sandboxing de agentes|sandboxing]]*, no como sustituto.

## Errores comunes

- Usar hooks demasiado lentos o frágiles.
- Bloquear patrones legítimos sin mensaje accionable.
- Depender solo del *hook* para seguridad.
- No versionar ni probar las reglas del hook.

## Preguntas

#flashcards/agents

**¿Qué son los *hooks* en agentes?**
?
![[#Definición]]

**¿Qué utilidad tiene un *hook* de seguridad?**
?
![[#Utilidad]]

**¿Qué errores comunes aparecen al diseñar *hooks* de agentes?**
?
![[#Errores comunes]]
