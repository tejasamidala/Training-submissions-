# ---------- Safe Division Example ----------

def safe_divide():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        result = a / b
    except ValueError:
        print("Error: Please enter valid numbers only.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    else:
        print("Result:", result)
    finally:
        print("Done (this always runs).")


# ---------- Custom Exception Example ----------

class NumberTooSmallError(Exception):
    pass


def check_number():
    try:
        num = int(input("Enter a number (must be 10 or more): "))
        if num < 10:
            raise NumberTooSmallError("Number is too small. Minimum is 10.")
        print("Valid number entered:", num)
    except NumberTooSmallError as e:
        print("Custom Error:", e)
    except ValueError:
        print("Please enter a valid integer.")


# ---------- Run Programs ----------

print("\n--- Safe Divide Demo ---")
safe_divide()

print("\n--- Custom Exception Demo ---")
check_number()