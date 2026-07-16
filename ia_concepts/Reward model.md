---
type: concept
tags:
  - llms
  - metrics
  - review
---

## Definición

Un ***reward model*** es un modelo que puntúa la calidad de una respuesta o acción según una señal de preferencia.

En LLMs, se usa a menudo dentro de [[RLHF]] para aproximar qué respuestas preferirían los humanos.

La intuición es entrenar un juez: en vez de pedirle que escriba la respuesta, le pedimos que estime qué respuesta es mejor.

## Entrenamiento

Un *reward model* suele entrenarse con comparaciones humanas.

Para un mismo *prompt* se generan varias respuestas y los anotadores eligen cuál prefieren. Esto produce datos del tipo:

```text
prompt, respuesta_ganadora, respuesta_perdedora
```

El modelo aprende a asignar mayor puntuación a las respuestas preferidas.

## Uso

Una vez entrenado, el *reward model* puede:

- guiar [[Proximal Policy Optimization|PPO]] en [[RLHF]]
- comparar candidatos en *[[Test-time compute|test-time compute]]*
- servir como evaluador automático aproximado
- ayudar a filtrar respuestas de baja calidad

No mide verdad de forma perfecta. Mide lo que aprendió de las preferencias y criterios usados durante el entrenamiento.

## Limitaciones

- Puede aprender sesgos de los anotadores.
- Puede premiar respuestas convincentes pero incorrectas.
- Puede ser explotado si el generador aprende atajos para maximizar la puntuación.
- Las comparaciones humanas pueden ser inconsistentes.

## Preguntas

#flashcards/llms #flashcards/metrics 

**¿Qué es un *reward model*?**
?
![[#Definición]]

**¿Cómo se entrena normalmente un *reward model*?**
?
![[#Entrenamiento]]

**¿Para qué se usa un *reward model* en LLMs?**
?
![[#Uso]]

**¿Qué limitaciones tiene un *reward model*?**
?
![[#Limitaciones]]
