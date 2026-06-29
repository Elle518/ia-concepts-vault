---
type: concept
tags:
  - llms
  - nlp
  - review
---

## Definición

Un ***prompt template*** es una plantilla reutilizable de [[Prompt engineering|prompt engineering]] con variables que se rellenan en tiempo de ejecución.

Permite mantener una estructura estable de instrucciones mientras cambian datos como el contexto, la pregunta del usuario, el idioma, el formato esperado o la política de respuesta.

Es como un formulario, donde el esqueleto permanece igual pero cada ejecución rellena campos distintos. Esto ayuda a que el comportamiento del modelo sea más consistente.

Un *prompt template* suele incluir *placeholders* como `{context}`, `{user_question}` o `{format}`:

```text
Responde usando solo el contexto.

Contexto:
{context}

Pregunta:
{user_question}

Formato:
{output_format}
```

## Utilidad

En sistemas de *AI Engineering*, las plantillas ayudan a separar lógica de aplicación, recuperación de contexto y redacción del *prompt*. Son especialmente comunes en [[RAG]], chatbots, extracción de información y tareas repetibles.

## Errores comunes

- No escapar o validar el contenido insertado en las variables.
- Mezclar instrucciones del sistema con datos del usuario sin delimitadores.
- Crear plantillas tan rígidas que fallan ante entradas reales.
- No probar la plantilla con casos límite.

## Preguntas

#flashcards/llms #flashcards/nlp

**¿Qué es un *prompt template*?**
?
![[#Definición]]

**¿Para qué sirven las variables en un prompt template?**
?
![[#Utilidad]]

**¿Qué error de seguridad o robustez puede aparecer al usar *prompt templates*?**
?
![[#Errores comunes]]
