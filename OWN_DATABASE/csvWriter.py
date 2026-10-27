
# This writes and updates the CSV file

import csv
from pathlib import Path

FILE_PATH = Path(__file__).with_name("students.csv")


def writeStudents(name, age, course):
    file_exists = FILE_PATH.exists()
    need_header = (
        not file_exists or FILE_PATH.stat().st_size == 0
    )

    with FILE_PATH.open(
        "a",
        newline="",
        encoding="utf-8"
    ) as file:
        writer = csv.writer(file)

        if need_header:
            writer.writerow(["Name", "Age", "Course"])

        writer.writerow([name, age, course])

    print("Student saved successfully!")


if __name__ == "__main__":
    writeStudents("Rahul", 20, "BCA")
