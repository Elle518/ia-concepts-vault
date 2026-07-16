---
type: concept
tags:
  - llms
  - nlp
  - review
---

## Definición

***Structure-based chunking*** divide documentos respetando su estructura explícita.

Puede usar títulos, secciones, párrafos, listas, tablas, bloques de código, páginas o elementos HTML.

La intuición es que el formato del documento ya contiene pistas sobre dónde empieza y termina una unidad de significado.

Es especialmente útil en documentación técnica, manuales, wikis, documentos legales, *notebooks* y páginas con estructura clara.

También ayuda a conservar metadatos como título, sección, URL, página o jerarquía del documento.

## Funcionamiento

El sistema parsea el documento y corta por unidades estructurales.

Ejemplos:

- una sección Markdown con su título
- un bloque de código completo
- una tabla completa con su encabezado
- una página o apartado de un PDF
- un nodo HTML como `article`, `section` o `h2`

Si una unidad estructural es demasiado grande, se puede combinar con *[[Recursive chunking|recursive chunking]]*.


## Trade-offs

Ventajas:

- conserva contexto estructural
- evita romper tablas o código
- facilita añadir metadatos útiles para filtros
- mejora la interpretabilidad de los chunks recuperados

Limitaciones:

- depende de que el parser sea fiable
- puede fallar con PDFs mal extraídos
- algunas secciones pueden ser demasiado largas o demasiado cortas
- requiere reglas por formato de documento

## Preguntas

#flashcards/llms #flashcards/nlp

**¿Qué es *structure-based chunking*?**
?
![[#Definición]]

**¿Qué estructuras puede respetar esta estrategia?**
?
![[#Funcionamiento]]

**¿Qué ventajas y limitaciones tiene *structure-based chunking*?**
?
![[#Trade-offs]]
