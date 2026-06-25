---
type: concept
tags:
  - llms
  - nlp
  - review
---

## Definición

El ***few-shot prompting***  es una técnica de *[[Prompt engineering|prompt engineering]]* que consiste en incluir unos pocos ejemplos resueltos dentro del *prompt* para enseñar al [[Modelo del lenguaje|modelo de lenguaje]] cómo debe interpretar la tarea y cómo debe formatear la salida.

Estos ejemplos actúan como una guía local de comportamiento, sin necesidad de actualizar los pesos del modelo.

Los ejemplos reducen ambigüedad y hacen más probable que el modelo copie el patrón correcto.

## Utilidad

Se usa cuando los resultados del [[Zero-shot prompting|zero-shot prompting]] son inconsistentes, la tarea requiere un formato específico y/o se necesita una mayor precisión.

*Few-shot* ayuda especialmente en tareas como:

- clasificación
- extracción estructurada de información
- normalización de texto
- generación de un formateo consistente

La calidad de los ejemplos importa mucho. Deben ser representativos, coherentes entre sí y alineados con la salida que queremos. Si los ejemplos están mal elegidos, el modelo puede aprender el patrón equivocado.

## Errores comunes

Algunos errores comunes que se cometen en *few-shot prompting* son:

- Meter demasiados ejemplos y consumir contexto innecesariamente.
- Poner ejemplos inconsistentes.
- Elegir ejemplos demasiado fáciles o no representativos.
- Creer que más ejemplos siempre mejora el resultado.

## Preguntas

#flashcards/llms #flashcards/nlp

**¿Qué es *few-shot prompting*?**
?
![[#Definición]]

**¿Qué utilidad tiene el *few-shot prompting*??**
?
![[#Utilidad]]

**¿Qué errores se suelen cometer en *few-shot prompting*?**
?
![[#Errores comunes]]
