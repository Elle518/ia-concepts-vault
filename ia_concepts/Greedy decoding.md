---
type: concept
tags:
  - llms
  - nlp
  - review
---

## Definición

***Greedy decoding*** es una estrategia de generación en la que un [[Modelo del lenguaje|modelo de lenguaje]] elige, en cada paso, el token con mayor probabilidad.

No hay muestreo aleatorio, sino que el modelo toma siempre la opción localmente más probable. Por eso suele producir respuestas más deterministas, pero también puede generar salidas menos diversas o quedarse atrapado en continuaciones pobres.

## Utilidad

La intuición es escoger siempre “la mejor opción inmediata”.

Esto puede funcionar bien cuando hay una respuesta claramente preferida o cuando se necesita consistencia. Sin embargo, elegir el token más probable en cada paso no garantiza que la secuencia completa sea la mejor posible.

En generación de texto, una decisión localmente buena puede cerrar caminos que habrían producido una respuesta globalmente mejor.

## Explicación técnica

En cada paso, el modelo calcula una distribución de probabilidad para el siguiente token:

$$P(x_t \mid x_{<t})$$

Con *greedy decoding*, se selecciona:

$$x_t = \arg\max_x P(x \mid x_{<t})$$

Después, ese token se añade al contexto y el proceso se repite hasta llegar a una condición de parada, como un token de fin, un límite de longitud o una regla del sistema.

Cuando la [[Temperatura|temperatura]] se acerca a 0, muchos sistemas se comportan de forma parecida a *greedy decoding*, aunque los detalles dependen de la implementación.

## Comparación con sampling

En estrategias como [[Top-k sampling|top-k sampling]] o [[Top-p sampling|top-p sampling]], el modelo conserva varios tokens candidatos y luego muestrea entre ellos. Eso introduce variedad.

En *greedy decoding*, solo se elige el token más probable. Esto reduce la variabilidad, pero puede hacer que la salida sea repetitiva, genérica o demasiado conservadora.

## Errores comunes

- Pensar que elegir siempre el token más probable produce la mejor respuesta global.
- Usarlo para tareas creativas donde conviene explorar alternativas.
- Confundir determinismo con corrección. Una respuesta puede ser estable y seguir siendo incorrecta.
- Asumir que equivale exactamente a temperatura 0 en cualquier API. La equivalencia depende de la implementación.

## Preguntas

#flashcards/llms #flashcards/nlp

**¿Qué es el *greedy decoding*?**
?
![[#Definición]]

**¿Cuál es la utilidad del *greedy decoding*?**
?
![[#Utilidad]]

**¿Cómo se calcula el *greedy decoding*?**
?
![[#Explicación técnica]]

**¿En qué se diferencia *greedy decoding* de las estrategias de *sampling*?**
?
![[#Comparación con sampling]]

**¿Qué errores comunes hay al usar *greedy decoding*?**
?
![[#Errores comunes]]
