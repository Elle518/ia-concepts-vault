---
type: concept
tags:
  - agents
  - review
---

## Definición

***Model Context Protocol*** o **MCP** es un estándar para exponer herramientas, recursos y servicios externos a [[Agente de IA|agentes de IA]] de una forma que el agente y su *[[Runtime de agente|runtime]]* puedan entender de manera uniforme.

Un servidor MCP puede ofrecer herramientas para consultar documentación, buscar en repositorios, leer bases de datos, acceder a APIs o recuperar conocimiento.

MCP intenta ser un conector estándar, en vez de escribir una integración distinta para cada herramienta y cada agente, la herramienta se presenta con un protocolo común.

## Funcionamiento

El [[Harness de agente|harness]] conecta con servidores MCP, lee sus descripciones de herramientas, valida llamadas y devuelve resultados al modelo como observaciones.

MCP aporta estandarización, autenticación, permisos y distribución organizativa.

## MCP y contexto del agente

Su coste principal es el contexto: si se cargan demasiados esquemas completos de herramientas, el *prompt* se llena. Por eso muchos sistemas usan carga diferida, donde el agente ve primero nombres y descripciones y solo carga el schema completo cuando decide usar una herramienta.

## Errores comunes

- Usar MCP cuando una CLI o API simple bastaría.
- Cargar demasiadas herramientas desde el inicio.
- Confiar en servidores MCP externos sin revisar permisos.
- Olvidar que un servidor MCP es código con capacidad de actuar.

## Preguntas

#flashcards/agents

**¿Qué es MCP en sistemas de agentes?**
?
![[#Definición]]

**¿Qué problemas resuelve MCP?**
?
![[#Funcionamiento]]

**¿Por qué MCP puede empeorar el contexto de un agente?**
?
![[#MCP y contexto del agente]]

**¿Qué riesgos aparecen al usar servidores MCP?**
?
![[#Errores comunes]]
