---
type: concept
tags:
  - ml
  - nlp
  - review
---

## Definición

En general, el **aprendizaje autosupervisado** (*self-supervised learning*) consiste en que el modelo aprende usando señales generadas automáticamente a partir de los propios datos. 

En el contexto de los [[Modelo del lenguaje|modelos de lenguaje]], el aprendizaje autosupervisado es una forma de entrenamiento en la que el modelo aprende a partir de texto sin necesitar etiquetas humanas explícitas.

La idea clave es que el propio texto proporciona la “supervisión”. Es decir, se crea una tarea automática a partir de los datos.

Por ejemplo, en un modelo de lenguaje, podemos darle al modelo esta frase:

> “El gato duerme en el ___”

y pedirle que prediga la palabra que falta:

> “sofá”, “suelo”, “jardín”…

Aquí no hace falta que una persona haya etiquetado manualmente la frase. La respuesta correcta ya está en el propio texto original.

La auto-supervisión se diferencia del aprendizaje no supervisado. En el aprendizaje auto-supervisado, las etiquetas se infieren a partir de los datos de entrada. En el aprendizaje no supervisado, no se necesitan etiquetas en absoluto.

## Tipos de tareas

En modelos de lenguaje, las tareas autosupervisadas más habituales son:

**Predecir el siguiente token**, como hacen los modelos autoregresivos:

$$P(w_t \mid w_1, w_2, \dots, w_{t-1})$$

Por ejemplo:

> “Hoy hace mucho…” → “frío”

**Predecir tokens enmascarados**, como en modelos tipo BERT:

> “Hoy hace mucho [MASK]” → “frío”

## Utilidad

La auto-supervisión ayuda a superar el cuello de botella del etiquetado de datos. En la auto-supervisión, en lugar de requerir etiquetas explícitas, el modelo puede inferirlas a partir de los datos de entrada.

El modelado del lenguaje es auto-supervisado porque cada secuencia de entrada proporciona tanto las etiquetas (tokens que se deben predecir) como los contextos que el modelo puede usar para predecir dichas etiquetas. En modelos del lenguaje, normalmente significa aprender a predecir partes del texto a partir de otras partes del mismo texto.

Gracias a este enfoque, los modelos pueden entrenarse con enormes cantidades de texto sin que sea necesario anotarlo manualmente. Después, ese modelo preentrenado puede adaptarse a tareas concretas, como clasificación, resumen, extracción de entidades o respuesta a preguntas.

## Preguntas

#flashcards/nlp #flashcards/ml

**¿En qué consiste el aprendizaje autosupervisado?**
?
![[#Definición]]

**¿Qué tipos de tareas de aprendizaje autosupervisado existen?**
?
![[#Tipos de tareas]]

**¿Cuál es la utilidad del aprendizaje supervisado?**
?
![[#Utilidad]]
