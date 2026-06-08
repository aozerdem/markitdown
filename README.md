# Batch MarkItDown Converter

A simple Python script that converts multiple files into Markdown using Microsoft's MarkItDown library.

## What this tool does

This script lets you select one or more files from your computer and converts each file into a separate `.md` Markdown file.

The converted Markdown files are saved in the same folder as the original input files.

## Why this is useful

When working with AI tools, LLMs, or API-based workflows, the quality of the input matters.

Large documents often contain extra formatting, hidden structure, tables, layout noise, or unnecessary file data. This can increase token usage, slow down processing, and increase API cost.

Markdown is cleaner, lighter, and easier for AI tools to process.

In simple terms:

```text
Cleaner files -> fewer unnecessary tokens -> faster processing -> lower cost
```

## Estimated savings

The exact savings depend on the file type and content.

As a rough estimate, converting files to Markdown before using them in AI workflows can help reduce:

* token usage by around 20-60%
* processing time by around 20-50%
* API costs by around 20-60%

These are not fixed numbers. They are practical estimates based on the idea that cleaner input usually means less unnecessary content for the model to process.

## Supported file types

MarkItDown supports many common file types, including:

* PDF
* Word documents
* PowerPoint presentations
* Excel files
* HTML
* CSV
* TXT
* JSON
* XML

## Requirements

You need:

* Python installed on your computer
* MarkItDown installed with pip

## Install MarkItDown

Open Command Prompt or PowerShell and run:

```bash
pip install "markitdown[all]"
```

## How to use the script

1. Download the Python script from this repository.
2. Open Command Prompt or PowerShell.
3. Go to the folder where the script is saved.
4. Run:

```bash
python batch_markitdown_converter.py
```

5. A file selection window will open.
6. Select one or more files.
7. The script will convert each file into a separate `.md` file.
8. The Markdown files will be saved in the same folder as the original files.

## Example

Input files:

```text
example.pdf
presentation.pptx
spreadsheet.xlsx
```

Output files:

```text
example.md
presentation.md
spreadsheet.md
```

## Important note for beginners

Do not name your script `markitdown.py`.

Use a name like:

```text
batch_markitdown_converter.py
```

If you name your script `markitdown.py`, Python may try to import your own script instead of the real MarkItDown library, which can cause an import error.

## Notes

This script is designed for simple batch conversion.

It is especially useful before sending document content to LLMs, using files in automation workflows, or preparing cleaner text for analysis.

The goal is not to perfectly preserve visual formatting. The goal is to create a cleaner text-based version of the file.
