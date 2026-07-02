---
type: concept
tags:
  - ml
  - review
---

## Definición

La **reducción de dimensionalidad** consiste en transformar un dataset con muchas variables en una representación con menos dimensiones, intentando conservar la información más relevante.

Es una tarea habitual de [[Aprendizaje no supervisado|aprendizaje no supervisado]], aunque también puede aparecer como paso de preprocesamiento en *pipelines* supervisados.

Si muchas variables cuentan información parecida, podemos resumirlas en menos variables. Por ejemplo, en lugar de trabajar con decenas de características correlacionadas de clientes, podemos proyectarlas a unos pocos componentes que capturen la mayor parte de la variación útil.

## Utilidad

La reducción de dimensionalidad puede usarse para:

- visualizar datos de alta dimensión
- reducir ruido
- acelerar entrenamiento o inferencia
- mitigar problemas de multicolinealidad
- construir features más compactas

## Técnicas de reducción de dimensionalidad

Una técnica clásica es **[[PCA]]** (*principal component analysis*), que encuentra direcciones ortogonales de máxima varianza y proyecta los datos sobre los primeros componentes principales.

También existen métodos no lineales como [[t-SNE]] y [[UMAP]], usados sobre todo para visualización.

## Preguntas

#flashcards/ml

**¿Qué es la reducción de dimensionalidad?**
?
![[#Definición]]

**¿Para qué se usa la reducción de dimensionalidad?**
?
![[#Utilidad]]

**¿Qué técnicas de reducción de dimensionalidad existen?**
?
![[#Técnicas de reducción de dimensionalidad]]
