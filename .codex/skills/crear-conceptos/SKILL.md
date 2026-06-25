---
name: crear-conceptos
description: Crear notas de conceptos de AI/ML/NLP para este vault desde cero o a partir de recursos como PDF, vídeo o artículo web, y proponer mejoras cuando el recurso solape con notas ya existentes.
---

# Crear conceptos

Usa esta skill cuando el usuario pida crear o revisar notas de concepto para este vault.

## Contexto del vault

- Escribe en español por defecto.
- Mantén en inglés los términos técnicos que ya se usan así en entrevistas: `attention`, `embedding`, `fine-tuning`, `retrieval`, `prompting`, etc.
- Sigue el estilo del vault:
  - notas útiles para estudiar
  - enfoque de entrevista
  - preguntas tipo flashcard
  - enlaces internos entre conceptos
- Antes de redactar, revisa `AGENTS.md`, `_templates/Concept.md` y varias notas existentes en `ia_concepts/` para imitar estructura, tono y longitud.

## Cuándo usar esta skill

### 1. Nota nueva sin referencia

Si el usuario pide un concepto nuevo sin fuente, crea la nota usando criterio experto en AI/ML/NLP.

Prioriza:

- definición clara en 2-4 frases
- intuición sencilla
- explicación técnica útil, sin alargarla de más
- errores comunes o limitaciones
- preguntas de entrevista con respuestas ancladas dentro de la propia nota
- enlaces internos a conceptos relacionados que ya existan o que probablemente deban existir

### 2. Nota o notas a partir de un recurso

Si el usuario pasa un PDF, vídeo, enlace o artículo:

1. Extrae los conceptos realmente relevantes para el vault.
2. Selecciona solo lo que aporte valor estable para estudiar o entrevistar.
3. Para cada concepto, combina:
   - lo que dice el recurso
   - lo que conviene añadir como contexto experto
   - los vínculos internos útiles
4. Si el recurso es sobre un concepto ya existente, no crees duplicados.
   En su lugar, revisa la nota actual y propón cambios concretos que merezca la pena incorporar.

## Regla para notas existentes

Cuando ya exista una nota del concepto:

- identifica la nota más cercana antes de escribir una nueva
- compara el recurso con la nota actual
- sugiere únicamente información nueva, útil y durable
- separa con claridad:
  - `añadir`
  - `matizar`
  - `corregir`

No reescribas toda la nota salvo que el usuario lo pida.

## Criterios de calidad

- No hagas notas enciclopédicas.
- No metas conceptos secundarios como notas nuevas si basta con enlazarlos.
- No inventes referencias del recurso: si algo es una inferencia, indícalo.
- Mantén el Markdown limpio.
- Evita flashcards demasiado largas.
- Si el recurso es ambiguo o incompleto, di qué parte viene del recurso y qué parte es criterio experto.

## Formato de salida recomendado

Cuando entregues el trabajo, usa una de estas salidas:

- **Concepto nuevo**: nota completa lista para pegar en Obsidian.
- **Varios conceptos**: lista priorizada de notas a crear, cada una con su borrador.
- **Concepto ya existente**: propuesta de edición con cambios concretos por secciones.

Si hay solape con una nota existente, devuelve también un resumen breve de por qué no crear duplicado.
