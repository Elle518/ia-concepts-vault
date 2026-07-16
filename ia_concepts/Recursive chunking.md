---
type: concept
tags:
  - llms
  - nlp
  - review
---

## Definición

***Recursive chunking*** es una estrategia de *[[Chunking|chunking]]* que intenta dividir el texto usando separadores cada vez más pequeños hasta que los fragmentos tienen un tamaño aceptable.

Suele probar primero con secciones, luego párrafos, después frases y finalmente caracteres o tokens si no queda otra opción.

La idea es preservar unidades naturales de texto siempre que sea posible. En vez de cortar cada 500 tokens sin mirar el contenido, el algoritmo pregunta:

“¿Puedo cortar por una frontera lógica grande? Si no, ¿puedo cortar por una frontera más pequeña?”

Así evita romper párrafos o frases salvo cuando el fragmento sigue siendo demasiado largo.

Es una buena opción general para RAG porque equilibra simplicidad y respeto por la estructura del texto.

Funciona bien en documentación, artículos, páginas web limpias y notas con párrafos razonablemente organizados.

## Separadores

Un orden típico de separadores puede ser:

1. encabezados
2. líneas en blanco
3. saltos de línea
4. puntos o final de frase
5. espacios
6. caracteres

El algoritmo aplica el separador más amplio que permita mantener *chunks* dentro del tamaño objetivo.

## Limitaciones

No entiende realmente el significado del texto. Solo usa separadores.

Si el documento tiene estructura pobre, tablas complejas o contenido mezclado, puede generar chunks poco útiles.

También puede requerir reglas específicas por idioma, formato o tipo de documento.

## Preguntas

#flashcards/llms #flashcards/nlp

**¿Qué es *recursive chunking*?**
?
![[#Definición]]

**¿Qué separadores suele usar *recursive chunking*?**
?
![[#Separadores]]

**¿Qué limitaciones tiene *recursive chunking*?**
?
![[#Limitaciones]]
