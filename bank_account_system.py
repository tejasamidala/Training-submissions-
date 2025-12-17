class BankAccount:
    bank_name = "Python Bank"   # class attribute (shared)

    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = float(balance)
        self.transactions = []

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        amount = self._validate_amount(amount)
        self._balance += amount
        self.transactions.append(f"Deposit: {amount}")
        print(f"Deposited {amount}")

    def withdraw(self, amount):
        amount = self._validate_amount(amount)
        if amount > self._balance:
            print("Insufficient balance")
            self.transactions.append(f"Withdraw declined: {amount}")
            return
        self._balance -= amount
        self.transactions.append(f"Withdraw: {amount}")
        print(f"Withdrew {amount}")

    def show_statement(self):
        print("\n--- Statement ---")
        for t in self.transactions:
            print(t)
        print("Balance:", self.balance)
        print("--------------\n")

    @classmethod
    def show_bank_name(cls):
        print("Welcome to", cls.bank_name)

    @staticmethod
    def _validate_amount(amount):
        try:
            amount = float(amount)
        except ValueError:
            raise ValueError("Amount must be a number")
        if amount <= 0:
            raise ValueError("Amount must be > 0")
        return amount


def main():
    BankAccount.show_bank_name()
    account = BankAccount("Sai Teja", 1000)

    while True:
        print("\nBank Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Show Statement")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            amt = input("Enter deposit amount: ")
            try:
                account.deposit(amt)
            except ValueError as e:
                print("Error:", e)

        elif choice == "2":
            amt = input("Enter withdraw amount: ")
            try:
                account.withdraw(amt)
            except ValueError as e:
                print("Error:", e)

        elif choice == "3":
            print("Current Balance:", account.balance)

        elif choice == "4":
            account.show_statement()

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
