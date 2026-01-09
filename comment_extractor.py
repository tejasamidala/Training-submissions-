import re
from pathlib import Path

# Extract:
# 1) Python comments starting with #
# 2) Python triple-quote docstrings ("""...""" or '''...''')
PY_COMMENT_RE = re.compile(r"(?m)^\s*#(.*)$")  # group(1) = comment text
PY_DOCSTRING_RE = re.compile(r'(?s)(["\']{3})(.*?)(\1)')  # group(2) = docstring content


def extract_comments(text: str):
    line_comments = [m.group(1).strip() for m in PY_COMMENT_RE.finditer(text)]
    docstrings = [m.group(2).strip() for m in PY_DOCSTRING_RE.finditer(text)]
    return line_comments, docstrings


def main():
    file_path = input("Enter a Python file name (example: diary_app.py): ").strip()

    path = Path(file_path)
    if not path.exists():
        print("File not found.")
        return

    try:
        content = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        # fallback if encoding is weird
        content = path.read_text(errors="replace")

    line_comments, docstrings = extract_comments(content)

    print("\n--- Line Comments (#) ---")
    if line_comments:
        for i, c in enumerate(line_comments, 1):
            print(f"{i}. {c}")
    else:
        print("No # comments found.")

    print("\n--- Docstrings (triple quotes) ---")
    if docstrings:
        for i, d in enumerate(docstrings, 1):
            print(f"{i}. {d}\n")
    else:
        print("No docstrings found.")


if __name__ == "__main__":
    main()