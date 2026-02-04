expenses = []

def show_menu():
    print("\nExpense Tracker")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Exit")

while True:
    show_menu()
    choice = input("Enter choice (1-3): ")

    if choice == "1":
        name = input("Expense name: ")
        amount = float(input("Amount: "))
        expenses.append({"name": name, "amount": amount})
        print("Expense added.")

    elif choice == "2":
        if not expenses:
            print("No expenses yet.")
        else:
            print("\nYour Expenses:")
            total = 0
            for i, exp in enumerate(expenses, start=1):
                print(f"{i}. {exp['name']} - ${exp['amount']}")
                total += exp["amount"]
            print("Total spent:", total)

    elif choice == "3":
        print("Goodbye 👋")
        break

    else:
        print("Invalid choice. Try again.")