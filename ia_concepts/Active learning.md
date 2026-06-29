---
type: concept
tags:
  - ml
  - review
---

## Definición

El ***active learning*** es una estrategia de *[[Aprendizaje automático|machine learning]]* en la que el modelo decide qué ejemplos no etiquetados conviene enviar a un humano para que los etiquete.

La idea es usar el presupuesto de etiquetado en los ejemplos más informativos, en vez de etiquetar datos al azar.

Es especialmente útil cuando hay muchos datos sin etiquetar y conseguir etiquetas es caro, lento o requiere expertos.

No tiene sentido gastar esfuerzo humano etiquetando ejemplos que el modelo ya clasifica con mucha confianza. Es mejor pedir etiquetas para los casos donde el modelo duda, donde varios modelos discrepan o donde faltan ejemplos representativos.

El *active learning* intenta maximizar el valor de cada etiqueta humana.

## Funcionamiento

El ciclo básico de active learning es:

1. Se parte de un pequeño conjunto de datos etiquetados.
2. Se entrena un modelo inicial.
3. El modelo evalúa un conjunto grande de datos no etiquetados.
4. Una *query strategy* selecciona los ejemplos más informativos.
5. Un humano, experto u *oracle* etiqueta esos ejemplos.
6. Los nuevos ejemplos etiquetados se incorporan al dataset de entrenamiento.
7. El modelo se reentrena o se actualiza.
8. El proceso se repite.

Este bucle puede mejorar el rendimiento con menos etiquetas que un enfoque supervisado clásico, siempre que la estrategia de selección sea buena y el proceso de etiquetado sea fiable.

## Conceptos clave

- **Unlabeled pool**: conjunto de datos todavía no etiquetados. ^ae8bac
- **Labeled data**: ejemplos ya etiquetados usados para entrenar el modelo.
- **Oracle**: persona, experto funcional o sistema fiable que proporciona la etiqueta. ^8dffa8
- **Query strategy**: criterio para decidir qué ejemplos se envían a etiquetar. ^296b3a
- **Labeling budget**: número máximo de ejemplos que podemos etiquetar por coste, tiempo o disponibilidad de expertos. ^34b770

## Estrategias de selección

### Uncertainty sampling

Selecciona los ejemplos donde el modelo tiene menor confianza.

En clasificación binaria, si el modelo predice probabilidades cercanas a 0.5, significa que no tiene clara la clase.

```python
uncertainty = np.abs(probas[:, 1] - 0.5)
uncertain_indices = np.argsort(uncertainty)[:n_samples]
```

Cuanto más cerca esté la probabilidad de 0.5, mayor incertidumbre.

### Margin sampling

Selecciona ejemplos donde la diferencia entre las dos clases más probables es pequeña.

Es útil en clasificación multiclase porque no basta con mirar solo la clase más probable: importa cuánto se separa de la segunda opción.

### Entropy sampling

Selecciona ejemplos con mayor entropía en la distribución de probabilidades.

Si el modelo reparte probabilidad entre muchas clases, la predicción es más incierta.

### Diversity sampling

Busca ejemplos diversos respecto a los ya etiquetados, para cubrir mejor el espacio de características.

Ayuda a evitar que el modelo pida muchas etiquetas de ejemplos parecidos entre sí.

### Query-by-committee

Entrena varios modelos y selecciona los ejemplos donde los modelos discrepan más.

La intuición es que un ejemplo es informativo si distintos modelos plausibles toman decisiones diferentes.

### Expected model change

Selecciona los ejemplos que provocarían mayor cambio en los parámetros del modelo si se etiquetaran.

Es una idea potente, pero puede ser más costosa de calcular.

### Expected error reduction

Selecciona los ejemplos que se espera que reduzcan más el error global del modelo.

También puede ser costosa porque intenta estimar el impacto futuro de etiquetar cada ejemplo.

### Random sampling

Selecciona ejemplos aleatoriamente.

No es una estrategia activa fuerte, pero sirve como *baseline* para comprobar si *active learning* aporta valor real.

## Evaluación

El *active learning* no se evalúa solo mirando el *[[Exactitud|accuracy]]* final, sino la relación entre rendimiento y número de etiquetas usadas.

Una forma habitual de evaluarlo es comparar curvas de aprendizaje:

- modelo entrenado con ejemplos seleccionados por *active learning*
- modelo entrenado con ejemplos seleccionados aleatoriamente

Si *active learning* funciona, debería alcanzar el mismo rendimiento con menos etiquetas o mayor rendimiento con el mismo presupuesto de etiquetado.

## Cuándo usarlo

Tiene sentido usar *active learning* cuando:

- hay muchos datos sin etiquetar
- etiquetar es caro
- hay acceso a un *oracle* fiable
- el modelo puede estimar incertidumbre razonablemente
- se puede reentrenar o actualizar el modelo de forma iterativa

No suele ser la mejor opción si las etiquetas son baratas, si no hay infraestructura de etiquetado o si el modelo está muy mal calibrado y selecciona ejemplos poco útiles.

## Errores comunes

- Pensar que seleccionar ejemplos inciertos siempre es mejor que seleccionar ejemplos representativos.
- No comparar contra *random sampling*.
- No controlar la calidad de las etiquetas humanas.
- Usar probabilidades del modelo como si estuvieran perfectamente calibradas.
- Sesgar el dataset hacia ejemplos raros, ambiguos o ruidosos.
- Ignorar el coste operativo: interfaz de anotación, revisión, versionado de datos y reentrenamiento.

## Preguntas

#flashcards/ml

**¿Qué es el *active learning*?**
?
![[#Definición]]

**¿Cuál es el ciclo básico de active learning?**
?
![[#Funcionamiento]]

**¿Qué es una *query strategy* en *active learning*?**
?
![[#^296b3a]]

**¿Qué es el *unlabeled pool* en *active learning*?**
?
![[#^ae8bac]]

**¿Qué es el *oracle* en *active learning*?**
?
![[#^8dffa8]]

**¿Qué es el *labeling budget* en *active learning*?**
?
![[#^34b770]]

**¿Qué estrategias de selección hay en *active learning*?**
?
![[#Estrategias de selección]]

**¿Cómo se evalúa si *active learning* está aportando valor?**
?
![[#Evaluación]]

**¿Cuándo es útil usar el *active learning*?**
?
![[#Cuándo usarlo]]

**¿Qué errores comunes aparecen al aplicar *active learning*?**
?
![[#Errores comunes]]
