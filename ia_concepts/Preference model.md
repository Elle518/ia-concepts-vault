---
type: concept
tags:
  - llms
  - metrics
  - review
---

## Definición

Un ***preference model*** es un modelo especializado que predice qué respuesta preferiría un usuario o evaluador entre varias candidatas.

Normalmente recibe un input y dos respuestas, y devuelve cuál de las dos es mejor para ese input.

Es una forma especializada de [[AI as a judge]] y está relacionada con [[Evaluación pairwise con LLM judge|evaluación pairwise]].

Comparar dos respuestas suele ser más fácil que asignar una puntuación absoluta.

Un *preference model* aprende ese juicio comparativo: dadas dos salidas posibles, estima cuál se ajusta mejor a las preferencias humanas o a una rúbrica concreta.

Esto permite automatizar parte de la evaluación y generar señales útiles para alinear modelos.

## Datos de entrenamiento

Los datos suelen tener el formato:

```text
prompt, chosen_response, rejected_response
```

La respuesta `chosen` es la preferida y `rejected` es la menos preferida.

Estos datos pueden venir de humanos, de usuarios, de expertos o de otro juez automático, aunque la calidad de la señal afecta directamente al modelo.

## Uso

Un preference model puede usarse para:

- comparar modelos o *prompts*
- construir rankings de respuestas
- seleccionar candidatos en *[[Test-time compute|test-time compute]]*
- generar señales para *[[Preference Finetuning|preference finetuning]]*
- filtrar respuestas antes de mostrarlas a usuarios

También puede servir como alternativa especializada a un juez generalista grande cuando el criterio de preferencia está bien definido.

## Relación con reward model

Un *[[Reward model|reward model]]* suele asignar una puntuación a una respuesta.

Un *preference model* se centra en elegir entre respuestas candidatas.

En la práctica, ambos conceptos están muy relacionados: muchos *reward models* se entrenan con datos de preferencias y luego producen *scores* que permiten comparar respuestas.

## Limitaciones

- Aprende las preferencias presentes en los datos, incluidos sesgos e inconsistencias.
- No garantiza factualidad si los datos de preferencia no la penalizan.
- Puede favorecer estilo, longitud o tono sobre calidad real.
- Puede degradarse fuera del dominio para el que fue entrenado.
- Si se usa para optimizar modelos, puede ser explotado por el generador.

## Preguntas

#flashcards/llms #flashcards/metrics

**¿Qué es un *preference model*?**
?
![[#Definición]]

**¿Qué formato suelen tener los datos de entrenamiento de un *preference model*?**
?
![[#Datos de entrenamiento]]

**¿Para qué se usa un *preference model*?**
?
![[#Uso]]

**¿Qué relación hay entre un *preference model* y un *reward model*?**
?
![[#Relación con reward model]]

**¿Cuáles suelen ser las limitaciones de un *preference model*?**
?
![[#Limitaciones]]
