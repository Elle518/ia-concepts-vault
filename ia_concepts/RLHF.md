---
type: concept
tags:
  - llms
  - ml
  - review
---

## Definición

**RLHF** (*reinforcement learning from human feedback*) es una técnica de *[[Preference Finetuning|preference finetuning]]* para ajustar modelos usando preferencias humanas.

En LLMs, se usa para hacer que las respuestas sean más útiles, seguras y alineadas con lo que las personas consideran una buena respuesta.

No siempre sabemos escribir una respuesta ideal, pero sí podemos comparar dos respuestas y decir cuál preferimos. RLHF aprovecha esas comparaciones para enseñar al modelo qué tipo de salida recibe mejor valoración humana.

## Funcionamiento

Un *pipeline* típico de RLHF tiene tres pasos:

1. Se parte de un modelo ya preentrenado y normalmente ajustado con [[Instruction tuning|instruction tuning]].
2. Humanos comparan respuestas y esas preferencias se usan para entrenar un ***[[Reward model|reward model]]***.
3. El modelo se optimiza para producir respuestas con mayor *reward*, por ejemplo con métodos de [[Reinforcement Learning|reinforcement learning]].

El resultado no es una garantía de verdad, sino una adaptación del comportamiento del modelo a preferencias observadas.

## Modelo de recompensa

Dado un par `(prompt, response)`, el modelo de recompensa genera una puntuación que indica la calidad de la respuesta.

Entrenar un modelo para puntuar una entrada dada es una tarea común en el aprendizaje automático. El desafío, similar al del [[Supervised finetuning|SFT]], radica en obtener datos fiables.

Si se pide a los etiquetadores que puntúen cada respuesta directamente (***pointwise evaluation***), las puntuaciones variarán. Para la misma muestra, en una escala de 10 puntos, un etiquetador podría asignar un 5 y otro un 7. Incluso el mismo etiquetador, al recibir el mismo par dos veces, podría dar puntuaciones diferentes.

Una tarea más sencilla consiste en pedir a los etiquetadores que comparen dos respuestas y decidan cuál es mejor. Para cada pregunta, se generan múltiples respuestas, ya sea por humanos o por IA. Los datos etiquetados resultantes se denominan ***comparison data,***, y siguen el formato `(prompt, winning_response, losing_response)`.

Aún así, esta tarea más sencilla de comparar dos respuestas también requiere tiempo y dinero, aunque sea mucho más económico que la de escribir los pares `(prompt, response)` para el SFT.

El modelo de recompensa se puede entrenar desde cero o ajustar sobre otro modelo, como el preentrenado o el modelo SFT. El ajuste sobre el modelo base más robusto parece ofrecer el mejor rendimiento.

Algunos creen que el modelo de recompensa debería ser al menos tan potente como el modelo base para poder puntuar sus respuestas. Sin embargo, se ha demostrado que un modelo más débil puede juzgar a uno más fuerte, ya que se considera que juzgar es más fácil que generar.

### Ajuste mediante el modelo de recompensa

Con el modelo de recompensa entrenado, entrenamos aún más el modelo SFT para generar respuestas que maximicen las puntuaciones del modelo de recompensa. Durante este proceso, se seleccionan aleatoriamente preguntas de una distribución, como por ejemplo de un conjunto de preguntas de usuarios ya existentes.

Estas preguntas se introducen en el modelo, cuyas respuestas son puntuadas por el modelo de recompensa. Este proceso de entrenamiento se suele realizar con la [[Proximal Policy Optimization|proximal policy optimization]] (PPO), un algoritmo de aprendizaje por refuerzo lanzado por OpenAI en 2017.

Empíricamente, tanto RLHF como [[DPO]] mejoran el rendimiento en comparación con SFT por sí solo.

## Limitaciones

- Las preferencias humanas pueden ser inconsistentes o sesgadas.
- El modelo puede aprender a sonar convincente aunque esté equivocado.
- Optimizar demasiado el *reward* puede explotar defectos del *reward model*.
- Es costoso en datos, infraestructura y evaluación.

## Preguntas

#flashcards/llms #flashcards/ml

**¿Qué es RLHF?**
?
![[#Definición]]

**¿Cuáles son los pasos principales de un pipeline de RLHF?**
?
![[#Funcionamiento]]

**¿Qué es un modelo de recompensa y cómo funciona?**
?
![[#Modelo de recompensa]]

**¿Qué limitaciones tiene RLHF?**
?
![[#Limitaciones]]
