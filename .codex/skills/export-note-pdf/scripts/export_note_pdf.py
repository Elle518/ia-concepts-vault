#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


VAULT_ROOT = Path(__file__).resolve().parents[4]
DEFAULT_FROM = "markdown+yaml_metadata_block+tex_math_dollars+wikilinks_title_after_pipe"


def resolve_note_path(raw: str) -> Path:
    """Resolve vault-relative note paths and the historical _ai_concepts alias."""
    normalized = raw
    if normalized.startswith("_ai_concepts/"):
        normalized = "ia_concepts/" + normalized.removeprefix("_ai_concepts/")
    path = Path(normalized).expanduser()
    if not path.is_absolute():
        path = VAULT_ROOT / path
    return path.resolve()


def vault_relative(path: Path) -> str:
    try:
        return os.fspath(path.relative_to(VAULT_ROOT))
    except ValueError:
        return os.fspath(path)


def strip_frontmatter(text: str) -> str:
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            after = text.find("\n", end + 4)
            return text[after + 1 :] if after != -1 else ""
    return text


def clean_inline(text: str) -> str:
    text = re.sub(r"!\[\[([^\]]+)\]\]", r"[embed: \1]", text)
    text = re.sub(r"\[\[([^|\]]+)\|([^\]]+)\]\]", r"\2", text)
    text = re.sub(r"\[\[([^\]]+)\]\]", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = text.replace("***", "").replace("**", "").replace("*", "")
    return text.strip()


def note_title(path: Path, markdown: str) -> str:
    for line in strip_frontmatter(markdown).splitlines():
        if line.startswith("# "):
            return clean_inline(line[2:])
    return path.stem


def prepare_markdown(markdown: str, include_questions: bool = False) -> str:
    if not include_questions:
        markdown = remove_questions_section(markdown)
    markdown = remove_obsidian_block_ids(markdown)
    markdown = re.sub(r"!\[\[([^\]]+)\]\]", r"> [embed: \1]", markdown)
    markdown = re.sub(r"%%.*?%%", "", markdown, flags=re.DOTALL)
    return markdown


def remove_obsidian_block_ids(markdown: str) -> str:
    lines = []
    for line in markdown.splitlines():
        if re.match(r"^\s*!?\[\[#\^[A-Za-z0-9_-]+\]\]\s*$", line):
            continue
        line = re.sub(r"\s+\^[A-Za-z0-9_-]+\s*$", "", line)
        line = re.sub(r"!?\[\[#\^[A-Za-z0-9_-]+\]\]", "", line)
        lines.append(line.rstrip())
    return "\n".join(lines) + ("\n" if markdown.endswith("\n") else "")


def remove_questions_section(markdown: str) -> str:
    lines = markdown.splitlines()
    kept: list[str] = []
    skipping_level: int | None = None

    for line in lines:
        heading = re.match(r"^(#{1,6})\s+(.+?)\s*#*\s*$", line)
        if heading:
            level = len(heading.group(1))
            title = clean_inline(heading.group(2)).strip().lower()
            if skipping_level is not None and level <= skipping_level:
                skipping_level = None
            if skipping_level is None and title == "preguntas":
                skipping_level = level
                continue
        if skipping_level is None:
            kept.append(line)

    return "\n".join(kept) + ("\n" if markdown.endswith("\n") else "")


def pandoc_command(source: Path, prepared: Path, output: Path, title: str, pdf_engine: str) -> list[str]:
    source_parent = source.parent
    resource_path = os.pathsep.join([os.fspath(source_parent), os.fspath(VAULT_ROOT)])
    return [
        "pandoc",
        os.fspath(prepared),
        "--from",
        DEFAULT_FROM,
        "--to",
        "pdf",
        "--pdf-engine",
        pdf_engine,
        "--standalone",
        "--resource-path",
        resource_path,
        "--metadata",
        f"title={title}",
        "--variable",
        "papersize=a4",
        "--variable",
        "geometry:margin=2cm",
        "--variable",
        "fontsize=11pt",
        "--variable",
        "colorlinks=true",
        "--variable",
        "linkcolor=blue",
        "--output",
        os.fspath(output),
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description="Export an Obsidian Markdown note to PDF with Pandoc.")
    parser.add_argument("source", help="Markdown source note, relative to the vault or absolute")
    parser.add_argument("output", help="PDF output path, relative to the vault or absolute")
    parser.add_argument("--pdf-engine", default="xelatex", help="Pandoc PDF engine to use; default: xelatex")
    parser.add_argument("--include-questions", action="store_true", help="Keep the Preguntas section in the PDF")
    parser.add_argument("--print-command", action="store_true", help="Print the pandoc command before running it")
    args = parser.parse_args()

    pandoc = shutil.which("pandoc")
    if not pandoc:
        print("error: pandoc is not installed or is not on PATH", file=sys.stderr)
        return 127

    source = resolve_note_path(args.source)
    if not source.exists():
        print(f"error: source note not found: {source}", file=sys.stderr)
        return 2

    output = Path(args.output).expanduser()
    if not output.is_absolute():
        output = VAULT_ROOT / output
    output = output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)

    markdown = source.read_text(encoding="utf-8")
    title = note_title(source, markdown)

    with tempfile.TemporaryDirectory(prefix="export-note-pdf-") as tmp:
        prepared = Path(tmp) / source.name
        prepared_markdown = prepare_markdown(markdown, include_questions=args.include_questions)
        prepared.write_text(prepared_markdown, encoding="utf-8")
        command = pandoc_command(source, prepared, output, title, args.pdf_engine)
        command[0] = pandoc
        if args.print_command:
            print(" ".join(subprocess.list2cmdline([part]) for part in command))
        subprocess.run(command, cwd=VAULT_ROOT, check=True)

    print(vault_relative(output))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
