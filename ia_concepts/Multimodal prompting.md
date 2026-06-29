---
type: concept
tags:
  - llms
  - nlp
  - review
---

## Definición

El ***multimodal prompting*** es una técnica de [[Prompt engineering|prompt engineering]] que consiste en dar al modelo más de un tipo de entrada, por ejemplo texto e imágenes, o texto y audio, cuando el sistema lo soporta.

El modelo combina la información de varias modalidades para producir una respuesta.

Es como enseñar una foto y hacer una pregunta sobre ella. La instrucción textual guía la tarea, pero la respuesta depende también de entender la imagen, el audio u otra señal.

## Utilidad

En un *prompt* multimodal se debe indicar claramente:

- qué entrada debe analizar el modelo
- qué información debe extraer
- qué formato de salida se espera
- qué partes debe ignorar si hay ruido

Ejemplo:

```text
Analiza la imagen del recibo y extrae la fecha, el comercio y el importe total.
Devuelve solo JSON válido.
```

Se usa en OCR asistido, análisis de documentos, inspección visual, extracción de datos de recibos, QA sobre imágenes y asistentes que combinan texto con media.

## Errores comunes

- Asumir que el modelo ve todos los detalles pequeños de una imagen.
- No especificar qué datos concretos debe extraer.
- Tratar una inferencia visual como si fuera una certeza.
- Olvidar que no todos los modelos aceptan las mismas modalidades.

## Preguntas

#flashcards/llms #flashcards/nlp

**¿Qué es *multimodal prompting*?**
?
![[#Definición]]

**¿Qué usos tiene el *multimodal prompting*?**
?
![[#Utilidad]]

**¿Qué se debe especificar en un *prompt* multimodal?**
?
![[#Utilidad]]

**¿Qué errores comunes se suelen cometer al usar *multimodal prompting* ?**
?
![[#Errores comunes]]
