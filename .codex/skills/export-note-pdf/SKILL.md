---
name: export-note-pdf
description: Export Obsidian Markdown notes from this vault to PDF using the bundled template script, especially when the user asks to export a specific note or iterate on PDF aesthetics such as margins, typography, headers, footers, page numbers, and heading styles.
---

# Export Note PDF

## Overview

Use this skill to export a single Markdown note from the vault to PDF with Pandoc.

The current implementation is a thin Pandoc wrapper: adjust `scripts/export_note_pdf.py` when the user requests changes to the Pandoc reader extensions, PDF engine, metadata, resource paths, margins, font size, link colors, or light Obsidian Markdown preprocessing.

## Workflow

1. Pick the source note path.
2. Choose an output path under `exports/pdf/` unless the user requests another location.
3. Run:

```bash
python3 .codex/skills/export-note-pdf/scripts/export_note_pdf.py "ia_concepts/Nota.md" "exports/pdf/Nota.pdf"
```

You can also pass the historical alias directly:

```bash
python3 .codex/skills/export-note-pdf/scripts/export_note_pdf.py "_ai_concepts/Nota.md" "exports/pdf/Nota.pdf"
```

4. If the user asks for aesthetic changes, patch the Pandoc variables or preprocessing in the script, regenerate the same sample PDF, and report the new output path.

By default, the export removes the `Preguntas` section from concept notes so flashcards do not appear in study PDFs. If the user explicitly wants that section included, run with:

```bash
python3 .codex/skills/export-note-pdf/scripts/export_note_pdf.py "ia_concepts/Nota.md" "exports/pdf/Nota.pdf" --include-questions
```

## Dependencies

- Requires `pandoc` on `PATH`.
- Uses `xelatex` by default via `--pdf-engine xelatex`.
- A different Pandoc PDF engine can be selected with `--pdf-engine`.

## Current Template Defaults

- Page size: A4.
- Margins: `2cm`.
- Font size: `11pt`.
- PDF engine: `xelatex`.
- Links: colored links disabled.
- Content: rendered by Pandoc from Markdown with YAML metadata, dollar math, and Obsidian wikilinks with pipe titles.
- Preprocessing: the `Preguntas` section is removed by default; Obsidian block IDs like `^ae8bac` are removed; Obsidian embeds are converted to blockquote placeholders; Obsidian comments are removed.

## Notes

- The script does not require Python packages, but it does require Pandoc and a configured PDF engine.
- Keep edits focused on Pandoc options or small Obsidian compatibility preprocessing while iterating with the user.
