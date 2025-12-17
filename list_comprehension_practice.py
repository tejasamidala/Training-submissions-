# List Comprehension Practice

# 1) Squares
numbers = [1, 2, 3, 4, 5]
squares = [n * n for n in numbers]
print("Squares:", squares)

# 2) Filter even numbers
evens = [n for n in numbers if n % 2 == 0]
print("Even numbers:", evens)

# 3) Transform strings (uppercase)
words = ["hello", "python", "world"]
upper_words = [w.upper() for w in words]
print("Capitalized words:", upper_words)

# 4) Filter long words
fruits = ["apple", "kiwi", "banana", "cat", "elephant"]
long_words = [f for f in fruits if len(f) > 4]
print("Words longer than 4 letters:", long_words)

# 5) Convert numbers to strings
numbers2 = [100, 109, 210, 500]
as_strings = [str(n) for n in numbers2]
print("Numbers as strings:", as_strings)

# 6) Celsius to Fahrenheit
celsius = [3, 12, 27, 33, 41]
fahrenheit = [(c * 9/5) + 32 for c in celsius]
print("Temperatures in Fahrenheit:", fahrenheit)