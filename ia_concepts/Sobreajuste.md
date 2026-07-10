---
type: concept
tags:
  - ml
  - review
---

## Definición

El **sobreajuste** u *overfitting* ocurre cuando un modelo aprende demasiado bien los patrones específicos del conjunto de entrenamiento, incluyendo ruido o peculiaridades, y generaliza mal a datos nuevos.

Un modelo sobreajustado puede tener muy buen rendimiento en entrenamiento y mal rendimiento en validación o test.

Es como memorizar las respuestas de un examen de práctica en vez de aprender el tema. El modelo parece bueno mientras ve ejemplos parecidos a los que memorizó, pero falla cuando aparecen casos nuevos.

## Señales

Algunas señales típicas de sobreajuste son:

- pérdida de entrenamiento baja y pérdida de validación alta
- *accuracy* de entrenamiento mucho mayor que *accuracy* de validación
- rendimiento inestable ante pequeños cambios de datos
- reglas o árboles excesivamente complejos

## Cómo reducirlo

Se puede reducir con:

- más datos o *[[Data augmentation|data augmentation]]*
- [[Regularización|regularización]]
- *[[Early stopping|early stopping]]*
- modelos más simples
- *[[Dropout|dropout]]* en redes neuronales
- [[Validación cruzada|validación cruzada]]
- mejor separación entre [[Train, validation y test|train, validation y test]]

## Preguntas

#flashcards/ml

**¿Qué es el sobreajuste?**
?
![[#Definición]]

**¿Qué señales indican posible sobreajuste?**
?
![[#Señales]]

**¿Cómo se puede reducir el sobreajuste?**
?
![[#Cómo reducirlo]]
