---
type: concept
tags:
  - ml
  - review
---

## Definición

**PCA** (*principal component analysis*) es una técnica de [[Reducción de dimensionalidad|reducción de dimensionalidad]] que proyecta los datos sobre nuevas dimensiones llamadas **componentes principales**.

Estos componentes son direcciones ortogonales que capturan la mayor [[Varianza|varianza]] posible de los datos.

PCA busca el ángulo desde el que los datos se explican con menos ejes.

Si muchas características están correlacionadas, PCA puede resumirlas en menos componentes que conservan gran parte de la información.

## Funcionamiento

A alto nivel, PCA:

1. centra los datos
2. calcula las direcciones de máxima varianza
3. ordena esas direcciones por varianza explicada
4. proyecta los datos sobre los primeros componentes

El primer componente principal captura la mayor varianza posible. El segundo captura la mayor varianza restante bajo la restricción de ser ortogonal al primero.

## Cuándo usarlo

PCA es útil para compresión, visualización, reducción de ruido, preprocesamiento y mitigación de [[Multicolinealidad|multicolinealidad]].

Suele requerir [[Escalado|escalar]] las características si están en unidades o rangos muy distintos.

## Errores comunes

- Aplicar PCA sin escalar variables con magnitudes muy diferentes.
- Interpretar componentes principales como características originales.
- Asumir que mayor varianza siempre significa mayor relevancia predictiva.
- Usarlo cuando la estructura importante es fuertemente no lineal.

## Preguntas

#flashcards/ml

**¿Qué es PCA?**
?
![[#Definición]]

**¿Cómo funciona PCA a alto nivel?**
?
![[#Funcionamiento]]

**¿Qué utilidad tiene el PCA?**
?
![[#Cuándo usarlo]]

**¿Qué errores comunes aparecen al usar PCA?**
?
![[#Errores comunes]]
