---
type: concept
tags:
  - dl
  - review
---

## Definición

**AdamW** es una variante de [[Adam]] que aplica *[[Weight decay|weight decay]]* de forma desacoplada de la actualización basada en gradientes.

Es uno de los optimizadores más usados en *deep learning* moderno, especialmente en modelos tipo [[Arquitectura Transformer|transformer]].

La idea clave es separar dos cosas distintas: cómo optimizamos la [[Función de pérdida|pérdida]] y cómo penalizamos pesos grandes para mejorar la generalización.

## Diferencia con Adam

En Adam clásico, la [[Regularización L2|regularización L2]] puede mezclarse con las estadísticas adaptativas del optimizador. Esto hace que el efecto real de la penalización dependa del mecanismo interno de Adam.

AdamW desacopla el *weight decay*, ya que primero calcula la actualización adaptativa y después aplica una reducción directa sobre los pesos. Esto suele dar un control más claro de la [[Regularización|regularización]].

## Cuándo usarlo

AdamW suele ser una buena opción cuando:

- se entrenan redes profundas
- se usan transformers o LLMs
- queremos usar *weight decay* de forma explícita
- Adam converge bien pero la generalización necesita control adicional

En muchos setups modernos, AdamW es el optimizador por defecto antes de considerar alternativas más específicas.

## Errores comunes

- Usar Adam con regularización L2 pensando que equivale exactamente a AdamW.
- Aplicar *weight decay* a todos los parámetros sin revisar excepciones como biases o parámetros de normalización.
- No ajustar el *learning rate* y el *weight decay* conjuntamente.
- Pensar que AdamW sustituye a una buena validación.

## Preguntas

#flashcards/dl

**¿Qué es AdamW?**
?
![[#Definición]]

**¿En qué se diferencia AdamW de Adam?**
?
![[#Diferencia con Adam]]

**¿Cuándo suele usarse AdamW?**
?
![[#Cuándo usarlo]]

**¿Qué errores comunes hay al usar AdamW?**
?
![[#Errores comunes]]
