---
type: concept
tags:
  - llms
  - ai-engineering
  - review
---

## Definición

***Context rot*** es la degradación de rendimiento que aparece cuando la [[Ventana de contexto|ventana de contexto]] de un [[Modelo del lenguaje|LLM]] se llena con demasiada información, especialmente si parte de ella es irrelevante, redundante o antigua.

Aunque el modelo acepte contextos muy largos, no significa que atienda igual de bien a todo el contenido.

Más contexto no siempre significa más claridad. Si llenas la mesa de trabajo con todos los documentos posibles, la información importante queda enterrada entre ruido.

## Explicación técnica

En un LLM de tipo *[[Arquitectura Transformer|transformer]]*, cada token reparte su atención entre muchos otros tokens. A medida que el contexto crece, la señal relevante compite con más material. Además, los modelos suelen estar mejor entrenados en longitudes más cortas que en contextos extremos.

## Mitigación

En los [[Agente de IA|agentes]], el *context rot* aparece por [[Agent config files|archivos de configuración]] largos, logs completos, resultados de herramientas sin resumir, memoria acumulada y *workflows* genéricos. La mitigación consiste en mantener el contexto activo pequeño, recuperar información bajo demanda, resumir *handoffs* y mover estado susceptible de ser persistido fuera del *prompt*.

## Errores comunes

- Creer que una ventana de contexto enorme elimina la necesidad de retrieval.
- Añadir reglas genéricas “por si acaso”.
- Mantener observaciones antiguas que ya no afectan la próxima acción.
- Evaluar solo el coste de tokens e ignorar calidad de atención.

## Preguntas

#flashcards/agents

**¿Qué es el *context rot*?**
?
![[#Definición]]

**¿Por qué un contexto más largo puede empeorar la calidad?**
?
![[#Explicación técnica]]

**¿Cómo se mitiga el *context rot* en agentes?**
?
![[#Mitigación]]

**¿Qué errores comunes llevan a *context rot*?**
?
![[#Errores comunes]]
