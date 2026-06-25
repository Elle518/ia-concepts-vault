---
type: concept
tags:
  - llms
  - nlp
  - review
---

## Definición

Las **penalizaciones por repetición** son [[Parámetros de decoding|parámetros de decoding]] que reducen la probabilidad de que un [[Modelo del lenguaje|modelo de lenguaje]] repita tokens, palabras, frases o temas durante la generación.

No cambian el conocimiento del modelo ni sus pesos. Modifican la distribución de probabilidad durante el *decoding* para hacer menos probable que el modelo siga insistiendo en lo que ya ha generado.

## Utilidad

La idea es evitar que el modelo "se quede atascado" repitiendo lo mismo.

Por ejemplo, si un modelo empieza a generar una lista y repite varias veces una palabra, una penalización por repetición puede hacer que esa palabra sea menos atractiva en los siguientes pasos.

Esto puede ayudar en generación larga, escritura creativa, *brainstorming* o respuestas donde queremos más variedad. Pero si se aplica demasiado fuerte, puede hacer que el texto sea menos natural o que evite repetir términos que sí debería repetir.

## Tipos de penalizaciones por repetición

En cada paso de generación, el modelo produce *[[Logit|logits]]* para los posibles siguientes tokens. Las penalizaciones por repetición modifican esos *logits* antes de aplicar el muestreo.

Dos variantes comunes son:

- **Frequency penalty**. Penaliza más los tokens cuanto más veces han aparecido. Si un token aparece muchas veces, su probabilidad se reduce más.
- **Presence penalty**. Penaliza los tokens que ya han aparecido al menos una vez, independientemente de cuántas veces hayan aparecido.

La diferencia importante es:

- *frequency penalty* responde a la **frecuencia**.
- *presence penalty* responde a la **presencia**.

Por eso, *frequency penalty* suele ser útil para reducir repeticiones literales. *Presence penalty* suele empujar al modelo a introducir temas o palabras nuevas.

Algunos frameworks también tienen un parámetro llamado *repetition penalty*, típico en modelos open-source, que penaliza tokens ya generados mediante una transformación directa sobre los *logits*.

## Errores comunes

- Pensar que una penalización alta siempre mejora la calidad. Puede hacer que el modelo evite términos necesarios.
- Usarlas para corregir falta de contexto, mala instrucción o mala recuperación en un sistema [[RAG]].
- Confundir *presence penalty* con *frequency penalty*. No penalizan exactamente lo mismo.
- Aplicarlas de forma agresiva en tareas donde la repetición es necesaria, como extracción, generación de JSON, código o respuestas con terminología técnica.
- Ajustarlas sin revisar otros parámetros como [[Temperatura]], [[Top-p sampling|top-p]], [[Top-k sampling|top-k]] o límites de longitud.

## Preguntas

#flashcards/llms #flashcards/nlp

**¿Qué son las penalizaciones por repetición en un LLM?**
?
![[#Definición]]

**¿Cuál es la utilidad de las penalizaciones por repetición?**
?
![[#Utilidad]]

**¿Qué diferencia hay entre *frequency penalty* y *presence penalty*?**
?
![[#Tipos de penalizaciones por repetición]]

**¿Cuándo puede ser útil una *frequency penalty*?**
?
Cuando queremos reducir repeticiones literales de tokens o palabras que aparecen demasiadas veces en la generación.

**¿Cuándo puede ser útil una *presence penalty*?**
?
Cuando queremos favorecer que el modelo introduzca información, temas o formulaciones nuevas en lugar de volver a tokens ya usados.

**¿Qué riesgos tiene usar penalizaciones por repetición demasiado altas?**
?
![[#Errores comunes]]
