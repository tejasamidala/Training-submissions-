class Student:
    def __init__(self, name, age):
        # instance variables
        self.name = name
        self.age = age
        self.grades = []  # grade list

    def add_grade(self, grade):
        # validation + error handling
        try:
            grade = float(grade)
        except ValueError:
            print("Invalid grade. Please enter a number.")
            return

        if 0 <= grade <= 100:
            self.grades.append(grade)
            print(f"Added grade {grade} for {self.name}.")
        else:
            print("Grade must be between 0 and 100.")

    def average_grade(self):
        if not self.grades:
            return None
        return sum(self.grades) / len(self.grades)

    def show_report(self):
        print("\n--- Student Report ---")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Grades:", self.grades if self.grades else "No grades yet")
        avg = self.average_grade()
        print("Average:", round(avg, 2) if avg is not None else "N/A")
        print("----------------------\n")


def main():
    print("Student Grade Manager")

    name = input("Enter student name: ").strip()
    age_input = input("Enter student age: ").strip()

    # age validation
    if not age_input.isdigit():
        print("Age must be a whole number.")
        return

    student = Student(name, int(age_input))

    while True:
        print("1) Add grade")
        print("2) Show report")
        print("3) Quit")
        choice = input("Choose (1-3): ").strip()

        if choice == "1":
            grade = input("Enter grade (0-100): ").strip()
            student.add_grade(grade)
        elif choice == "2":
            student.show_report()
        elif choice == "3":
            print("Done.")
            break
        else:
            print("Invalid choice. Pick 1, 2, or 3.")


if __name__ == "__main__":
    main()