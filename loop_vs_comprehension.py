# Comparing loops vs list comprehension

numbers = [2, 5, 8, 11, 14]

# ---- Traditional Loop ----
squares_loop = []
for n in numbers:
    squares_loop.append(n * n)

# ---- List Comprehension ----
squares_comp = [n * n for n in numbers]

print("Squares using loop:", squares_loop)
print("Squares using list comprehension:", squares_comp)


# ---- Filtering Even Numbers ----
# Traditional loop
evens_loop = []
for n in numbers:
    if n % 2 == 0:
        evens_loop.append(n)

# Comprehension
evens_comp = [n for n in numbers if n % 2 == 0]

print("Evens using loop:", evens_loop)
print("Evens using list comprehension:", evens_comp)