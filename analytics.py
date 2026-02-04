import csv

def load_sales_data(filename):
    records = []
    with open(filename, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                row["quantity"] = int(row["quantity"])
                row["unit_price"] = float(row["unit_price"])
                records.append(row)
            except ValueError:
                continue
    return records

def analyze_data(data):
    total_revenue = 0.0
    customer_revenue = {}
    product_revenue = {}
    region_revenue = {}

    for row in data:
        revenue = row["quantity"] * row["unit_price"]
        total_revenue += revenue

        customer = row["customer_name"]
        product = row["product"]
        region = row["region"]

        customer_revenue[customer] = customer_revenue.get(customer, 0) + revenue
        product_revenue[product] = product_revenue.get(product, 0) + revenue
        region_revenue[region] = region_revenue.get(region, 0) + revenue

    return total_revenue, customer_revenue, product_revenue, region_revenue

def generate_report(total_revenue, customer_revenue, product_revenue, region_revenue):
    top_customer = max(customer_revenue, key=customer_revenue.get)
    top_product = max(product_revenue, key=product_revenue.get)
    top_region = max(region_revenue, key=region_revenue.get)

    report = f"""
==============================
SALES PERFORMANCE REPORT
==============================

Total Revenue: ${total_revenue:,.2f}

Top Customer:
- {top_customer}: ${customer_revenue[top_customer]:,.2f}

Top Product:
- {top_product}: ${product_revenue[top_product]:,.2f}

Top Region:
- {top_region}: ${region_revenue[top_region]:,.2f}

Revenue by Customer:
"""

    for cust, amt in sorted(customer_revenue.items(), key=lambda x: x[1], reverse=True):
        report += f"- {cust}: ${amt:,.2f}\n"

    report += "\nRevenue by Region:\n"
    for reg, amt in sorted(region_revenue.items(), key=lambda x: x[1], reverse=True):
        report += f"- {reg}: ${amt:,.2f}\n"

    return report.strip()

def main():
    data = load_sales_data("sales_data.csv")
    total_revenue, customer_revenue, product_revenue, region_revenue = analyze_data(data)
    report = generate_report(total_revenue, customer_revenue, product_revenue, region_revenue)

    print(report)

    with open("report.txt", "w") as f:
        f.write(report + "\n")

if __name__ == "__main__":
    main()