---
type: concept
tags:
  - ml
  - review
---

## Definición

Un **proceso gaussiano** (*Gaussian process*, GP) es un modelo probabilístico que define una distribución sobre funciones.

En vez de aprender una única función fija, estima muchas funciones posibles compatibles con los datos observados y mantiene incertidumbre sobre las zonas donde hay pocos datos.

La intuición es tener una curva con una banda de confianza alrededor. Donde ya hemos observado datos, la predicción es más segura; donde no hemos probado, la incertidumbre aumenta.

## Uso en optimización bayesiana

En [[Optimización bayesiana|optimización bayesiana]], un proceso gaussiano se usa a menudo como **modelo sustituto** del rendimiento real.

Esto es útil cuando evaluar una configuración de [[Hiperparámetros|hiperparámetros]] es caro. En lugar de entrenar el modelo para todas las configuraciones posibles, el GP estima:

- qué rendimiento esperamos en una configuración nueva
- cuánta incertidumbre hay sobre esa estimación

Después, una función de adquisición usa esa información para decidir dónde probar a continuación, equilibrando explotación de zonas prometedoras y exploración de zonas inciertas.

## Explicación técnica

Un proceso gaussiano queda definido por:

- una función media
- una función de covarianza o *[[Kernel|kernel]]*

El *kernel* determina qué tan parecidas se consideran dos configuraciones. Si dos puntos del espacio de hiperparámetros son cercanos según el *kernel*, el modelo espera que sus resultados también sean parecidos.

La ventaja del GP es que produce predicción e incertidumbre de forma natural. La limitación es que puede escalar mal cuando hay muchas observaciones o espacios de búsqueda complejos.

## Cuándo usarlo

Tiene sentido cuando:

- cada evaluación es cara
- el número de evaluaciones previas no es enorme
- el espacio de búsqueda es relativamente continuo
- queremos modelar explícitamente la incertidumbre

Puede ser menos adecuado para espacios muy grandes, categóricos, condicionales o con muchas dimensiones.

## Errores comunes

- Pensar que un proceso gaussiano asume que los datos observados siguen una única distribución normal simple.
- Ignorar la elección del *kernel*, que afecta mucho al comportamiento del modelo.
- Usarlo en espacios de hiperparámetros muy grandes sin revisar escalabilidad.
- Confundir el modelo sustituto con la evaluación real del modelo entrenado.

## Preguntas

#flashcards/ml

**¿Qué es un proceso gaussiano?**
?
![[#Definición]]

**¿Para qué se usa un proceso gaussiano en optimización bayesiana?**
?
![[#Uso en optimización bayesiana]]

**¿Qué papel tiene el *kernel* en un proceso gaussiano?**
?
![[#Explicación técnica]]

**¿Cuándo tiene sentido usar procesos gaussianos como modelo sustituto?**
?
![[#Cuándo usarlo]]

**¿Qué errores comunes hay al usar procesos gaussianos?**
?
![[#Errores comunes]]
