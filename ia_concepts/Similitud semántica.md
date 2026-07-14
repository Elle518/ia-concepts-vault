---
type: concept
tags:
  - llms
  - metrics
  - nlp
  - review
---

## Definición

La **similitud semántica** mide cuánto se parecen dos textos, conceptos u objetos (audio, imágenes, etc.) en significado.

En NLP moderno suele estimarse comparando sus *[[Embeddings|embeddings]]* con métricas como [[Similitud coseno|similitud coseno]].

La intuición es distinguir parecido de significado frente a parecido literal. “comprar un portátil” y “adquirir un laptop” son semánticamente cercanos aunque usen palabras distintas.

En evaluación de LLMs, se usa como subtipo de [[Evaluación por referencia|evaluación por referencia]] para comparar una respuesta generada con una respuesta esperada por significado, no por coincidencia literal.

## Uso

Se usa en:

- [[Búsqueda semántica|búsqueda semántica]]
- deduplicación de documentos
- clustering de textos
- recomendadores
- detección de paráfrasis
- evaluación aproximada de respuestas

La similitud semántica depende del modelo que genera los *embeddings* y del dominio de los datos.

## Diferencia con coincidencia léxica

La [[Similitud léxica|coincidencia léxica]] compara palabras exactas o tokens.

La similitud semántica intenta capturar significado. Esto permite recuperar expresiones equivalentes, pero también puede traer resultados demasiado generales o relacionados solo de forma indirecta.

En evaluación automática, la similitud léxica puede penalizar una respuesta correcta si usa palabras distintas. La similitud semántica reduce ese problema, pero depende de la calidad del modelo de *embeddings*.

La similitud semántica no requiere un conjunto de respuestas de referencia tan completo como lo requiere la similitud léxica. Sin embargo, del mismo modo, la fiabilidad de la similitud semántica depende de la calidad del algoritmo de *embeddings* subyacente. Dos textos con el mismo significado aún pueden tener una puntuación de similitud semántica baja si sus *embeddings* son malos.

## En evaluación automática

Para evaluar una respuesta generada, se calcula un *embedding* de la respuesta y otro de la referencia. Después se compara la distancia o similitud entre ambos vectores, por ejemplo con similitud coseno.

Aunque se suele incluir dentro de [[Evaluación exacta en LLMs|evaluación exacta]], tiene una parte subjetiva, ya que distintos modelos de *embeddings* pueden representar los textos de forma diferente.

Una vez fijado el modelo de *embeddings* y la métrica, el cálculo sí es determinista.

## Errores comunes

- Interpretar similitud alta como equivalencia exacta.
- Comparar *embeddings* de modelos distintos.
- Ignorar que dos textos pueden ser semánticamente parecidos pero tener respuestas opuestas.
- No calibrar umbrales de similitud con ejemplos reales.
- Usarla como sustituto de *[[Functional correctness|functional correctness]]* cuando la tarea requiere verificar si algo funciona.
- Ignorar que el algoritmo de *embeddings* subyacente puede requerir tiempo y computación no triviales para ejecutarse.

## Preguntas

#flashcards/llms #flashcards/metrics  #flashcards/nlp 

**¿Qué es la similitud semántica?**
?
![[#Definición]]

**¿Para qué se usa la similitud semántica?**
?
![[#Uso]]

**¿En qué se diferencia similitud semántica de similitud léxica?**
?
![[#Diferencia con coincidencia léxica]]

**¿Cómo se usa la similitud semántica en evaluación automática?**
?
![[#En evaluación automática]]

**¿Qué errores comunes hay al usar similitud semántica?**
?
![[#Errores comunes]]
