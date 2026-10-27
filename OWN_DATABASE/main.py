
from csvReader import readStudents
from csvWriter import writeStudents
import csv


def main():
    while True:
        print("=" * 60)
        print("              Student Database Manager")
        print("=" * 60)
        print("1. ADD STUDENT")
        print("2. VIEW STUDENTS")
        print("3. EXIT")

        choice = input("Choose an option: ").strip()

        match choice:
            case "1":
                name = input("Enter the name of the student: ").strip()

                if not name:
                    print("Name cannot be empty.")
                    continue

                age_text = input("Enter the age of the student: ").strip()

                try:
                    age = int(age_text)

                    if age <= 0:
                        print("Age must be greater than zero.")
                        continue

                except ValueError:
                    print("Please enter a valid whole number.")
                    continue

                course = input("Enter the course name: ").strip()

                if not course:
                    print("Course cannot be empty.")
                    continue

                try:
                    writeStudents(name, age, course)
                except (OSError, csv.Error) as error:
                    print("Could not save student:", error)

            case "2":
                try:
                    readStudents()
                except (OSError, csv.Error) as error:
                    print("Could not read students:", error)

            case "3":
                print("Thanks for using our services!")
                return

            case _:
                print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
