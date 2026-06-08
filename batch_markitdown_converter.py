from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox
from markitdown import MarkItDown


def get_unique_output_path(input_path: Path) -> Path:
    """
    Creates an output .md path in the same folder.
    If file.md already exists, creates file_1.md, file_2.md, etc.
    """
    output_path = input_path.with_suffix(".md")

    counter = 1
    while output_path.exists():
        output_path = input_path.with_name(f"{input_path.stem}_{counter}.md")
        counter += 1

    return output_path


def convert_files():
    root = tk.Tk()
    root.withdraw()

    file_paths = filedialog.askopenfilenames(
        title="Select files to convert to Markdown",
        filetypes=[
            ("Supported files", "*.pdf *.docx *.pptx *.xlsx *.html *.htm *.csv *.json *.xml *.txt"),
            ("All files", "*.*"),
        ],
    )

    if not file_paths:
        messagebox.showinfo("No files selected", "No files were selected.")
        return

    md_converter = MarkItDown(enable_plugins=False)

    successful = 0
    failed = []

    for file_path in file_paths:
        input_path = Path(file_path)

        try:
            result = md_converter.convert(str(input_path))
            output_path = get_unique_output_path(input_path)

            output_path.write_text(result.text_content, encoding="utf-8")

            successful += 1
            print(f"Converted: {input_path.name} -> {output_path.name}")

        except Exception as e:
            failed.append((input_path.name, str(e)))
            print(f"Failed: {input_path.name} | {e}")

    summary = f"Converted {successful} file(s)."

    if failed:
        summary += f"\n\nFailed {len(failed)} file(s):"
        for file_name, error in failed:
            summary += f"\n- {file_name}: {error}"

    messagebox.showinfo("Conversion finished", summary)


if __name__ == "__main__":
    convert_files()
