
# This file is used to display the data

import csv
from pathlib import Path

FILE_PATH = Path(__file__).with_name("students.csv")


def readStudents():
    if not FILE_PATH.exists():
        print("CSV file not found.")
        return

    try:
        with FILE_PATH.open(
            "r",
            newline="",
            encoding="utf-8"
        ) as file:
            reader = csv.DictReader(file)
            found_student = False

            for student in reader:
                found_student = True

                print(
                    f"Name: {student['Name']} | "
                    f"Age: {student['Age']} | "
                    f"Course: {student['Course']}"
                )

            if not found_student:
                print("No students found.")

    except (OSError, csv.Error) as error:
        print("Could not read the CSV file:", error)


if __name__ == "__main__":
    readStudents()
