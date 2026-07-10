---
type: concept
tags:
  - ml
  - review
---

## Definición

La **optimización bayesiana** es una técnica para elegir [[Hiperparámetros|hiperparámetros]] usando un modelo probabilístico que estima qué configuraciones prometen mejores resultados.

Es útil cuando evaluar cada configuración es caro, por ejemplo porque implica entrenar un modelo.

## Intuición

En vez de probar configuraciones a ciegas, la optimización bayesiana aprende de los experimentos anteriores.

Mantiene una estimación de qué zonas del espacio parecen buenas y decide si conviene explotar zonas prometedoras o explorar zonas inciertas.

## Funcionamiento

El proceso típico es:

1. probar algunas configuraciones iniciales
2. entrenar un modelo sustituto del rendimiento esperado
3. usar una función de adquisición para elegir la siguiente configuración
4. evaluar esa configuración real
5. actualizar el modelo sustituto y repetir

El modelo sustituto puede ser un [[Proceso gaussiano|proceso gaussiano]], un *[[Random forest|random forest]]* o un modelo tipo [[Tree-structured Parzen Estimator|TPE]], según la herramienta.

## Comparación

Frente a *[[Grid search|grid search]]* y *[[Random search|random search]]*, puede encontrar buenas configuraciones con menos evaluaciones.

A cambio, introduce más complejidad y no siempre compensa si los entrenamientos son baratos o el espacio de búsqueda es pequeño.

## Preguntas

#flashcards/ml

**¿Qué es la optimización bayesiana de hiperparámetros?**
?
![[#Definición]]

**¿Cómo funciona la optimización bayesiana a alto nivel?**
?
![[#Funcionamiento]]

**¿Cómo se compara con grid search y random search?**
?
![[#Comparación]]
