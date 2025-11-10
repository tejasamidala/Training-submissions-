# --- Working with Dictionaries ---
student = {
    "name": "Teja",
    "age": 27,
    "is_student": True
}

# Accessing dictionary values
print("Name:", student["name"])
print("Age:", student["age"])
print("Is student:", student["is_student"])

# Adding a new key-value pair
student["grade"] = "A"
print("\nAfter adding grade:", student)

# Updating a value
student["age"] = 28
print("After updating age:", student)

# Removing a key
student.pop("is_student")
print("After removing 'is_student':", student)

# Looping through a dictionary
print("\nStudent details:")
for key, value in student.items():
    print(key, ":", value)

# --- Working with Sets ---
print("\n--- Set Operations ---")
numbers = {1, 2, 3, 4, 5}
more_numbers = {4, 5, 6, 7, 8}

print("Original sets:")
print("numbers:", numbers)
print("more_numbers:", more_numbers)

# Union
print("Union:", numbers | more_numbers)

# Intersection
print("Intersection:", numbers & more_numbers)

# Difference
print("Difference:", numbers - more_numbers)

# Add and Remove
numbers.add(9)
numbers.remove(1)
print("After add/remove:", numbers)

# Uniqueness example
unique_test = [1, 2, 2, 3, 3, 3]
unique_set = set(unique_test)
print("Unique elements from list:", unique_set)