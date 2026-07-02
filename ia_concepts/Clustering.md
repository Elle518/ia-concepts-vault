---
type: concept
tags:
  - ml
  - review
---

## Definición

El **clustering** es una tarea de [[Aprendizaje no supervisado|aprendizaje no supervisado]] que agrupa ejemplos similares entre sí sin usar etiquetas previas. Los algoritmos de clustering definen una noción de similitud o distancia entre puntos y buscan particiones coherentes del dataset.

Se usa para descubrir segmentos, estructuras o patrones en los datos, como grupos de clientes con comportamientos parecidos.

Clusterizar es ordenar ejemplos por parecido cuando nadie nos ha dado las categorías.

Si tenemos datos de clientes, el algoritmo puede separar grupos con hábitos de compra similares aunque no sepamos de antemano qué segmentos existen.

## Modelos de clustering

Un ejemplo clásico es **[[k-Means|k-means]]**, que asigna cada punto al centroide más cercano y actualiza los centroides iterativamente. Otros métodos incluyen [[Clustering jerárquico|clustering jerárquico]] y [[DBSCAN]].

## Factores que afectan al clustering

El resultado depende mucho de la representación de las variables, el escalado, la métrica de distancia y los hiperparámetros. En k-means, por ejemplo, hay que elegir el número de clusters $k$.

## Preguntas

#flashcards/ml

**¿Qué es el clustering?**
?
![[#Definición]]

**¿Cuál modelos de clustering existen?**
?
![[#Modelos de clustering]]

**¿Qué factores afectan mucho al resultado de un clustering?**
?
![[#Factores que afectan al clustering]]
