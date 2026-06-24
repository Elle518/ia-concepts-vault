---
type: concept
tags:
  - llms
  - nlp
  - review
---

## Definición

Un **modelo fundacional** es un modelo de IA entrenado con grandes cantidades de datos, normalmente de forma **[[Aprendizaje autosupervisado|autosupervisada]]**, que sirve como base para muchas tareas diferentes.

En el contexto de los [[Modelo del lenguaje|modelos de lenguaje]], un modelo fundacional sería, por ejemplo, un gran modelo preentrenado sobre texto. Durante ese preentrenamiento aprende patrones generales del lenguaje: gramática, significado, estilos, relaciones entre conceptos, razonamiento básico, conocimiento del mundo, etc.

Después, ese modelo base puede adaptarse o usarse para muchas tareas concretas, como:

- clasificación de textos    
- resumen automático
- traducción
- extracción de información
- generación de texto
- respuesta a preguntas
- chatbots
- análisis de sentimiento

De este modo, un modelo fundacional es un modelo base, grande y generalista, que puede reutilizarse y adaptarse a muchas tareas posteriores.

## Idea clave

La idea importante es que **no se entrena desde cero para una sola tarea**, sino que primero aprende una representación general y reutilizable. Luego puede especializarse mediante técnicas como ***[[Fine-tuning|fine-tuning]]***, ***[[Instruction tuning|instruction tuning]]***, **[[RLHF]]**, **[[RAG]]** o simplemente mediante ***[[Prompt engineering|prompting]]***.

Los modelos fundacionales, gracias a su escala y al método de entrenamiento, son capaces de realizar de forma predeterminada una amplia gama de tareas. Por ejemplo, un modelo LLM puede realizar tanto análisis de sentimiento como traducción. Sin embargo, a menudo es posible optimizar un modelo de propósito general para maximizar su rendimiento en una tarea específica.

## Modelos multimodales

Muchos de estos modelos son además **multimodales** (*large multimodal model* o LMM), es decir, pueden trabajar a la vez con más de un tipo de datos: texto, imágenes, vídeos, audio, etc.

## Preguntas

#flashcards/llms #flashcards/nlp 

¿Qué es un modelo fundacional?
?
[[Modelo fundacional#Definición]]

¿Cuál es la idea clave detrás de los modelos fundacionales?
?
[[Modelo fundacional#Idea clave]]

¿Qué es un modelo multimodal o LMM?
?
[[Modelo fundacional#Modelos multimodales]]