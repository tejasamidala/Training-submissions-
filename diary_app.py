from datetime import datetime

DIARY_FILE = "my_diary.txt"


def show_menu():
    print("\nDiary Menu:")
    print("1. Write a new entry")
    print("2. View all entries")
    print("3. Search entries")
    print("4. Exit")


def write_entry():
    print("\nWrite your diary entry (press Enter on empty line to finish):")
    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)

    if not lines:
        print("No text entered. Entry not saved.")
        return

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    entry_text = "\n".join(lines)

    # append mode + encoding + context manager
    with open(DIARY_FILE, "a", encoding="utf-8") as f:
        f.write(f"\n--- {timestamp} ---\n")
        f.write(entry_text + "\n")

    print("Saved.")


def view_entries():
    try:
        with open(DIARY_FILE, "r", encoding="utf-8") as f:
            content = f.read().strip()
        if not content:
            print("\nDiary is empty.")
        else:
            print("\n--- All Entries ---")
            print(content)
    except FileNotFoundError:
        print("\nNo diary file yet. Write your first entry!")


def search_entries():
    keyword = input("Enter a keyword to search: ").strip().lower()
    if not keyword:
        print("No keyword entered.")
        return

    try:
        with open(DIARY_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("No diary file yet.")
        return

    # simple search: show matching lines + nearby header
    print("\n--- Search Results ---")
    found = False
    current_header = ""
    for line in lines:
        if line.startswith("--- ") and line.strip().endswith(" ---"):
            current_header = line.strip()
        if keyword in line.lower():
            found = True
            print(current_header)
            print(line.strip())
            print("-" * 25)

    if not found:
        print("No matches found.")


def main():
    print("Personal Diary App")
    while True:
        show_menu()
        choice = input("Enter choice (1-4): ").strip()

        if choice == "1":
            write_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            search_entries()
        elif choice == "4":
            print("Bye.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
    