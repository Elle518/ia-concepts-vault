---
type: concept
tags:
  - ml
  - review
---

## Definición

***Random search*** es una técnica de búsqueda de [[Hiperparámetros|hiperparámetros]] que prueba configuraciones elegidas aleatoriamente dentro de una serie de rangos definidos.

En lugar de recorrer todas las combinaciones posibles, asigna un presupuesto de pruebas y explora el espacio de forma aleatoria.

*Random search* asume que no todos los hiperparámetros importan igual. Si solo unos pocos hiperparámetros explican la mayor parte del rendimiento, probar puntos aleatorios puede cubrir mejor esos valores importantes que una cuadrícula rígida.

## Cuándo usarlo

Tiene sentido cuando:

- hay muchos hiperparámetros
- no sabemos qué rangos son mejores
- el presupuesto de entrenamiento es limitado
- queremos una *baseline* simple antes de métodos más complejos

Suele ser sorprendentemente competitivo frente a *[[Grid search|grid search]]* cuando el espacio de búsqueda es grande.

## Errores comunes

- Definir rangos de búsqueda poco realistas.
- Usar distribuciones uniformes cuando convendría buscar en escala logarítmica.
- No fijar semillas o registrar configuraciones, dificultando reproducibilidad.
- Evaluar demasiadas configuraciones sobre el test set.

## Preguntas

#flashcards/ml

**¿Qué es *random search*?**
?
![[#Definición]]

**¿Cuándo tiene sentido usar *random search*?**
?
![[#Cuándo usarlo]]

**¿Qué errores comunes aparecen al usar *random search*?**
?
![[#Errores comunes]]
