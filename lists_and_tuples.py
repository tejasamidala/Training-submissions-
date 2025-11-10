# List creation
fruits = ["apple", "banana", "cherry", "mango", "orange"]

# Indexing
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Slicing
print("First three fruits:", fruits[:3])
print("Middle fruits:", fruits[1:4])
print("All except the first:", fruits[1:])
# List methods
fruits.append("grape")        # add an item
print("After append:", fruits)

fruits.remove("banana")       # remove an item
print("After remove:", fruits)

fruits.sort()                 # sort alphabetically
print("Sorted list:", fruits)

fruits.reverse()              # reverse the list
print("Reversed list:", fruits)

print("Total fruits:", len(fruits))  # length of the list
# Tuples
colors = ("red", "green", "blue", "yellow")

print("\nTuple example:")
print("All colors:", colors)
print("First color:", colors[0])
print("Last color:", colors[-1])
print("Number of colors:", len(colors))

# Demonstrate immutability
try:
    colors[1] = "purple"
except TypeError:
    print("Tuples are immutable — you cannot modify them!")
    # Contact book using a list of tuples
print("\n--- Contact Book ---")

contacts = [
    ("Alice", "123-456-7890"),
    ("Bob", "987-654-3210"),
    ("Charlie", "555-666-7777")
]

for name, phone in contacts:
    print(f"Name: {name}, Phone: {phone}")

# Add a new contact
contacts.append(("David", "111-222-3333"))
print("\nAfter adding a new contact:")
for name, phone in contacts:
    print(f"Name: {name}, Phone: {phone}")