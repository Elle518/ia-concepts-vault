---
type: concept
tags:
  - llms
  - nlp
  - review
---

## Definición

***ReAct prompting*** (*Reason + Act*) es una técnica de *[[Prompt engineering|prompt engineering]]* en la que el modelo alterna razonamiento con acciones, como llamar a una herramienta, consultar un buscador o usar un sistema de [[RAG]].

El objetivo es que el modelo no dependa solo de su conocimiento interno, sino que pueda obtener información externa y continuar razonando con las observaciones.

Es como resolver una tarea mirando datos cuando hace falta. Primero decides qué necesitas, luego consultas una fuente, observas el resultado y ajustas el siguiente paso.

## Funcionamiento

Un flujo ReAct típico sigue un bucle:

- **Thought**: el modelo decide qué necesita hacer
- **Act**: ejecuta una acción o herramienta
- **Observation**: recibe el resultado
- **Thought**: actualiza su razonamiento y continúa

## Utilidad

ReAct es útil cuando la respuesta requiere información actualizada, cálculos, llamadas a APIs, acceso a documentos o interacción con herramientas. Se diferencia de [[Chain of thought prompting|chain-of-thought]] en que CoT razona de forma interna y lineal, mientras que ReAct conecta razonamiento con acciones externas.

## Errores comunes

- Usarlo cuando no hay herramientas reales disponibles.
- No restringir qué acciones puede tomar el modelo.
- Tratar las observaciones de herramientas como si siempre fueran correctas.
- Exponer razonamiento interno al usuario cuando no aporta valor.

## Preguntas

#flashcards/llms #flashcards/nlp

**¿Qué es el *ReAct prompting*?**
?
![[#Definición]]

**¿Cuál es el flujo típico del *ReAct prompting*?**
?
![[#Funcionamiento]]

**¿Para qué sirve y en qué se diferencia *ReAct prompting* de *chain-of-thought prompting*?**
?
![[#Utilidad]]

**¿Qué errores comunes se suelen cometer en *ReAct prompting*?**
?
![[#Funcionamiento]]