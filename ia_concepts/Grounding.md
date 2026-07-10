---
type: concept
tags:
  - llms
  - nlp
  - review
---

## Definición

***Grounding*** es la práctica de anclar la respuesta de un modelo a información disponible y verificable, como documentos recuperados, datos de una base de conocimiento, resultados de herramientas o contexto proporcionado por el usuario.

Su objetivo es reducir respuestas inventadas y hacer que el sistema dependa menos de la memoria paramétrica del modelo.

Es como pedir al modelo que conteste con los apuntes delante y que no rellene huecos con suposiciones.

## Funcionamiento

Un sistema con *grounding* suele:

- Recuperar o recibir contexto relevante.
- Instruir al modelo para responder solo con esa información.
- Pedir citas, evidencias o referencias cuando tenga sentido.
- Validar que la respuesta esté soportada por el contexto.
- Rechazar o marcar respuestas cuando falte evidencia.

[[RAG]] es una arquitectura común para implementar *grounding*, porque recupera documentos antes de generar la respuesta.

## Relación con alucinaciones

El *grounding* ayuda a reducir las [[Alucinación en LLMs|alucinaciones]] de los modelos, pero no las elimina automáticamente.

Puede fallar si la recuperación trae documentos irrelevantes, si el contexto contiene información falsa, si el modelo ignora la evidencia o si la pregunta requiere razonamiento que no está explícito en las fuentes.

Por eso se suele combinar con [[Guardarraíles|guardarraíles]], evaluación, verificación posterior y buenas instrucciones de rechazo cuando no hay información suficiente.

## Errores comunes

- Pensar que añadir documentos al contexto garantiza factualidad.
- No verificar que cada afirmación esté soportada por una fuente.
- Recuperar demasiado contexto y provocar *[[Context rot|context rot]]*.
- Permitir que el modelo mezcle fuente recuperada con conocimiento no verificado.
- Confundir citas generadas con citas realmente existentes.

## Preguntas

#flashcards/llms #flashcards/nlp 

**¿Qué es *grounding* en sistemas con LLMs?**
?
![[#Definición]]

**¿Cómo suele funcionar un sistema con *grounding*?**
?
![[#Funcionamiento]]

**¿Cómo se relaciona *grounding* con las alucinaciones?**
?
![[#Relación con alucinaciones]]

**¿Qué errores comunes hay al aplicar *grounding*?**
?
![[#Errores comunes]]
