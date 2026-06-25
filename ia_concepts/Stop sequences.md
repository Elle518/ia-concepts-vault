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
