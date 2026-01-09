import re

# Template format:
# "Hello {{ name }}! Today is {{ day | upper }}."
#
# Supports filters:
# - upper
# - lower
# - title
#
# Regex groups:
# group(1) = variable name
# group(2) = optional filter name
TOKEN_RE = re.compile(r"\{\{\s*([a-zA-Z_]\w*)\s*(?:\|\s*(upper|lower|title)\s*)?\}\}")


def apply_filter(value: str, flt: str | None) -> str:
    if flt == "upper":
        return value.upper()
    if flt == "lower":
        return value.lower()
    if flt == "title":
        return value.title()
    return value


def render(template: str, context: dict) -> str:
    def replacer(match: re.Match):
        var_name = match.group(1)
        flt = match.group(2)

        if var_name not in context:
            return f"<<missing:{var_name}>>"

        value = str(context[var_name])
        return apply_filter(value, flt)

    return TOKEN_RE.sub(replacer, template)


def main():
    template = input("Enter template (example: Hello {{ name | title }}):\n> ")
    print("\nNow enter values. Leave blank key to finish.")

    context = {}
    while True:
        key = input("Key: ").strip()
        if key == "":
            break
        val = input("Value: ").strip()
        context[key] = val

    output = render(template, context)
    print("\n--- Rendered Output ---")
    print(output)


if __name__ == "__main__":
    main()