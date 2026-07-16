---
type: concept
tags:
  - llms
  - nlp
  - review
---

## Definición

***Semantic chunking*** divide un documento según cambios de significado, no solo por tamaño o separadores.

Suele usar *[[Embeddings|embeddings]]*, similitud entre frases o [[modelos de lenguaje|modelos de lenguaje]] para agrupar contenido semánticamente coherente.

La intuición es cortar cuando cambia el tema, no cuando se alcanza un número arbitrario de tokens.

Es útil cuando los documentos mezclan temas, cuando los párrafos son largos o cuando la estructura formal no refleja bien el contenido.

Puede mejorar el [[Búsqueda semántica|retrieval]] porque cada *chunk* tiende a representar una idea más coherente.

## Funcionamiento

Un enfoque habitual es:

1. dividir el texto en frases o párrafos
2. calcular *embeddings* para cada unidad
3. medir similitud entre unidades consecutivas
4. detectar puntos donde la similitud cae
5. formar *chunks* con unidades semánticamente cercanas

También puede usarse un LLM para proponer cortes, aunque eso aumenta coste y latencia.

## Trade-offs

Ventajas:

- genera *chunks* más coherentes
- puede reducir ruido dentro de cada fragmento
- se adapta mejor a cambios de tema

Limitaciones:

- es más caro que cortar por reglas simples
- depende del modelo de *embeddings* o del LLM usado
- puede ser menos reproducible si usa generación
- requiere evaluación para saber si mejora el RAG real
- no siempre supera estrategias más simples, hay que medirlo

## Preguntas

#flashcards/llms #flashcards/nlp

**¿Qué es *semantic chunking*?**
?
![[#Definición]]

**¿Cómo suele funcionar *semantic chunking*?**
?
![[#Funcionamiento]]

**¿Qué trade-offs tiene *semantic chunking*?**
?
![[#Trade-offs]]
