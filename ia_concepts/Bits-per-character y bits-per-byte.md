---
type: concept
tags:
  - llms
  - metrics
  - nlp
  - review
---

## Definición

***Bits-per-character*** (**BPC**) y ***bits-per-byte*** (**BPB**) son métricas de [[Modelo del lenguaje|modelos del lenguaje]] que expresan la *[[Cross-entropy|cross-entropy]]* normalizada por carácter o por byte.

Sirven para medir cuántos bits necesita el modelo, en promedio, para representar el texto original.

Son útiles porque la *cross-entropy* por token no siempre es comparable entre modelos, ya que dos modelos pueden usar [[Tokenización|tokenizadores]] distintos y, por tanto, tener tokens de tamaños muy diferentes.

De este modo, si un modelo necesita 6 bits por token, ese número no dice mucho por sí solo si no sabemos qué es un token.

Un token podría ser una palabra, una subpalabra, un carácter o un [[Byte|byte]]. Por eso, BPC y BPB intentan llevar la métrica a una unidad más estable del texto original.

BPB suele ser más estandarizado que BPC porque los bytes son una unidad más cercana a cómo se almacena el texto en disco.

## Fórmula

Si la *cross-entropy* está medida en [[Bit|bits]] por token:

$$BPC = \frac{\text{bits por token}}{\text{caracteres por token}}$$

Por ejemplo, si un modelo tiene 6 bits por token y cada token contiene, de media, 2 caracteres:

$$BPC = \frac{6}{2} = 3$$

Para bytes:

$$BPB = \frac{\text{bits por token}}{\text{bytes por token}}$$

También puede calcularse desde BPC si sabemos cuántos bytes ocupa cada carácter en promedio:

$$BPB = \frac{BPC}{\text{bytes por carácter}}$$

## BPC frente a BPB

BPC normaliza por carácter, pero el concepto de “carácter” depende de la [[Enconding|codificación]] y del idioma.

Por ejemplo, en [[ASCII]] un carácter ocupa 7 bits, mientras que en [[UTF-8]] un carácter puede ocupar entre 1 y 4 bytes.

BPB evita parte de esa ambigüedad porque mide directamente cuántos bits necesita el modelo por byte del texto original.

Por eso, cuando se comparan modelos entrenados o evaluados con textos multilingües, codificaciones distintas o tokenizadores muy diferentes, BPB suele ser más comparable que BPC.

## Relación con compresión

La *cross-entropy* puede interpretarse como una medida de compresión: indica cuántos bits harían falta, idealmente, para codificar los datos usando las probabilidades del modelo.

Si un modelo tiene un BPB de 3.43, significa que puede representar cada byte original, que normalmente son 8 bits, usando unos 3.43 bits en promedio.

De forma aproximada, eso correspondería a comprimir el texto a:

$$\frac{3.43}{8} \approx 43\%$$

del tamaño original, ignorando *overheads* prácticos del sistema de compresión, es decir, toda aquella información adicional que el sistema de compresión necesita guardar y descomprimir los datos, aparte de los propios datos comprimidos.

## Errores comunes

- Comparar bits por token entre modelos con tokenizadores distintos.
- Tratar BPC como totalmente independiente de la codificación de caracteres.
- Olvidar que BPB mide bytes del texto original, no bytes de los tokens internos del modelo.
- Interpretar BPB como una tasa de compresión real sin considerar overheads, implementación y formato.
- Comparar BPC o BPB entre conjuntos de datos distintos sin tener en cuenta idioma, dominio y distribución del texto.

## Preguntas

#flashcards/llms #flashcards/metrics #flashcards/nlp

**¿Qué miden BPC y BPB?**
?
![[#Definición]]


**¿Cómo se calcula BPC?**
?
![[#Fórmula]]

**¿En qué se diferencian BPC y BPB?**
?
![[#BPC frente a BPB]]

**¿Qué relación tienen BPC y BPB con la compresión?**
?
![[#Relación con compresión]]

**¿Qué errores comunes aparecen al interpretar BPC o BPB?**
?
![[#Errores comunes]]
