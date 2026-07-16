---
type: concept
tags:
  - llms
  - metrics
  - review
---

## Definición

Los **sesgos en LLM judges** son patrones sistemáticos que hacen que un juez automático favorezca ciertas respuestas por razones distintas a la calidad real.

Aparecen dentro de *[[AI as a judge]]* porque el juez también es un modelo probabilístico con preferencias aprendidas, sensibilidad al *prompt* y limitaciones de razonamiento.

Estos sesgos no invalidan el uso de *LLM judges*, pero sí obligan a interpretar sus scores con cuidado.

## Sesgos comunes

### Self-bias

El juez puede favorecer respuestas generadas por el mismo modelo o por modelos parecidos.

La intuición es que una respuesta que el modelo tendería a generar también puede parecerle más probable o más natural al evaluarla.

Esto afecta especialmente a la autoevaluación o *self-critique*.

### Position bias

En [[Evaluación pairwise con LLM judge|comparación pairwise]], el juez puede favorecer la primera respuesta o una posición concreta.

Esto puede distorsionar rankings si siempre se presenta la respuesta A antes que la respuesta B.

Una mitigación simple es repetir la comparación invirtiendo el orden de las respuestas.

### Verbosity bias

El juez puede favorecer respuestas más largas aunque no sean mejores.

Una respuesta extensa puede parecer más completa, pero también puede contener relleno, errores o [[Alucinación en LLMs|alucinaciones]].

### Style bias

El juez puede premiar respuestas con tono seguro, estructura pulida o lenguaje convincente aunque la factualidad sea débil.

Esto es peligroso cuando se evalúan dominios donde la corrección importa más que la forma.

## Mitigación

Para reducir sesgos conviene:

- usar *prompts* y rúbricas explícitas
- separar criterios como factualidad, completitud, seguridad y estilo
- aleatorizar o invertir el orden en comparaciones *pairwise*
- calibrar contra evaluación humana
- comparar varios jueces cuando el coste lo permita
- auditar ejemplos donde el juez discrepa de métricas exactas o humanos
- pedir explicaciones, pero no tratarlas como prueba definitiva

La mitigación no elimina todos los sesgos, pero hace más visible cuándo el juez falla.

## Relación con evaluación

Los sesgos importan porque los scores de un juez suelen usarse para tomar decisiones:

- comparar modelos
- aceptar o rechazar respuestas en producción
- seleccionar datos para *[[Preference Finetuning|preference finetuning]]*
- elegir candidatos en *[[Test-time compute|test-time compute]]*
- monitorizar regresiones

Si el juez tiene sesgo de longitud, por ejemplo, una optimización basada en su puntuación puede empujar al sistema a generar respuestas cada vez más largas sin mejorar calidad real.

## Preguntas

#flashcards/llms #flashcards/metrics 

**¿Qué son los sesgos en *LLM judges*?**
?
![[#Definición]]

**¿Qué es el *self-bias* en un *LLM judge*?**
?
![[#Self-bias]]

**¿Qué es el *position bias* en evaluación *pairwise*?**
?
![[#Position bias]]

**¿Qué es el *verbosity bias*?**
?
![[#Verbosity bias]]

**¿Cómo se pueden mitigar sesgos en *LLM judges*?**
?
![[#Mitigación]]

**¿Cómo se relacionan los sesgos con la evaluación de tipo *AI as a judge*?**
?
![[#Relación con evaluación]]
