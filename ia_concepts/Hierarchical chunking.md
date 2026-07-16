---
type: concept
tags:
  - llms
  - nlp
  - review
---

## Definición

***Hierarchical chunking*** organiza los chunks en varios niveles de granularidad, por ejemplo *chunks* pequeños dentro de secciones más grandes.

En [[RAG]] también se conoce como estrategia **parent-child**, cuando se indexan *chunks* hijos pequeños pero se recupera o entrega al modelo el *chunk* padre con más contexto.

La intuición es buscar con fragmentos precisos, pero responder con contexto suficiente.

Es útil cuando los *chunks* pequeños recuperan mejor, pero por sí solos no contienen suficiente contexto para responder.

También encaja bien en documentación larga, políticas internas, manuales técnicos y bases de conocimiento con jerarquías claras.

## Funcionamiento

Un flujo común es:

1. dividir el documento en secciones grandes o *chunks* padre
2. dividir cada padre en *chunks* hijos más pequeños
3. crear *embeddings* e indexar los *chunks* hijos
4. al recuperar un hijo relevante, traer también su padre o una ventana ampliada

Así se combina precisión en la búsqueda con contexto ampliado para generación.

## Trade-offs

Ventajas:

- mejora la precisión del retrieval inicial
- reduce el riesgo de perder contexto
- aprovecha metadatos jerárquicos
- puede evitar respuestas basadas en fragmentos demasiado aislados

Limitaciones:

- aumenta complejidad del *pipeline*
- puede introducir más tokens en el contexto final
- requiere decidir qué nivel devolver al modelo
- puede recuperar contexto irrelevante si el padre es demasiado amplio

## Preguntas

#flashcards/llms #flashcards/nlp

**¿Qué es *hierarchical chunking*?**
?
![[#Definición]]

**¿Cómo funciona una estrategia de *hierarchical chunking*?**
?
![[#Funcionamiento]]


**¿Qué trade-offs tiene *hierarchical chunking*?**
?
![[#Trade-offs]]
