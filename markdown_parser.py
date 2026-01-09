import re

H1_RE = re.compile(r"^\s*#\s+(.*)$")
BOLD_RE = re.compile(r"\*\*(.+?)\*\*")
ITALIC_RE = re.compile(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)")
CODE_RE = re.compile(r"`(.+?)`")

def parse_line(line: str) -> str:
    m = H1_RE.match(line)
    if m:
        return f"HEADING: {m.group(1).strip()}"

    line = BOLD_RE.sub(r"BOLD(\1)", line)
    line = CODE_RE.sub(r"CODE(\1)", line)
    line = ITALIC_RE.sub(r"ITALIC(\1)", line)
    return line.rstrip()

def main():
    print("Simple Markdown Parser")
    print("Type lines. Press ENTER on empty line to finish.\n")

    lines = []
    while True:
        s = input()
        if s == "":
            break
        lines.append(s)

    print("\n--- Parsed Output ---")
    for line in lines:
        print(parse_line(line))

if __name__ == "__main__":
    main()