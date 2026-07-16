---
type: concept
tags:
  - ml
  - dl
  - review
---

## Definición

***Data augmentation*** es una técnica para aumentar la variedad de datos de entrenamiento aplicando transformaciones que conservan la etiqueta o el significado relevante.

Su objetivo es mejorar la generalización del modelo y reducir el [[Sobreajuste|sobreajuste]] sin recoger necesariamente más datos reales.

La intuición es enseñar el mismo concepto desde variantes distintas. Si un modelo ve una imagen rotada, recortada o con ruido, aprende a no depender de detalles accidentales.

Es útil cuando los datos son escasos, el modelo sobreajusta o esperamos variaciones naturales en producción.

La transformación debe preservar la etiqueta. Si una augmentación cambia el significado, introduce ruido y puede empeorar el aprendizaje.

## Ejemplos

En visión por computador:

- rotaciones
- recortes
- cambios de brillo o contraste
- flips
- ruido

En texto:

- paráfrasis
- sustitución controlada de palabras
- eliminación o inserción leve de tokens
- traducción ida y vuelta

En audio:

- ruido de fondo
- cambios de velocidad
- desplazamientos temporales

## Errores comunes

- Aplicar transformaciones que cambian la etiqueta real.
- Usar transformaciones demasiado agresivas para el dominio.
- Creer que sustituye a datos reales de calidad.
- No validar si usar data augmentation realmente mejora en datos fuera del entrenamiento.

## Preguntas

#flashcards/ml #flashcards/dl

**¿Qué es *data augmentation*?**
?
![[#Definición]]

**¿Qué ejemplos de *data augmentation* existen?**
?
![[#Ejemplos]]

**¿Qué errores comunes hay al usar *data augmentation*?**
?
![[#Errores comunes]]
