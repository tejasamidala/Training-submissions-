# List of numbers
numbers = [1, 2, 3, 4, 5]

# List comprehension to square each number
squares = [num * num for num in numbers]
print("Squares:", squares)
# Filtering even numbers
even_numbers = [num for num in numbers if num % 2 == 0]
print("Even numbers:", even_numbers)
# Capitalizing words
words = ["hello", "python", "world"]
capitalized = [word.upper() for word in words]
print("Capitalized words:", capitalized)
# Filtering long words (more than 4 letters)
words = ["apple", "hi", "banana", "dog", "elephant"]
long_words = [w for w in words if len(w) > 4]
print("Words longer than 4 letters:", long_words)
numbers = [100, 109, 210, 500]
as_strings = [str(n) for n in numbers]
print("Temperatures Conversion:")

celsius = [3, 12, 27, 33, 41]
fahrenheit = [(c * 9/5) + 32 for c in celsius]
print("Temperatures in Fahrenheit:", fahrenheit)