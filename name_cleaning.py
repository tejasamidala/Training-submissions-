# Raw messy data
raw_data = ["Sai ", "  ", "mahesh", "", "  RAJU", "x", "Te", "  anjali  "]

# Clean the data (remove empty, trim spaces, lowercase, ignore very short names)
cleaned = [
    item.strip().capitalize()
    for item in raw_data
    if item.strip() != "" and len(item.strip()) > 2
]

print("Cleaned names:", cleaned)