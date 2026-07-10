---
type: concept
tags:
  - llms
  - nlp
  - review
---

## Definición

Una **alucinación en LLMs** ocurre cuando un modelo genera una respuesta que no está respaldada por hechos, fuentes o contexto suficiente.

Puede sonar coherente y segura, pero contener datos inventados, citas inexistentes, relaciones falsas o inferencias que no se justifican con la información disponible.

La intuición es que el modelo optimiza generar texto plausible, no verificar automáticamente que cada afirmación corresponda con la realidad.

## Por qué ocurren

El *[[Sampling|sampling]]* influye, pero no explica por sí solo todas las alucinaciones.

Dos hipótesis útiles para entenderlas son:

- ***Self-delusion***. En modelos autorregresivos, cada token nuevo se condiciona en el texto anterior, incluyendo texto generado por el propio modelo. Si el modelo introduce una premisa falsa, puede seguir desarrollándola como si fuera un hecho.
- **Desajuste de conocimiento**. Durante [[Supervised finetuning|SFT]] o *[[Instruction tuning|instruction tuning]]*, el modelo aprende a imitar respuestas humanas. Si los etiquetadores usan conocimiento que el modelo no tiene realmente disponible, el entrenamiento puede reforzar respuestas que suenan bien pero no están fundamentadas.

Estas hipótesis se complementan, una se centra en el mecanismo de generación y otra en los datos de supervisión.

## Snowballing hallucinations

Las ***snowballing hallucinations*** aparecen cuando una suposición inicial incorrecta arrastra la generación posterior.

El modelo no solo comete un error aislado, sino que continúa construyendo una explicación coherente alrededor de ese error. Esto puede hacer que falle incluso en preguntas que habría podido responder bien si no hubiera empezado desde una premisa falsa.

## Mitigación

No existe una forma universal de eliminar alucinaciones, pero se pueden reducir con varias capas:

- [[RAG]] para anclar respuestas en fuentes externas.
- [[Grounding]] y citas verificables.
- [[Guardarraíles]] que limiten la especulación.
- *[[Prompt engineering|Prompts]]* que permitan decir “no lo sé”.
- Respuestas más concisas cuando la tarea lo permita.
- Verificación posterior con herramientas, búsqueda o evaluadores.
- Entrenamiento con señales factuales y contra-factuales.
- [[RLHF]] o funciones de recompensa que penalicen inventar información.

En tareas de alta factualidad, la mitigación debe diseñarse como sistema, no como una frase añadida al *prompt*.

## Detección

Detectar alucinaciones es difícil porque una respuesta puede ser fluida, plausible y aun así falsa.

Algunas estrategias prácticas son comparar contra fuentes recuperadas, pedir evidencias, ejecutar verificadores externos, usar evaluaciones humanas y medir tasas de error en conjuntos representativos. Aun así, ningún detector es perfecto.

## Errores comunes

- Creer que una respuesta segura o bien escrita es factual.
- Pensar que bajar la temperatura elimina alucinaciones.
- Confiar en RAG sin evaluar si la recuperación trae el contexto correcto.
- Pedir citas sin comprobar que existan.
- Tratar las alucinaciones como un problema solo de *prompt*.
- Confundir ausencia de alucinaciones en demos con seguridad en producción.

## Preguntas

#flashcards/llms #flashcards/nlp 

**¿Qué es una alucinación en LLMs?**
?
![[#Definición]]

**¿Por qué ocurren las alucinaciones en LLMs?**
?
![[#Por qué ocurren]]

**¿Qué son las *snowballing hallucinations*?**
?
![[#Snowballing hallucinations]]

**¿Cómo se pueden mitigar las alucinaciones en LLMs?**
?
![[#Mitigación]]

**¿Por qué es difícil detectar alucinaciones?**
?
![[#Detección]]

**¿Qué errores comunes hay al tratar alucinaciones en LLMs?**
?
![[#Errores comunes]]
