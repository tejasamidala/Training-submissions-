class BankAccount:
    bank_name = "Python Bank"   # class attribute

    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance  # protected attribute

    # property (getter)
    @property
    def balance(self):
        return self._balance

    # instance method
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ₹{amount}")
        else:
            print("Invalid amount")

    # instance method
    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew ₹{amount}")
        else:
            print("Insufficient balance")

    # class method
    @classmethod
    def show_bank_name(cls):
        print("Welcome to", cls.bank_name)

    # static method
    @staticmethod
    def validate_amount(amount):
        return amount > 0


def main():
    account = BankAccount("Sai Teja", 1000)
    BankAccount.show_bank_name()

    while True:
        print("\nBank Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = int(input("Enter amount to deposit: "))
            account.deposit(amount)

        elif choice == "2":
            amount = int(input("Enter amount to withdraw: "))
            account.withdraw(amount)

        elif choice == "3":
            print("Current Balance:", account.balance)

        elif choice == "4":
            print("Thank you! Exiting...")
            break

        else:
            print("Invalid choice. Try again.")


# THIS LINE IS THE KEY
main()
