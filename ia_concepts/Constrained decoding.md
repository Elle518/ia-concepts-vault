---
type: concept
tags:
  - llms
  - nlp
  - review
---

## Definición

***Constrained decoding***, también llamado ***constrained sampling***, es una técnica de generación en la que el modelo solo puede elegir tokens que cumplan ciertas restricciones de formato o gramática.

En lugar de confiar únicamente en que el [[Modelo del lenguaje|modelo de lenguaje]] siga una instrucción, el sistema restringe el espacio de tokens válidos durante la generación.

La intuición es poner una barrera en el momento de escribir. Si el modelo debe producir JSON válido, no basta con pedirlo en el *prompt*, el decodificador puede impedir que elija tokens que romperían la estructura.

## Funcionamiento

En cada paso de generación, el modelo produce un vector de [[Logit|logits]], con un valor para cada token posible del vocabulario.

Con *constrained decoding*, antes de hacer [[Sampling|sampling]], el sistema filtra o enmascara los tokens que no cumplen la restricción actual. Después, el modelo solo puede muestrear entre los tokens válidos.

Por ejemplo, si se está generando JSON, la gramática decide qué tokens pueden aparecer después de `{`, después de una clave, después de `:` o dentro de un *string*. La restricción cambia en cada paso según el prefijo ya generado.

## Relación con structured outputs

[[Structured output prompting]] intenta obtener un formato concreto mediante instrucciones en el *prompt*.

*Constrained decoding* va un paso más allá ya que incorpora reglas externas al proceso de [[Parámetros de decoding|decoding]]. Esto puede aumentar mucho la tasa de salidas parseables, especialmente cuando la respuesta será consumida por código.

En producción suelen combinarse:

- *prompt* claro con el formato esperado
- *constrained decoding* si el proveedor o *framework* lo soporta
- validación posterior con parser, schema o reglas de negocio

## Limitaciones

La principal dificultad es que hace falta una gramática o conjunto de reglas que diga qué tokens son válidos en cada estado de la generación.

Esto no es trivial para formatos complejos. JSON, YAML, regex, CSV o lenguajes de programación pueden necesitar gramáticas distintas. Por eso *constrained decoding* es menos general que el *prompting* y solo funciona bien para formatos soportados por la herramienta o implementados por el equipo.

Además, la verificación de la gramática puede aumentar la [[Latencia|latencia]] y no garantiza que el contenido sea correcto. Puede garantizar que el JSON sea válido, pero no que los valores extraídos sean verdaderos.

## Cuándo usarlo

Es útil cuando:

- la salida debe ser parseada automáticamente
- se necesita JSON, XML, SQL, regex, CSV o código con estructura estricta
- un error de formato rompe el pipeline
- la validación posterior es cara o llega demasiado tarde
- se quiere reducir la probabilidad de texto extra fuera del formato

Es menos útil cuando la tarea es abierta, creativa o cuando no existe una gramática clara para definir salidas válidas.

## Errores comunes

- Confundir formato válido con respuesta correcta.
- Usarlo como sustituto completo de la validación posterior.
- Asumir que cualquier formato se puede restringir fácilmente.
- Ignorar el coste de latencia de verificar restricciones en cada paso.
- Pensar que *constrained decoding* mejora el conocimiento del modelo; solo restringe las salidas posibles.
- Intentar resolver con restricciones un problema que debería resolverse con mejores instrucciones, datos o evaluación.

## Preguntas

#flashcards/llms #flashcards/nlp 

**¿Qué es *constrained decoding* o *constrained sampling*?**
?
![[#Definición]]

**¿Cómo funciona técnicamente el *constrained decoding* durante la generación?**
?
![[#Funcionamiento]]

**¿En qué se diferencia *constrained decoding* de *structured output prompting*?**
?
![[#Relación con structured outputs]]

**¿Qué limitaciones tiene el *constrained decoding*?**
?
![[#Limitaciones]]

**¿Cuándo conviene usar *constrained decoding*?**
?
![[#Cuándo usarlo]]

**¿Qué errores comunes hay al usar *constrained decoding*?**
?
![[#Errores comunes]]
