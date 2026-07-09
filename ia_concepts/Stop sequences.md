---
type: concept
tags:
  - llms
  - nlp
  - review
---

## Definición

Las ***stop sequences*** son secuencias de texto que indican a un [[Modelo del lenguaje|modelo de lenguaje]] cuándo debe detener la generación.

Son un [[Parámetros de decoding|parámetro de decoding]] usado para controlar el final de la salida. No hacen que el modelo razone mejor, pero ayudan a cortar la respuesta en el punto esperado.

## Utilidad

Un modelo de lenguaje autorregresivo genera secuencias de tokens generando un token tras otro. Una secuencia de salida larga requiere más tiempo, tiene más coste de computación (dinero) y, en ocasiones, puede molestar a los usuarios. Vamos a necesitar establecer una condición para que el modelo detenga la secuencia.

Un método sencillo es pedir a los modelos que dejen de generar después de una cantidad fija de tokens. La desventaja es que es probable que la salida se corte a mitad de la frase. Otro método es utilizar tokens de parada o palabras vacías, es decir, tokens de fin de secuencia. Las condiciones de parada son útiles para mantener bajos la latencia y los costos.

La desventaja de la detención anticipada es que si deseamos que los modelos generen resultados en un formato determinado, la detención prematura puede provocar que los resultados tengan un formato incorrecto. Por ejemplo, si le pedimos al modelo que genere JSON, una detención anticipada puede hacer que al JSON de salida le falten cosas como corchetes, lo que hace que el JSON generado sea difícil de analizar.

Una *stop sequence* funciona como una señal de "hasta aquí".

Por ejemplo, si queremos que el modelo genere solo la respuesta de un asistente y no continúe simulando al usuario, podemos usar una secuencia como `Usuario:` para detener la generación cuando aparezca.

También son útiles cuando esperamos un formato concreto: una sola respuesta, una sección, una línea o un bloque estructurado.

## Explicación técnica

Durante la generación, el sistema va acumulando los tokens producidos por el modelo. Si el texto generado contiene una de las *stop sequences* configuradas, la generación se detiene.

Por ejemplo, si la secuencia de parada es:

```text
### END
```

el sistema corta la generación cuando detecta esa cadena.

Las *stop sequences* no suelen modificar las probabilidades del modelo. A diferencia de [[Temperatura]], [[Top-p sampling|top-p]] o las [[Penalizaciones por repetición]], su función principal no es cambiar qué token es más probable, sino decidir cuándo parar.

En sistemas de producción, se usan para:

- Evitar que el modelo genere más secciones de las necesarias.
- Separar turnos en conversaciones.
- Cortar salidas antes de texto no deseado.
- Controlar formatos simples.
- Reducir coste y latencia evitando generaciones largas.

## Ejemplos comunes de stop sequences

|Stop sequence|Uso típico|Ejemplo de cuándo se detiene|
|---|---|---|
|`"\nUser:"`|Evitar que el modelo empiece a simular el siguiente turno del usuario.|Cuando genera `User:` después de su respuesta.|
|`"\nAssistant:"`|Evitar que el modelo continúe simulando otra respuesta del asistente.|Cuando intenta escribir otro bloque `Assistant:`.|
|`"###"`|Marcar el final de una sección o ejemplo.|Cuando llega a un separador `###`.|
|`"</answer>"`|Cortar respuestas estructuradas con etiquetas.|Cuando termina una respuesta tipo `<answer>...</answer>`.|
|`"END"`|Usar una marca explícita de finalización.|Cuando el modelo escribe `END`.|
|`"\n\n"`|Detener tras un párrafo o bloque corto.|Cuando genera una línea en blanco doble.|
|`"\nPregunta:"`|Evitar que genere un nuevo ejemplo o una nueva pregunta.|Cuando intenta continuar con otra `Pregunta:`.|

## Errores comunes

- Usar una *stop sequence* demasiado común, haciendo que la salida se corte antes de tiempo.
- Confiar solo en *stop sequences* para garantizar formatos complejos como JSON válido.
- Olvidar que la parada depende de cómo el sistema detecta la secuencia en el texto o en los tokens.
- Usarlas como sustituto de un buen prompt o de validación posterior.
- No probarlas con ejemplos reales donde la secuencia podría aparecer dentro del contenido legítimo.

## Preguntas

#flashcards/llms #flashcards/nlp

**¿Qué son las *stop sequences* en un LLM?**
?
![[#Definición]]

**¿Cuál es la utilidad detrás de una *stop sequence*?**
?
![[#Utilidad]]

**¿Cómo se usan las *stop sequences* en producción?**
?
![[#Explicación técnica]]

**¿Enumera algunos ejemplos comunes de *stop sequences*?**
?
![[#Ejemplos comunes de stop sequences]]

**¿Qué errores comunes hay al usar *stop sequences*?**
?
![[#Errores comunes]]
