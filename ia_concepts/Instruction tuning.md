---
type: concept
tags:
  - llms
  - ml
  - review
---

## Definición

El ***instruction tuning*** es una forma de [[Fine-tuning|fine-tuning]] en la que un modelo se entrena con pares de instrucciones y respuestas esperadas.

Su objetivo es que el modelo aprenda a seguir instrucciones humanas de forma más útil, general y consistente.

Un modelo preentrenado aprende a predecir texto. Un modelo con *instruction tuning* aprende mejor el patrón “el usuario pide algo y yo debo responder de forma adecuada”.

No solo aprende contenido, también aprende formato, tono, obediencia a instrucciones y comportamiento conversacional.

## Funcionamiento

El dataset suele contener ejemplos como:

- instrucción del usuario
- contexto opcional
- respuesta ideal

Durante el entrenamiento, el modelo ajusta sus pesos para producir respuestas parecidas a las respuestas objetivo. Esto ayuda a convertir un modelo base en un modelo más usable como asistente.

El *instruction tuning* suele combinarse después con [[RLHF]] u otros métodos de alineamiento.

## Errores comunes

- Confundir *instruction tuning* con *prompting*, en *instruction tuning* se actualizan pesos.
- Pensar que elimina por completo alucinaciones o respuestas inseguras.
- Usar datasets de instrucciones de baja calidad y esperar buen comportamiento general.
- Asumir que seguir instrucciones siempre implica razonar correctamente.

## Preguntas

#flashcards/llms #flashcards/ml

**¿Qué es *instruction tuning*?**
?
![[#Definición]]

**¿Cómo funciona *instruction tuning* a alto nivel?**
?
![[#Funcionamiento]]

**¿En qué se diferencia *instruction tuning* de *prompting*?**
?
![[#Errores comunes]]
