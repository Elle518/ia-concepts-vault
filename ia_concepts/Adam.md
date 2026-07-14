---
type: concept
tags:
  - dl
  - review
---

## Definición

**Adam** (*Adaptive Moment Estimation*) es un [[Optimizador|optimizador]] muy usado en *[[Aprendizaje profundo|deep learning]]* que adapta el tamaño de actualización de cada [[Parámetro|parámetro]] usando información del [[Gradiente|gradiente]] reciente.

Combina dos ideas:

1. [[Momentum]], para suavizar la dirección de actualización.
2. [[Escalado adaptativo]], para ajustar el paso según la magnitud histórica de los gradientes.

La intuición es que Adam no usa el mismo paso para todos los pesos. Si un parámetro tiene gradientes muy variables, reduce o ajusta su actualización; si la dirección parece estable, puede avanzar con más confianza.

## Funcionamiento

Adam mantiene dos medias móviles por parámetro:

- el primer momento, que estima la media de los gradientes
- el segundo momento, que estima la media de los gradientes al cuadrado

Con estas estimaciones, actualiza cada parámetro usando un paso normalizado. Esto suele hacerlo más estable que [[SGD]] puro, especialmente en redes profundas, gradientes ruidosos o problemas con escalas distintas entre parámetros.

Sus hiperparámetros más comunes son el *[[Tasa de aprendizaje|learning rate]]*, $\beta_1$, $\beta_2$ y $\epsilon$.

De forma breve:

- el *learning rate* controla el tamaño global del paso de actualización
- $\beta_1$ controla cuánto peso se da al promedio histórico de los gradientes, parecido a [[Momentum|momentum]]
- $\beta_2$ controla cuánto peso se da al promedio histórico de los gradientes al cuadrado, usado para escalar cada parámetro
- $\epsilon$ es una constante pequeña que evita divisiones por cero y mejora la estabilidad numérica

## Cuándo usarlo

Adam suele ser una buena opción por defecto en entrenamiento de redes neuronales, prototipos, transformers y problemas donde queremos convergencia rápida sin ajustar demasiado el optimizador.

Aun así, no elimina la necesidad de elegir bien el *learning rate*, revisar la generalización y usar regularización cuando haga falta.

## Errores comunes

- Pensar que Adam siempre generaliza mejor que SGD.
- Usar el *learning rate* por defecto sin validarlo.
- Confundir Adam con [[AdamW]], que maneja mejor el *weight decay* desacoplado.
- Ignorar que una convergencia rápida puede llevar a [[Sobreajuste|sobreajuste]] si no se valida bien.

## Preguntas

#flashcards/dl

**¿Qué es Adam?**
?
![[#Definición]]

**¿Qué dos estadísticas mantiene Adam para actualizar parámetros?**
?
![[#Funcionamiento]]

**¿Cuándo suele ser útil Adam?**
?
![[#Cuándo usarlo]]

**¿Qué errores comunes hay al usar Adam?**
?
![[#Errores comunes]]
