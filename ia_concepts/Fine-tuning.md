---
type: concept
tags:
  - ml
  - llms
  - review
---

## Definición

El ***fine-tuning*** o ajuste fino es el proceso de continuar entrenando un modelo previamente entrenado usando datos más específicos.

En vez de empezar desde cero, se parte de pesos ya aprendidos durante el *[[Pre-training|pre-training]]* y se ajustan para una tarea, dominio, formato de salida o comportamiento concreto.

*Pre-training* enseña al modelo capacidades generales. *Fine-tuning* lo especializa.

Dado que el modelo ya cuenta con cierto conocimiento adquirido durante el preentrenamiento, el *fine-tuning* generalmente requiere menos recursos (por ejemplo, datos y capacidad de procesamiento) que el preentrenamiento.

Es parecido a tomar una persona con formación general y entrenarla para seguir un procedimiento específico de una empresa.

## Cuándo usarlo

El *fine-tuning* puede tener sentido cuando:

- hay muchos ejemplos representativos de la tarea
- el formato de salida debe ser muy consistente
- el comportamiento deseado no se consigue bien con *[[Prompt engineering|prompting]]*
- se quiere reducir latencia o coste usando *prompts* más cortos
- se necesita adaptar el modelo a un dominio específico

No suele ser la primera opción si el problema se puede resolver con *prompting*, [[RAG]] o mejores datos de contexto.

## Salida estructurada

Ajustar un modelo con ejemplos que siguen el formato deseado de salida es el enfoque más eficaz para lograr que los modelos generen resultados en este formato (entrenar un modelo desde cero con datos siguiendo el formato deseado también funciona). Si bien un simple ajuste no garantiza que el modelo siempre generará el formato esperado, es mucho más fiable que el *prompting* .

Para determinadas tareas, podemos garantizar el formato de salida modificando la arquitectura del modelo antes del ajuste fino. Por ejemplo, para clasificación, se puede agregar una cabeza de clasificación a la arquitectura del modelo base. Este enfoque también se denomina **[[Feature-based transfer|transferencia basada en características]]**.

Durante el ajuste fino, se puede volver a entrenar todo el modelo o parte del modelo, como la cabeza de clasificación. El entrenamiento del modelo completo requiere más recursos, pero da un mejor rendimiento.

Necesitamos técnicas para resultados estructurados ya que en principio el modelo, por sí solo, no es capaz de generar resultados estructurados. Sin embargo, a medida que los modelos se vuelven más potentes, podemos esperar que mejoren en el seguimiento de estas instrucciones.

## Trade-offs

*Fine-tuning* puede mejorar calidad, consistencia y coste de inferencia, pero introduce complejidad operativa: preparación de datos, entrenamiento, evaluación, versionado y monitorización.

También puede degradar capacidades generales si los datos son pobres, sesgados o demasiado estrechos.

## Preguntas

#flashcards/ml #flashcards/llms

**¿Qué es el *fine-tuning*?**
?
![[#Definición]]

**¿Cuándo tiene sentido usar *fine-tuning*?**
?
![[#Cuándo usarlo]]

**¿Qué *trade-offs* introduce el *fine-tuning*?**
?
![[#Trade-offs]]
