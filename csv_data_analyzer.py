import csv

FILE_NAME = "sample_sales.csv"

def safe_float(value):
    try:
        return float(value)
    except:
        return None

def analyze_csv(filename):
    total = 0.0
    valid_count = 0
    amounts = []
    category_totals = {}

    skipped_rows = 0

    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            category = row["category"].strip()
            amount = safe_float(row["amount"])

            if amount is None:
                skipped_rows += 1
                continue

            total += amount
            valid_count += 1
            amounts.append(amount)

            category_totals[category] = category_totals.get(category, 0) + amount

    avg = total / valid_count if valid_count > 0 else 0
    min_amt = min(amounts) if amounts else 0
    max_amt = max(amounts) if amounts else 0

    print("\n--- CSV DATA ANALYSIS REPORT ---")
    print("File:", filename)
    print("Valid rows:", valid_count)
    print("Skipped rows (bad/missing amount):", skipped_rows)
    print("Total amount:", round(total, 2))
    print("Average amount:", round(avg, 2))
    print("Min amount:", round(min_amt, 2))
    print("Max amount:", round(max_amt, 2))

    print("\n--- Category Totals ---")
    for cat, amt in sorted(category_totals.items(), key=lambda x: x[1], reverse=True):
        print(f"{cat}: {round(amt, 2)}")

if __name__ == "__main__":
    analyze_csv(FILE_NAME)