---
type: concept
tags:
  - llms
  - nlp
  - review
---

## Definición

El ***structured output prompting*** es una técnica de [[Prompt engineering|prompting]] que consiste en diseñar *prompts* para que un [[Modelo del lenguaje|modelo de lenguaje]] devuelva la respuesta en un formato estructurado, como JSON, XML, HTML, Markdown, tabular o una lista con campos fijos.

Es una práctica clave cuando la salida del modelo será consumida por código o por otro componente del sistema.

No basta con pedir "extrae la información". Hay que decir qué campos queremos, cómo se llaman y qué debe pasar si un dato falta.

El que un modelo pueda seguir esta instrucción depende de la capacidad del modelo para seguir instrucciones y de la claridad de la instrucción.

Para aumentar el porcentaje de resultados válidos, algunas personas utilizan la IA para validar y/o corregir el resultado del mensaje original. Esto significa que para cada resultado, habrá al menos dos consultas de modelo: una para generar el resultado y otra para validarlo. Si bien la capa de validación agregada puede mejorar significativamente la validez de los resultados, el costo adicional y la latencia incurridos por las consultas de validación adicionales pueden hacer que este enfoque sea demasiado costoso para algunos.

## Funcionamiento

Un prompt para salida estructurada suele especificar:

- campos exactos
- tipos de datos esperados
- formato de salida
- reglas para valores ausentes
- prohibición de texto extra fuera del formato

Ejemplo:

```text
Devuelve solo JSON válido con las claves: name, email, phone.
Si un campo no aparece, usa null.
No incluyas explicaciones.
```

En producción conviene combinar el *prompting* con una validación posterior  base de esquemas, parsers o [[Constrained decoding|constrained decoding]] cuando estén disponibles.

## Errores comunes

- Confiar solo en el *prompt* y no validar la salida.
- No definir qué hacer con campos ausentes o ambiguos.
- Permitir explicaciones extra que rompen el parser.
- Pedir un formato demasiado complejo para una única respuesta.

## Preguntas

#flashcards/llms #flashcards/nlp

**¿Qué es *structured output prompting*?**
?
![[#Definición]]

**¿Qué debe especificar un *prompt* para obtener una salida estructurada?**
?
![[#Funcionamiento]]

**¿Qué errores comunes se suelen cometer al estructurar la salida de un LLM?**
?
![[#Errores comunes]]
