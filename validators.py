import re

EMAIL_RE = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")
PHONE_RE = re.compile(r"^(?:\+1[-.\s]?)?(?:\(\d{3}\)|\d{3})[-.\s]?\d{3}[-.\s]?\d{4}$")

def is_valid_email(email: str) -> bool:
    return bool(EMAIL_RE.match(email.strip()))

def is_valid_phone(phone: str) -> bool:
    return bool(PHONE_RE.match(phone.strip()))

def main():
    print("Validator Menu")
    print("1. Validate Email")
    print("2. Validate Phone")
    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        email = input("Enter an email: ")
        print("Valid email" if is_valid_email(email) else "Invalid email")
    elif choice == "2":
        phone = input("Enter a phone number: ")
        print("Valid phone" if is_valid_phone(phone) else "Invalid phone")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()