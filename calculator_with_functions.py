def calculate(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero!"
    else:
        return "Invalid operation!"

result = calculate(1, 9, "multiply")
print("Result:", result)