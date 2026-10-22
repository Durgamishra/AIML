def checkGrade(mark):
    if mark < 0 or mark > 100:
        print("Invalid marks!")

    elif mark >= 90:
        print("Grade A")

    elif mark >= 80:
        print("Grade B")

    elif mark >= 70:
        print("Grade C")

    elif mark >= 60:
        print("Grade D")

    elif mark >= 50:
        print("Grade E")

    elif mark >= 40:
        print("Grade F")

    elif mark >= 33:
        print("Grade G")

    else:
        print("Fail")


def main():
    print("=" * 60)
    print(" " * 20 + "Grade Checker")
    print("=" * 60)

    try:
        mark = int(input("Enter the marks: "))
        checkGrade(mark)
    except ValueError:
        print("Please enter a valid whole number!")


if __name__ == "__main__":
    main()
