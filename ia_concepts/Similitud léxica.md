---
type: concept
tags:
  - llms
  - metrics
  - nlp
  - review
---

## Definición

La **similitud léxica** o *lexical similarity* mide cuánto se parecen dos textos en su superficie: palabras, caracteres, tokens o [[n-gramas]] compartidos.

Es un subtipo de [[Evaluación por referencia]] usado para comparar una respuesta generada con una o varias referencias.

No mide directamente significado, sino cuánto se solapan dos textos.

Si la referencia es `My cats scare the mice`, una respuesta como `My cats eat the mice` tendrá alta similitud léxica porque comparte muchas palabras.

Una respuesta como `Cats and mice fight all the time` puede expresar una idea relacionada, pero comparte menos tokens.

## Métodos comunes

Una forma simple es contar tokens en común.

Otra es usar *[[Fuzzy matching|fuzzy matching]]*, que mide cuántas ediciones hacen falta para convertir un texto en otro. Esa cantidad se llama *[[Distancia de edición|edit distance]]*.

Las operaciones típicas son:

- *deletion* o eliminación
- *insertion* o inserción
- *substitution* o sustitución
- *transposition* o transposición. Algunas implementaciones tratan cada transposición como dos operaciones de edición: una eliminación y una inserción.

También se puede medir solapamiento de n-gramas en lugar de tokens únicos. Un unigrama es un token,  un bigrama es una secuencia de dos tokens, etc. Mide qué porcentaje de n-gramas en las respuestas de referencia también está en la respuesta generada.

Métricas conocidas de similitud léxica incluyen BLEU, ROUGE, METEOR, TER y CIDEr. Difieren en cómo se calcula exactamente la superposición.

## Limitaciones

Una desventaja de este método es que requiere seleccionar un conjunto muy completo de respuestas de referencia. Si no, una respuesta correcta puede recibir baja puntuación si usa palabras distintas a la referencia. Una respuesta incorrecta puede recibir alta puntuación si se parece mucho en superficie.

La métrica depende mucho de la cobertura y calidad de las referencias.

En modelos modernos, estas métricas suelen ser menos fiables que evaluaciones semánticas o funcionales para tareas abiertas.

## Preguntas

#flashcards/llms #flashcards/metrics #flashcards/nlp

**¿Qué mide la similitud léxica?**
?
![[#Definición]]

**¿Qué métodos se usan para medir similitud léxica?**
?
![[#Métodos comunes]]

**¿Qué limitaciones tiene la similitud léxica?**
?
![[#Limitaciones]]
