password = input("enter your password: ")
length = len(password)
strength = 0
if length >= 8:
    strength += 1
if any(char.isdigit() for char in password):
    strength += 1
if any(char.isupper() for char in password):
    strength += 1
if any(char.islower() for char in password):
    strength += 1
if any(char in "!@#$%^&*()_+-=[]{};:'\",.<>?/|" for char in password):
    strength += 1
if strength <=2:
    print("Weak password")
elif strength == 3 or strength == 4:
    print("Moderate password")
else:
    print("Strong password")
    