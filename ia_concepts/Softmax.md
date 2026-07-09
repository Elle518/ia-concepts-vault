---
type: concept
tags:
  - ml
  - llms
  - review
---

## Definición

**Softmax** es una función que convierte un vector de *[[Logit|logits]]* en una distribución de probabilidad.

Se usa normalmente en clasificación multiclase y en [[Modelo del lenguaje|modelos de lenguaje]] para transformar las puntuaciones de cada token en probabilidades sobre el vocabulario.

Softmax toma puntuaciones arbitrarias y las convierte en probabilidades comparables.

Si un *logit* es mucho mayor que los demás, softmax le asignará una probabilidad alta. Si varios logits son parecidos, la probabilidad se reparte entre ellos.

## Cálculo de la softmax

Dado un vector de logits $x = [x_1, x_2, \dots, x_N]$, softmax calcula:

$$p_i = \text{softmax}(x_i) = \frac{\exp(x_i)}{\sum_j \exp(x_j)} = \frac{e^{x_i}}{\sum_j e^{x_j}}$$

El resultado tiene dos propiedades importantes:

- cada $p_i$ está entre 0 y 1
- la suma de todas las probabilidades es 1

La exponencial hace que diferencias pequeñas entre *logits* puedan convertirse en diferencias grandes de probabilidad. Por eso softmax no solo ordena clases, sino que define una distribución completa.

Una técnica de depuración común cuando se trabaja con un modelo de IA es observar las probabilidades que este modelo calcula para determinadas entradas. Si las probabilidades parecen aleatorias, el modelo no ha aprendido mucho.

## En modelos de lenguaje

En un LLM autorregresivo, el modelo produce un *logit* para cada token posible del vocabulario en cada paso de generación.

Después se aplica softmax para obtener:

$$P(x_t \mid x_{<t})$$

Es decir, la probabilidad de cada posible siguiente token dado el contexto anterior.

Antes de aplicar softmax, los *logits* pueden modificarse con parámetros de [[Parámetros de decoding|decoding]] como la [[Temperatura|temperatura]]. Después de la softmax, el sistema puede seleccionar el token con estrategias como *[[Greedy decoding|greedy decoding]]*, *[[Top-k sampling|top-k]]* o *[[Top-p sampling|top-p]]*.

## Estabilidad numérica

En una implementación real, softmax suele calcularse restando el máximo *logit* antes de aplicar la exponencial:

$$\text{softmax}(x_i) = \frac{\exp(x_i - \max(x))}{\sum_j \exp(x_j - \max(x))}$$

Esto no cambia el resultado matemático, pero evita *overflow* numérico cuando los *logits* son grandes.

Muchos proveedores de modelos devuelven probabilidades generadas por sus modelos como ***[[Logprobs|logprobs]]***.

## Errores comunes

- Confundir softmax con una decisión final. Softmax da probabilidades, la selección de clase o token viene después.
- Aplicar softmax antes de una función de pérdida que ya espera *logits*.
- Interpretar la probabilidad de softmax como confianza perfectamente calibrada.
- Olvidar que softmax fuerza que todas las clases compitan entre sí, por eso no es ideal para clasificación multilabel.
- Pensar que softmax corrige un mal modelo, cuando solo normaliza sus puntuaciones.

## Preguntas

#flashcards/ml #flashcards/llms

**¿Qué es softmax?**
?
![[#Definición]]

**¿Cómo se calcula la salida de la softmax?**
?
![[#Cálculo de la softmax]]

**¿Para qué se usa softmax en un modelo de lenguaje?**
?
![[#En modelos de lenguaje]]

**¿Por qué se resta el máximo *logit* al implementar softmax?**
?
![[#Estabilidad numérica]]

**¿Qué errores comunes aparecen al usar softmax?**
?
![[#Errores comunes]]
