---
type: concept
tags:
  - ml
  - dl
  - review
---

## Definición

El ***batch size*** o **tamaño de lote** es el número de muestras que se procesan juntos antes de actualizar los [[Parámetro|parámetros]] del modelo durante el entrenamiento.

En vez de calcular el gradiente con todo el dataset, se usan grupos de muestras llamados *batches* o lotes.

La intuición es estudiar con grupos de ejercicios. Un *batch* pequeño da *feedback* frecuente pero ruidoso, mientras que un *batch* grande da *feedback* más estable pero menos frecuente.

## Efecto en el entrenamiento

El *batch size* afecta a:

- la estabilidad de los gradientes
- la velocidad de entrenamiento
- el uso de memoria
- la calidad de la generalización
- la interacción con el *[[Tasa de aprendizaje|learning rate]]*

*Batch sizes* pequeños introducen más ruido en la actualización, lo que a veces ayuda a escapar de mínimos locales pobres. *Batch sizes* grandes aprovechan mejor el *hardware* paralelo, pero pueden requerir ajustar el *learning rate* y consumir mucha memoria.

## Trade-offs

Un *batch size* grande puede entrenar más rápido por época, pero no siempre mejora el rendimiento final. También puede hacer que cada actualización sea más cara y menos frecuente.

Un *batch size* pequeño puede generalizar bien y usar menos memoria, pero el entrenamiento puede ser más ruidoso y lento en *hardware* moderno.

## Errores comunes

- Cambiar el *batch size* sin revisar el *learning rate*.
- Asumir que un *batch* más grande siempre es mejor.
- Comparar experimentos sin mantener constante el presupuesto de entrenamiento.
- Ignorar los límites de memoria de la GPU.
- Confundir *batch size* con número total de ejemplos del dataset.

## Preguntas

#flashcards/ml #flashcards/dl

**¿Qué es el *batch size*?**
?
![[#Definición]]

**¿Qué aspectos del entrenamiento afecta el *batch size*?**
?
![[#Efecto en el entrenamiento]]

**¿Qué *trade-off* hay entre *batch sizes* pequeños y grandes?**
?
![[#Trade-offs]]

**¿Qué errores comunes hay al ajustar el *batch size*?**
?
![[#Errores comunes]]
