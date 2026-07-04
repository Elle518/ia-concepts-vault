---
type: concept
tags:
  - metric
  - ml
  - review
---

## Definición

La **exactitud** o *accuracy* es una métrica de [[Clasificación|clasificación]] que mide la proporción de predicciones correctas sobre el total de ejemplos.

Es simple e intuitiva, pero puede ser engañosa cuando las clases están desbalanceadas o cuando los errores tienen costes distintos.

## Fórmula

$$\text{accuracy} = \frac{\text{predicciones correctas}}{\text{total de predicciones}}$$

En clasificación binaria también puede escribirse como:

$$\text{accuracy} = \frac{TP + TN}{TP + TN + FP + FN}$$

donde $TP$ son verdaderos positivos, $TN$ verdaderos negativos, $FP$ falsos positivos y $FN$ falsos negativos.

## Cuándo usarla

La exactitud es útil cuando:

- las clases están razonablemente balanceadas
- todos los tipos de error tienen coste parecido
- se necesita una métrica fácil de comunicar

No es suficiente en problemas como fraude, diagnóstico médico o detección de spam si una clase es muy minoritaria.

## Errores comunes

- Usar *accuracy* como única métrica en datasets desbalanceados.
- Comparar *accuracy* entre datasets con distribuciones de clases distintas.
- Ignorar *precision*, *recall*, F1 o ROC-AUC cuando el coste de error importa.
- Confundir una *accuracy* alta con un modelo útil para producción.

## Preguntas

#flashcards/metrics #flashcards/ml

**¿Qué mide la exactitud o *accuracy*?**
?
![[#Definición]]

**¿Cómo se calcula *accuracy*?**
?
![[#Fórmula]]

**¿Cuándo es razonable usar *accuracy*?**
?
![[#Cuándo usarla]]

**¿Qué problema tiene *accuracy* en datasets desbalanceados?**
?
![[#Errores comunes]]
