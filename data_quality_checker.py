import csv
from datetime import datetime

DATE_FORMAT = "%Y-%m-%d"

def is_valid_date(value: str) -> bool:
    try:
        datetime.strptime(value, DATE_FORMAT)
        return True
    except Exception:
        return False

def is_valid_email(value: str) -> bool:
    # Simple check (good enough for beginner project)
    return "@" in value and "." in value.split("@")[-1]

def safe_float(value: str):
    try:
        return float(value)
    except Exception:
        return None

def load_csv(filename: str):
    with open(filename, newline="") as f:
        return list(csv.DictReader(f))

def find_duplicates(rows, key_field):
    seen = set()
    duplicates = []
    for r in rows:
        k = r.get(key_field, "").strip()
        if k in seen and k != "":
            duplicates.append(k)
        else:
            seen.add(k)
    return duplicates

def run_quality_checks(rows):
    issues = {
        "missing_values": [],
        "invalid_salary": [],
        "invalid_join_date": [],
        "invalid_email": [],
        "duplicate_emp_ids": []
    }

    # Missing values check
    required_fields = ["emp_id", "name", "department", "salary", "join_date", "email"]
    for idx, r in enumerate(rows, start=2):  # header is line 1
        for field in required_fields:
            if r.get(field, "").strip() == "":
                issues["missing_values"].append(f"Line {idx}: missing {field}")

    # Duplicate emp_id
    dupes = find_duplicates(rows, "emp_id")
    issues["duplicate_emp_ids"] = dupes

    # Field validation
    for idx, r in enumerate(rows, start=2):
        salary = safe_float(r.get("salary", "").strip())
        if salary is None:
            issues["invalid_salary"].append(f"Line {idx}: salary='{r.get('salary')}'")

        join_date = r.get("join_date", "").strip()
        if not is_valid_date(join_date):
            issues["invalid_join_date"].append(f"Line {idx}: join_date='{join_date}'")

        email = r.get("email", "").strip()
        if not is_valid_email(email):
            issues["invalid_email"].append(f"Line {idx}: email='{email}'")

    return issues

def clean_rows(rows):
    cleaned = []
    for r in rows:
        # Skip rows with missing emp_id or name
        if r.get("emp_id", "").strip() == "" or r.get("name", "").strip() == "":
            continue

        # Fix: salary -> keep only valid numbers, else set to 0
        salary = safe_float(r.get("salary", "").strip())
        r["salary"] = str(salary if salary is not None else 0)

        cleaned.append(r)
    return cleaned

def write_csv(filename, rows, fieldnames):
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

def write_report(filename, issues):
    lines = []
    lines.append("DATA QUALITY REPORT")
    lines.append("=" * 40)

    for k, v in issues.items():
        lines.append(f"\n{k.upper()} ({len(v)}):")
        if isinstance(v, list) and len(v) > 0:
            for item in v[:20]:
                lines.append(f"- {item}")
            if len(v) > 20:
                lines.append(f"... and {len(v) - 20} more")
        else:
            lines.append("- None")

    report = "\n".join(lines)

    with open(filename, "w") as f:
        f.write(report + "\n")

    print(report)

def main():
    input_file = "employee_data.csv"
    rows = load_csv(input_file)

    issues = run_quality_checks(rows)
    write_report("data_quality_report.txt", issues)

    cleaned = clean_rows(rows)
    fieldnames = rows[0].keys()
    write_csv("employee_data_cleaned.csv", cleaned, fieldnames)

    print("\nSaved files:")
    print("- data_quality_report.txt")
    print("- employee_data_cleaned.csv")

if __name__ == "__main__":
    main()