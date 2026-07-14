---
type: concept
tags:
  - llms
  - metrics
  - nlp
  - review
---

## Definición

La ***perplexity*** o **perplejidad** es una métrica que mide lo bien que un [[Modelo del lenguaje|modelo de lenguaje]] predice una secuencia de texto. Cuanta más incertidumbre tenga el modelo a la hora de predecir lo que viene a continuación en un conjunto de datos determinado, mayor será la perplejidad.

De forma intuitiva, si la [[Cross-entropy|entropía cruzada]] mide qué tan difícil es para un modelo predecir el siguiente token, la *perplexity*, mide la cantidad de incertidumbre que tiene al predecir el siguiente [[Tokenización|token]]. Una mayor incertidumbre significa que hay más opciones posibles para el próximo token.

Cuanto más baja es la *perplexity*, mejor: significa que el modelo asigna mayor probabilidad al texto correcto y está menos “perplejo” ante la secuencia.

Por ejemplo, si un modelo tiene una *perplexity* de 10, puede interpretarse aproximadamente como que, en promedio, duda entre unas 10 opciones razonables en cada paso.

Si todos los tokens en un lenguaje hipotético tienen la misma probabilidad de suceder, una perplejidad de 3 significa que este modelo tiene una probabilidad de 1 entre 3 de predecir correctamente el siguiente token.

## Relación con cross-entropy

La *perplexity* es el exponencial de la *[[Cross-entropy|cross-entropy]]*.

Si la entropía o la *cross-entropy* se mide en [[Bit|bits]]:

$$PPL(P) = 2^{H(P)}$$

Para un modelo con distribución aprendida $Q$ evaluado sobre datos con distribución real $P$:

$$PPL(P,Q) = 2^{H(P,Q)}$$

Cada bit puede representar 2 valores únicos, de ahí la base de 2 en la ecuación de perplejidad anterior.

Si la *cross-entropy* se mide en [[Nat|nats]], como suele ocurrir en *frameworks* como PyTorch o TensorFlow porque usan logaritmo natural, la fórmula será:

$$PPL(P,Q) = e^{H(P,Q)}$$

 Una razón por la que se suele preferir el logaritmo natural al logaritmo de base 2 es porque el logaritmo natural tiene ciertas propiedades que facilitan los cálculos. Por ejemplo, la derivada del logaritmo natural $\ln(x)$ es $1/x$.

Por eso, cuando se reporta *perplexity*, hay que saber cómo se calculó la *cross-entropy* subyacente.

Por ejemplo, consideremos un modelo de lenguaje entrenado para codificar perfectamente los tokens de 4 posiciones. La entropía cruzada de este modelo de lenguaje es de 2 bits. Si este modelo de lenguaje intenta predecir una posición, tiene que elegir entre $2^2 = 4$ opciones posibles. Por tanto, este modelo de lenguaje tiene una perplejidad de 4.

## Fórmula en modelos de lenguaje

Para una secuencia de tokens $w_1, \dots, w_N$:

$$\text{PPL}(w_1, \dots, w_N) =
\exp\left(
-\frac{1}{N}
\sum_{i=1}^{N}
\log P(w_i \mid w_1, \dots, w_{i-1})
\right)$$

donde el modelo asigna una probabilidad al token correcto en cada posición.

Una menor *perplexity* implica que el modelo asigna mayor probabilidad media a los tokens reales.

## Qué afecta a la perplexity

Lo que cuenta como una buena *perplexity* depende del dataset, del tokenizador y de cómo se calcula la métrica.

En general:

- Los datos más estructurados suelen tener menor *perplexity* esperada, porque son más predecibles. HTML o código suelen ser más predecibles que texto en lenguaje natural.
- Un vocabulario mayor suele aumentar la *perplexity*, porque hay más tokens posibles entre los que elegir. Cuantos más tokens posibles haya, más difícil será para el modelo predecir el siguiente token.
- Para el mismo conjunto de datos, la perplejidad basada en caracteres (que predice el siguiente carácter) será menor que la perplejidad basada en palabras (que predice la siguiente palabra), porque la cantidad de caracteres posibles es menor que la cantidad de palabras posibles.
- Más contexto suele reducir la *perplexity*, porque el modelo tiene más información para predecir el siguiente token.
- La comparación entre modelos solo es limpia si se evalúan sobre el mismo dataset, con la misma tokenización o con una normalización comparable.

Por eso, no conviene comparar *perplexity* de forma aislada entre modelos con tokenizadores o [[Ventana de contexto|ventanas de contexto]] muy distintos.

## Usos prácticos

La *perplexity* es útil como indicador de la calidad probabilística de un modelo base, es decir, de sus capacidades. Si un modelo no predice bien el siguiente token, normalmente tampoco será fuerte como base para muchas tareas posteriores.

En general, los modelos más grandes, que también son modelos más potentes, consistentemente generan menor perplejidad en una variedad de conjuntos de datos.

También puede usarse para:

- Comparar modelos base sobre el mismo conjunto de datos.
- Detectar posible contaminación de datos en un *[[Benchmark|benchmark]]*, ya que si la *perplexity* sobre un *benchmark* es anormalmente baja, el modelo podría haber visto esos ejemplos durante el entrenamiento.
- Ayudar en deduplicación o filtrado de datos, ya que textos con *perplexity* muy baja pueden ser duplicados o memorizarse fácilmente y textos con *perplexity* muy alta pueden ser anómalos, ruidosos o estar fuera de distribución. Así, solo se agregan nuevos datos al conjunto de datos de entrenamiento existente solo si la perplejidad de los nuevos datos no es muy baja ni muy alta.
- Detectar texto anómalo o muy impredecible, ya que la perplejidad es máxima en el caso de textos impredecibles.

La *perplexity* está relacionada con otras métricas de modelado del lenguaje como [[Bits-per-character y bits-per-byte|BPC y BPB]].

## Limitaciones

La *perplexity* no siempre predice bien el rendimiento en tareas finales.

Después de técnicas de *[[Post-training|post-training]]* como [[Supervised finetuning|SFT]] o [[RLHF]], un modelo puede mejorar siguiendo instrucciones aunque su *perplexity* aumente.

Esto ocurre porque el objetivo deja de ser solo predecir el siguiente token de forma genérica y pasa a incluir comportamiento conversacional, preferencias humanas o formatos de respuesta.

También puede cambiar de forma inesperada con optimizaciones como [[Cuantización|cuantización]], cambios de tokenizador o restricciones de contexto.

## Errores comunes

- Pensar que una menor *perplexity* siempre implica mejor modelo para cualquier tarea.
- Comparar *perplexity* entre tokenizadores, datasets o vocabularios distintos sin cuidado.
- Olvidar si la *cross-entropy* base estaba medida en bits o en nats.
- Interpretar una *perplexity* baja como garantía de ausencia de *[[Sobreajuste|overfitting]]* o contaminación de datos.
- Usarla como única métrica para evaluar modelos *instruction-tuned* o alineados.

## Preguntas

#flashcards/llms #flashcards/nlp #flashcards/metrics

**¿Qué mide la *perplexity*?**
?
![[#Definición]]

**¿Cómo se relaciona la *perplexity* con la *cross-entropy*?**
?
![[#Relación con cross-entropy]]

**¿Cómo se calcula la *perplexity* en modelos de lenguaje?**
?
![[#Fórmula en modelos de lenguaje]]

**¿Qué factores afectan a la *perplexity*?**
?
![[#Qué afecta a la perplexity]]

**¿Para qué puede usarse la *perplexity* en AI engineering?**
?
![[#Usos prácticos]]

**¿Qué limitaciones tiene la *perplexity*?**
?
![[#Limitaciones]]

**¿Qué errores comunes aparecen al interpretar *perplexity*?**
?
![[#Errores comunes]]
