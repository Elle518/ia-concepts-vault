---
type: concept
tags:
  - llms
  - nlp
  - review
---

## Definición

La **temperatura** (*temperature*) es un [[Parámetros de decoding|hiperparámetro de generación]] que controla cuánta aleatoriedad introduce un [[Modelo del lenguaje|modelo de lenguaje]] al elegir el siguiente token.

Una temperatura baja hace que el modelo tienda a escoger los tokens más probables, produciendo respuestas más deterministas y conservadoras. Una temperatura alta aplana la distribución de probabilidades, permitiendo que tokens menos probables tengan más opciones de ser elegidos, esto permite que los modelos generen respuestas más creativas.

## Utilidad

La temperatura funciona como un control de creatividad.

- Con temperatura baja, el modelo “se la juega poco”: elige casi siempre la continuación más probable. Esto suele ser útil para tareas donde queremos precisión, consistencia y formato estable, como extracción de información, clasificación o generación de código.
- Con temperatura alta, el modelo explora más opciones. Esto puede ayudar en *brainstorming*, escritura creativa o generación de alternativas, pero también aumenta el riesgo de respuestas incoherentes, incorrectas o menos reproducibles.

No existe una temperatura universalmente correcta. Depende de la tarea:

- Para respuestas factuales, extracción, clasificación o código, suelen funcionar mejor temperaturas bajas.
- Para redacción, generación de ideas o variantes creativas, puede tener sentido subir la temperatura.
- Para sistemas en producción, conviene evaluar la temperatura junto con métricas de calidad, consistencia y tasa de errores.

La temperatura no mejora el conocimiento del modelo ni corrige falta de contexto. Solo cambia cómo se muestrea la salida a partir de la distribución que el modelo ya ha producido.

## Explicación técnica

En un LLM autorregresivo, el modelo produce una puntuación o *[[Logit|logit]]* para cada token del vocabulario. Antes de muestrear el siguiente token, esos logits se transforman en probabilidades mediante [[Softmax|softmax]].

La temperatura modifica los *logits* antes de aplicar softmax:

$$p(x_i) = \text{softmax}(x_i​) = \frac{\exp(x_i / T)}{\sum_j \exp(x_j / T)}$$

donde $x_i$ es el *logit* del token $i$ y $T$ es la temperatura.

Cuando $T < 1$, las diferencias entre *logits* se amplifican. La distribución se vuelve más concentrada y los tokens más probables dominan todavía más.

Cuando $T = 1$, la temperatura no modifica la distribución de probabilidades original del modelo, es lo mismo que no usar temperatura. Los tokens se eligen según las probabilidades originales del modelo. $p_i ​= \text{softmax}(x_i​)$

Cuando $T > 1$, las diferencias entre *logits* se reducen. La distribución se vuelve más plana y aumenta la probabilidad de seleccionar tokens menos probables.

Cuando $T$ se acerca a 0, la generación se aproxima a elegir siempre el token de mayor probabilidad, algo parecido a *[[Greedy decoding|greedy decoding]]*.  Con $T = 0$ no hay muestreo real, se elige siempre el token más probable. Con $T = 1$ sí hay muestreo, los tokens se eligen según las probabilidades originales del modelo.

Es una práctica común establecer la temperatura en 0 para que los resultados del modelo sean más consistentes. Aunque técnicamente, la temperatura nunca puede ser 0, ya que los logits no se pueden dividir entre 0.

Los proveedores de modelos normalmente limitan la temperatura entre 0 y 2, pero se puede usar cualquier temperatura no negativa. A menudo se recomienda una temperatura de 0.7 para casos de uso creativos, ya que equilibra la creatividad y la previsibilidad, pero debemos experimentar y encontrar la temperatura que funcione mejor para nuestro caso de uso.

En la práctica, muchos sistemas usan temperatura junto con otros parámetros de *decoding* como [[Top-k sampling|top-k]], [[Top-p sampling|top-p]] o límites de longitud.

## Errores comunes

- Pensar que temperatura alta significa “mejor razonamiento”. En realidad, aumenta la aleatoriedad del muestreo.
- Usar temperatura alta en tareas donde la consistencia importa más que la variedad.
- Confundir temperatura con [[Fine-tuning|fine-tuning]] o [[Prompt engineering|prompt engineering]]. La temperatura no cambia los pesos del modelo ni la instrucción, solo afecta la generación.
- Asumir que temperatura 0 garantiza respuestas idénticas siempre. En algunos sistemas puede seguir habiendo pequeñas fuentes de no determinismo.
- Ajustar la temperatura sin revisar otros parámetros de decoding como *top-p*, *top-k* o penalizaciones por repetición.

## Preguntas

#flashcards/llms #flashcards/nlp

**¿Qué es la temperatura en un LLM?**
?
![[#Definición]]

**¿Cuál es la utilidad de la temperatura en un LLM?**
?
![[#Utilidad]]

**¿Cómo afecta una temperatura baja a la generación de texto? ¿Y alta?**
?
![[#Explicación técnica]]

**¿En qué tipo de tareas conviene usar temperaturas bajas? ¿Y altas?**
?
![[#Utilidad]]

**¿Qué errores comunes hay al ajustar la temperatura de un LLM?**
?
![[#Errores comunes]]
