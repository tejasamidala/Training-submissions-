# --- 1. Extract ages above 18 ---
ages = [12, 19, 25, 15, 30, 17, 42]
adults = [age for age in ages if age >= 18]
print("Adults (18+):", adults)


# --- 2. Convert mixed strings to cleaned lowercase words ---
raw_words = [" Hello ", "PYTHON", "", "  ai", "x", "Data ", "42", " CODE  "]
clean_words = [
    w.strip().lower()
    for w in raw_words
    if w.strip() != "" and len(w.strip()) > 1
]
print("Cleaned words:", clean_words)


# --- 3. Extract initials from names ---
names = ["Sai Teja", "Mahesh Babu", "Raju Kumar", "Anjali Devi"]
initials = [
    name.split()[0][0].upper() + name.split()[1][0].upper()
    for name in names
]
print("Initials:", initials)