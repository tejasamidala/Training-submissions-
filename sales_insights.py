import csv

total_revenue = 0
total_quantity = 0
product_sales = {}

with open("sales_data.csv", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        qty = int(row["quantity"])
        price = float(row["price"])
        revenue = qty * price

        total_revenue += revenue
        total_quantity += qty

        product = row["product"]
        product_sales[product] = product_sales.get(product, 0) + revenue

top_product = max(product_sales, key=product_sales.get)

report = f"""
Sales Summary Report
--------------------
Total Revenue: ${total_revenue}
Total Items Sold: {total_quantity}
Top Selling Product: {top_product}
"""

print(report)

with open("summary_report.txt", "w") as f:
    f.write(report)
    