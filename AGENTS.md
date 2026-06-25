# AGENTS.md

## Objetivo del proyecto

Este repositorio es un Obsidian Vault para preparar entrevistas de ML/NLP/AI Engineer.

El objetivo no es crear apuntes enciclopédicos, sino notas útiles para estudiar mediante:

- Active Recall
- Spaced Repetition
- Flashcards
- Preguntas de tipo entrevista
- Links internos entre conceptos

## Idioma

Escribe por defecto en español, salvo que el término técnico sea más natural en inglés.

Mantén los nombres técnicos habituales en inglés cuando sean los usados en entrevistas como, por ejemplo, attention, embedding, fine-tuning, retrieval, etc.

## Estilo de las notas

Antes de crear una nota nueva, revisa varias notas existentes del vault para imitar:

- estructura
- nivel de detalle
- tono
- longitud
- forma de crear preguntas para las flashcards

No cambies las notas existentes salvo que se te pida.

## Flujo de trabajo para conceptos

Cuando la tarea sea crear o revisar un concepto:

1. Busca primero si ya existe una nota equivalente o muy cercana en `ia_concepts/`.
2. Si el usuario aporta un recurso, extrae primero los conceptos relevantes y luego decide cuáles merecen nota propia.
3. Si el concepto ya existe, no dupliques la nota: propón cambios concretos sobre la nota actual.
4. Separa siempre el resultado en una de estas salidas:
   - nota nueva lista para pegar
   - lista de conceptos a crear
   - propuesta de mejora sobre una nota existente
5. Cuando hagas una propuesta de mejora, distingue entre:
   - añadir
   - matizar
   - corregir

## Convenciones operativas

- Usa `#review` en las notas pensadas para repaso por Spaced Repetition.
- Usa `#flashcards` y, cuando tenga sentido, un subtag temático como `#flashcards/nlp` o `#flashcards/ml`.
- Si una nota requiere trabajo temporal o borrador, colócala en `_raw/` y deja la versión final en `ia_concepts/`.
- Mantén los enlaces internos cuando un concepto dependa claramente de otro que ya exista o que sea una nota futura probable.

## Estructura recomendada para una nota de concepto

Cada nota de concepto debe contener, como mínimo, salvo que no aplique:

- Título del concepto
- Definición. Una explicación clara en 2-4 frases.
- Intuición. Explicación sencilla, con analogía o ejemplo si ayuda, preferiblemente relacionado con ML, NLP o AI Engineering.
- Explicación técnica. Desarrollo más formal, pero sin hacerlo innecesariamente largo.
- Errores comunes. Malentendidos o limitaciones frecuentes.
- Preguntas. Preguntas tipo entrevista con referencia a la respuesta esperada dentro del propio concepto con un formato compatible con el plugin Spaced Repetition de Obsidian.
- Links internos. Cuando menciones conceptos importantes que probablemente existan o deban existir como notas, usa links internos. Si una nota relacionada no existe, no la crees automáticamente salvo que se te pida. Puedes dejarla enlazada como nota futura.

## Control de calidad

Antes de elaborar una nota nueva, revisa que cumpla con los siguientes criterios:

- Comprueba si ya existe una nota sobre el concepto, evita duplicados
- Revisa que las preguntas sean útiles para entrevistas
- Revisa que las flashcards no sean demasiado largas
- Mantén el Markdown limpio
