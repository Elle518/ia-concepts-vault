---
type: concept
tags:
  - llms
  - metrics
  - review
---

## Definición

***AI as a judge*** o ***LLM as a judge*** consiste en usar un modelo de IA para evaluar respuestas generadas por otro modelo o sistema.

Un ***AI judge*** no es solo el modelo: es el sistema formado por el modelo, el *prompt*, los criterios, la escala de puntuación y los parámetros de generación.

Es una forma de [[Evaluación subjetiva en LLMs|evaluación subjetiva]] porque el resultado depende del juez usado. Cambiar el modelo, el *prompt* o los [[Parámetros de decoding|parámetros de decoding]] puede producir otro juez distinto.

Se usa cuando la calidad de una respuesta abierta no puede medirse bien con una regla exacta, como ocurre con utilidad, claridad, factualidad, toxicidad, repetición o [[Alucinación en LLMs|alucinaciones]].

Evaluar respuestas abiertas es difícil porque muchas veces no existe una única respuesta correcta.

En vez de pedir a humanos que revisen todo, se puede pedir a otro modelo que actúe como evaluador.

La ventaja es que el juez puede ser rápido, barato (o al menos más barato que la evaluación humana) y escalable. Además puede explicar su decisión, lo que ayuda a auditar resultados.

La trampa es que no estamos midiendo una verdad objetiva: estamos midiendo lo que ese juez, con ese *prompt*, interpreta como bueno.

## Funcionamiento

El juez recibe información como:

- el input original
- una o varias respuestas candidatas
- instrucciones de evaluación
- una [[Evaluación con rúbrica|rúbrica]] o criterios
- opcionalmente, una respuesta de referencia

Después devuelve una puntuación, una preferencia, una etiqueta o una explicación.

Un mismo modelo puede comportarse como jueces distintos si se cambia:

- el prompt del juez
- el modelo base
- la escala de puntiación
- la temperatura u otros parámetros de *sampling*
- el orden de las respuestas en una comparación

Por eso conviene versionar el juez como si fuera parte del sistema de evaluación.

## Formas de uso

Hay tres patrones comunes.

### Evaluación pointwise

El juez evalúa una respuesta por sí sola, dado el input original.

Por ejemplo, puede puntuar de 1 a 5 si una respuesta es útil, correcta o segura.

Es el caso de [[Evaluación pointwise con LLM judge]].

### Evaluación reference-based

El juez compara una respuesta generada contra una o varias respuestas de referencia.

Puede usarse cuando hay una respuesta esperada, pero una métrica exacta como [[Exact match]] sería demasiado rígida.

Está relacionada con [[Evaluación por referencia]].

### Evaluación pairwise

El juez compara dos respuestas para el mismo input y decide cuál es mejor.

Este formato suele ser más estable que pedir puntuaciones absolutas y es útil para ranking, [[Test-time compute|test-time compute]] y generación de datos de preferencia.

Es el caso de [[Evaluación pairwise con LLM judge]].

## Diseño del prompt del juez

Un buen *prompt* para un *AI judge* debería especificar:

- la tarea exacta del juez
- los criterios de evaluación
- qué información debe priorizar
- la escala de salida
- el formato de respuesta esperado
- ejemplos calibrados, si se usa una escala

Los criterios deben ser concretos. No es lo mismo pedir “evalúa si la respuesta es buena” que pedir “evalúa si la respuesta responde a la pregunta usando la información del contexto sin añadir afirmaciones no respaldadas”.

Si la salida esperada es una puntuación de 1 a 5, conviene incluir ejemplos de qué significa cada nivel.

## Escalas de scoring

Los LLMs suelen comportarse mejor con etiquetas que con números.

Orden típico de estabilidad:

1. clasificación, como `correcto` / `incorrecto`
2. escala discreta corta, como 1 a 5
3. *score* continuo, como 0.0 a 1.0

Las escalas discretas muy amplias suelen ser menos fiables. En la práctica, una escala de 1 a 5 es más manejable que una de 1 a 100.

Cuando sea posible, conviene convertir criterios vagos en clases bien definidas.

## Ventajas

- Escala mejor que evaluación humana.
- Es más barata y rápida que revisar manualmente todas las respuestas.
- Puede funcionar sin datos de referencia.
- Permite evaluar tareas abiertas como utilidad, claridad, tono, factualidad o seguridad.
- Puede adaptarse a criterios nuevos cambiando el *prompt* o la rúbrica.
- Puede generar explicaciones útiles para auditar resultados.
- Es útil para detectar regresiones durante experimentación y monitorización.

## Limitaciones

*AI as a judge* no debería tratarse como una métrica objetiva y universal.

Sus principales limitaciones son:

- **Inconsistencia**: el mismo juez puede producir resultados distintos si cambian *prompt*, modelo, orden o *sampling*.
- **Ambigüedad de criterios**: dos herramientas pueden tener una métrica llamada `faithfulness`, pero con *prompts* y escalas distintas.
- **Coste y latencia**: evaluar con un modelo puede duplicar o multiplicar llamadas si hay varios criterios.
- **[[Sesgos en LLM judges|Sesgos]]**: puede favorecer sus propias respuestas, la primera respuesta, respuestas más largas o estilos concretos.
- **Privacidad e IP**: usar un juez propietario puede implicar enviar datos sensibles a un proveedor externo.
- **Falsa confianza**: una explicación convincente del juez no garantiza que el juicio sea correcto.

Para reducir coste se puede usar *spot-checking*, es decir, evaluar solo una muestra de respuestas. Aumentar el porcentaje evaluado da más confianza, pero también aumenta el coste.

## Juez fuerte, débil o autoevaluación

El juez puede ser más fuerte, más débil o el mismo modelo que genera la respuesta.

Un juez más fuerte suele correlacionar mejor con preferencias humanas, pero puede ser caro o lento. Una arquitectura práctica es generar con un modelo barato y evaluar una muestra con un modelo más fuerte.

Un juez más débil puede ser suficiente si la tarea de juzgar es más fácil que la de generar, especialmente si está especializado.

La autoevaluación o *self-critique* puede servir como *sanity check* o como mecanismo para revisar una respuesta antes de entregarla. Aun así, sufre *[[Sesgos en LLM judges|self-bias]]* y no debe ser la única fuente de evaluación.

## Jueces especializados

Además de jueces generalistas, se pueden construir jueces especializados para un criterio y una escala concretos.

Ejemplos:

- [[Reward model]]: puntúa un par `(prompt, response)` según preferencias aprendidas.
- [[Evaluación por referencia|Reference-based judge]]: compara una respuesta generada contra una referencia.
- [[Preference model]]: elige qué respuesta es preferible entre dos candidatas.

Un juez pequeño y especializado puede ser más fiable que un modelo generalista grande para una evaluación concreta.

## Buenas prácticas

- Versionar el modelo, *prompt*, criterios, escala y parámetros del juez.
- Mantener fija la definición de la métrica para poder comparar experimentos.
- Calibrar el juez contra humanos o ejemplos etiquetados.
- Usar ejemplos en el *prompt* cuando haya escala numérica.
- Preferir clasificación o escalas discretas cortas cuando sea suficiente.
- Repetir comparaciones *pairwise* cambiando el orden para detectar position bias.
- Combinar AI judges con [[Evaluación exacta en LLMs|métricas exactas]] y evaluación humana cuando el riesgo sea alto.

## Errores comunes

- Comparar *scores* de jueces distintos como si midieran lo mismo.
- No guardar el *prompt* exacto del juez.
- Usar *scores* numéricos continuos sin calibración.
- Evaluar solo la calidad global cuando hacen falta criterios separados.
- Usar un juez en producción sin medir coste, latencia y falsos negativos.
- Asumir que un juez potente no tiene sesgos.
- Usar siempre el mismo orden en comparaciones *pairwise*.
- Interpretar una explicación convincente del juez como garantía de corrección.
- No revisar ejemplos concretos detrás de un cambio agregado en el *score*.
- Optimizar el sistema solo contra el juez sin evaluación humana o exacta.

## Preguntas

#flashcards/llms #flashcards/metrics 

**¿Qué es *AI as a judge*?**
?
![[#Definición]]

**¿Cómo funciona un LLM *judge*?**
?
![[#Funcionamiento]]

**¿Qué tres formas comunes de uso tiene *AI as a judge*?**
?
![[#Formas de uso]]

**¿Qué debería especificar el *prompt* de un *AI as a judge*?**
?
![[#Diseño del prompt del juez]]

**¿Qué escalas de *scoring* suelen ser más estables para LLM judges?**
?
![[#Escalas de scoring]]

**¿Qué ventajas tiene *AI as a judge*?**
?
![[#Ventajas]]

**¿Qué limitaciones tiene *AI as a judge*?**
?
![[#Limitaciones]]

**¿Qué diferencia hay entre un juez fuerte, un juez débil y la autoevaluación en *AI as a judge*?**
?
![[#Juez fuerte, débil o autoevaluación]]

**¿Qué buenas prácticas conviene seguir al usar *AI as a judge*?**
?
![[#Buenas prácticas]]

**¿Qué errores se suele cometer al usar *AI as a judge*?**
?
![[#Errores comunes]]
