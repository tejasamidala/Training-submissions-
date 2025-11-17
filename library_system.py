# ----------------------------------------
# Simple Library Management System
# ----------------------------------------

library = []  # list to store all books


def show_menu():
    print("\nLibrary Menu:")
    print("1. Add a book")
    print("2. View all books")
    print("3. Quit")


def add_book():
    print("\n--- Add a New Book ---")

    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()
    year = input("Enter published year: ").strip()

    # Validation
    if title == "" or author == "" or not year.isdigit():
        print("Invalid details. Book not added.")
        return

    book = {
        "title": title,
        "author": author,
        "year": int(year)
    }

    library.append(book)
    print("Book added successfully!")


def view_books():
    if not library:
        print("\nNo books in the library yet.")
        return

    print("\n--- Library Books ---")
    for i, book in enumerate(library, start=1):
        print(f"{i}. {book['title']} — {book['author']} ({book['year']})")


# ------------------------
# Main Program Loop
# ------------------------

while True:
    show_menu()
    choice = input("Enter your choice (1-3): ").strip()

    if choice == "1":
        add_book()

    elif choice == "2":
        view_books()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose 1, 2, or 3.")
        