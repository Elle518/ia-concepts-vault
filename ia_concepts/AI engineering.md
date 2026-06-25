---
type: concept
tags:
  - ml
  - review
---

## Definición

La **ingeniería de inteligencia artificial** (*artificial intelligence engineering*) se refiere al proceso de crear aplicaciones sobre [[Modelo fundacional|modelos fundacionales]].

Se han estado creando aplicaciones de IA durante más de una década, un proceso a menudo conocido como ingeniería de aprendizaje automático (*machine learning engineering*) o MLOps (abreviatura de *ML operations*).

Si la [[Ingeniería de aprendizaje automático|Ingeniería de aprendizaje automático]] tradicional implica el desarrollo de modelos de aprendizaje automático, la ingeniería de IA aprovecha los modelos existentes.

## ML engineering vs AI engineering

En términos generales, la creación de aplicaciones utilizando modelos fundacionales hoy en día difiere de la ingeniería de aprendizaje automático tradicional en tres aspectos principales:

1. Sin modelos base, es necesario entrenar modelos propios para las aplicaciones. Con la ingeniería de IA, se utiliza un modelo entrenado previamente. Esto significa que la ingeniería de IA se centra menos en el modelado y el entrenamiento, y más en la adaptación del modelo.
2. La ingeniería de IA trabaja con modelos más grandes, que consumen más recursos computacionales y presentan mayor latencia que la ingeniería de aprendizaje automático tradicional. Esto implica una mayor presión para optimizar el entrenamiento y la inferencia.
3. La ingeniería de IA trabaja con modelos que pueden generar resultados abiertos. Estos resultados ofrecen a los modelos la flexibilidad de usarse para más tareas, pero también dificultan su evaluación. Esto convierte la evaluación en un problema mucho mayor en la ingeniería de IA.

En resumen, la ingeniería de IA se diferencia de la ingeniería de ML en que se centra menos en el desarrollo de modelos y más en la adaptación y evaluación de los mismos.

## Adaptación de modelos

En general, las técnicas de adaptación de modelos se pueden dividir en dos categorías, según requieran o no actualizar los pesos del modelo:

- **Técnicas basadas en *prompts***, que incluyen el *[[Prompt engineering|prompt engineering]]*, adaptan un modelo sin actualizar sus pesos. La adaptación se realiza proporcionando instrucciones y contexto al modelo, en lugar de modificarlo directamente. El *prompt engineering* es más fácil de implementar y requiere menos datos. Permite experimentar con más modelos, sin embargo, puede no ser suficiente para tareas complejas o aplicaciones con requisitos de rendimiento estrictos. Dentro de este bloque entran técnicas como *[[Zero-shot prompting|zero-shot prompting]]*, *[[Few-shot prompting|few-shot prompting]]* y *[[Chain of thought prompting|chain-of-thought prompting]]*.
- **Técnicas de *fine-tuning***, que sí que requieren actualizar los pesos del modelo. La adaptación se realiza modificando el modelo directamente. En general, las técnicas de *[[Fine-tuning|fine-tuning]]* o ajuste fino son más complejas y requieren más datos, pero pueden mejorar significativamente la calidad, la latencia y el coste del modelo. Muchas cosas no son posibles sin modificar los pesos del modelo, como adaptarlo a una nueva tarea a la que no se expuso durante el entrenamiento.

## Preguntas

#flashcards/ml

**¿Qué se entiende por *AI engineering*?**
?
![[#Definición]]

**¿En qué se diferencian *AI engineering* y *ML engineering*?**
?
![[#ML engineering vs AI engineering]]

**¿Qué técnicas de adaptación de modelos existen en *AI engineering*?**
?
![[#Adaptación de modelos]]
