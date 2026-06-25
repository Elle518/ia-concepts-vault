---
type: concept
tags:
  - llms
  - nlp
  - review
---

## Definición

El ***prompt engineering*** es la práctica de diseñar y ajustar las instrucciones, el contexto y el formato de salida que damos a un [[Modelo del lenguaje|modelo de lenguaje]] para obtener respuestas más útiles, correctas y consistentes.

No cambia los pesos del modelo. La adaptación ocurre en la entrada: qué le pedimos, cómo se lo pedimos, qué ejemplos le damos y qué restricciones imponemos.

Es como escribir un buen encargo para un colaborador muy capaz pero literal. Cuanto más clara sea la tarea, mejor delimitado esté el contexto y más explícito sea el formato esperado, menos margen habrá para respuestas ambiguas o inútiles.

## Definición de prompt

Un ***prompt*** es una instrucción, comando o pregunta que se escribe o dicta a una inteligencia artificial (como ChatGPT, Gemini, Copilot o DeepSeek) para que realice una tarea específica. Es el *input* o entrada que se utiliza para guiar a la IA y obtener el resultado deseado.

## Tipos de prompts

### System prompt

El ***system prompt*** es la instrucción de más alto nivel. Define el comportamiento general del modelo: límites, tono, reglas, formato de salida, restricciones de seguridad, herramientas disponibles, etc.

Ejemplo:

```text
Eres un asistente experto en Python. Responde siempre de forma clara, concisa y con ejemplos cuando sea útil. No inventes información.
```

Sirve para fijar el “marco de trabajo” del modelo.

### User prompt

El ***user prompt*** es la instrucción concreta que da el usuario en cada interacción. Define la tarea específica que el modelo debe resolver.

Ejemplo:

```text
Explícame cómo diseñar una arquitectura RAG para resumir historias clínicas.
```

Es lo más variable: cambia en cada consulta.

### Role prompt

El ***role prompt*** no siempre es una categoría técnica separada, pero se usa mucho para referirse a la parte del *prompt* que le asigna un **rol o personalidad experta** al modelo.

Ejemplo:

```text
Actúa como un senior ML engineer especializado en NLP clínico.
```

En muchos casos, el *role prompt* está dentro del *system prompt* o al inicio del *user prompt*. Su objetivo es orientar el tipo de razonamiento, vocabulario y nivel técnico esperado.

## Consideraciones

En la práctica, el *prompt engineering* implica tomar varias decisiones:

- redacción de instrucciones
- elección del rol o perspectiva
- uso de ejemplos (*few-shot*)
- delimitación del contexto relevante
- especificación del formato de salida
- restricciones de estilo, longitud o seguridad

Funciona especialmente bien cuando el modelo ya tiene la capacidad necesaria y solo necesitamos guiar su comportamiento. Es menos eficaz cuando la tarea requiere conocimiento muy específico, consistencia fuerte o comportamiento que el modelo no domina de forma nativa.

## Errores comunes

Los errores más comunes en *prompt engineering* incluyen:

- Pensar que basta con pedirlo “mejor” para resolver cualquier problema.
- Mezclar demasiadas instrucciones en un solo *prompt*.
- No separar contexto, instrucción y formato.
- No probar variaciones y asumir que un *prompt* bueno lo es para todos los casos.
- Confundir *prompt engineering* con [[Fine-tuning|fine-tuning]], son enfoques distintos.

## Buenas prácticas

Se consideran buenas prácticas a la hora de elaborar un *prompt* las siguientes:

- ser claro y específico
- definir la tarea explícitamente
- especificar el formato de salida si es necesario
- añadir restricciones (longitud, tono, fuente)
- evitar instrucciones vagas o abiertas
- indicar al modelo qué hacer si falta información.

Unas instrucciones claras permiten obtener resultados predecibles y útiles.

## Evaluación de un prompt

Un *prompt* es efectivo si produce consistentemente respuestas correctas, respuestas relevantes, con el formato y tono deseados y mínimas alucinaciones.

Podemos evaluar la eficacia de un *prompt* de la siguiente manera:

- probando con múltiples entradas
- verificando la coherencia entre ejecuciones
- comparando los resultados antes y después de los cambios
- recopilando el *feedback* de los usuarios

Si modificar un *prompt* reduce las respuestas incorrectas o irrelevantes, el nuevo *prompt* es más efectivo.

## Preguntas

#flashcards/llms #flashcards/nlp

**¿Qué es el *prompt engineering*?**
?
![[#Definición]]

**¿Qué es un *prompt*?**
?
![[#Definición de prompt]]

**¿Qué tipos de *prompt* existen?**
?
![[#Tipos de prompts]]

**¿Qué decisiones debemos tomar a la hora de elaborar un *prompt*?**
?
![[#Consideraciones]]

**¿Qué errores comunes se cometen en *prompt engineering*?**
?
![[#Errores comunes]]

**¿Cuáles son algunas buenas prácticas a la hora de escribir un *prompt*?**
?
![[#Buenas prácticas]]

**¿Cómo podemos evaluar la eficacia de un *prompt*?**
?
![[#Evaluación de un prompt]]
