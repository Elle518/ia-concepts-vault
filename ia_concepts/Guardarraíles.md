---
type: concept
tags:
  - llms
  - ml
  - review
---

## Definición

Los **guardarraíles** (*guardrails*) son mecanismos de control que limitan o filtran el comportamiento de un sistema con [[Modelo fundacional|modelos fundacionales]] para que sus respuestas cumplan restricciones de seguridad, calidad, formato o negocio.

Estas restricciones reducen las alucinaciones y las suposiciones. Pueden actuar antes, durante o después de la generación.

Ejemplo: «Responde utilizando únicamente la información proporcionada. Si desconoces la respuesta, di “no lo sé”. No especules».

Son como barandillas en un camino estrecho: no cambian el camino, pero reducen la probabilidad de que el sistema se salga de lo permitido.

## Utilidad

Los guardrails pueden implementarse como:

- validación de entrada
- filtrado de salida
- reglas de formato
- detección de contenido inseguro
- políticas de acceso a herramientas
- verificación de factualidad o *[[Grounding|grounding]]*

En sistemas reales suelen combinarse varios niveles de protección. No son una garantía absoluta, pero sí una capa importante para hacer el sistema más predecible y seguro.

## Errores comunes

- Pensar que un único filtro resuelve todos los riesgos.
- Usarlos solo como moderación de contenido y olvidar formato o herramientas.
- No probar casos límite.
- Suponer que los guardrarraíles sustituyen la evaluación.

## Preguntas

#flashcards/llms #flashcards/ml

**¿Qué son los guardarraíles en un sistema con LLMs?**
?
![[#Definición]]

**¿En qué momentos del flujo se pueden aplicar guardarraíles?**
?
![[#Utilidad]]

**¿Qué errores comunes se suelen cometer al usar guardarraíles?**
?
![[#Errores comunes]]

