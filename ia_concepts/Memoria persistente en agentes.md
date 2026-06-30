---
type: concept
tags:
  - agents
  - review
---

## Definición

La **memoria persistente en agentes** es información que sobrevive entre sesiones y que el [[Agente de IA|agente]] puede recuperar para no empezar siempre desde cero.

Puede ser un archivo simple, como `MEMORY.md`, o una capa indexada con [[Embeddings|embeddings]] y búsqueda semántica.

El contexto es memoria de corto plazo. La memoria persistente es el cuaderno donde quedan decisiones, convenciones y contexto que mañana seguirán importando.

## Utilización

La forma más simple es un archivo Markdown que el agente lee al inicio y actualiza durante el trabajo. Sirve para convenciones, decisiones arquitectónicas, resúmenes de sesiones y hechos estables.

Cuando crece demasiado, se convierte en otra fuente de [[Context rot|context rot]]. En ese punto conviene separar memoria en una capa recuperable: indexar sesiones, decisiones o notas y traer solo fragmentos relevantes mediante búsqueda, parecido a un [[RAG]] interno.

## Errores comunes

- Guardar todo en memoria sin curación.
- Mezclar hechos estables con tareas temporales.
- Permitir que el agente reescriba memoria crítica sin revisión.
- Confundir memoria persistente con logs completos.

## Preguntas

#flashcards/agents 

**¿Qué es la memoria persistente en agentes?**
?
![[#Definición]]

**¿Cuándo conviene pasar de `MEMORY.md` a una memoria indexada?**
?
![[#Utilización]]

**¿Qué riesgos tiene una memoria persistente mal gestionada?**
?
![[#Errores comunes]]
