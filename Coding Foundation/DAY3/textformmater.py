
def main():
    print("=" * 65)
    print(" " * 25, "Text Formatter")
    print("=" * 65)

    text = input("Enter the text to format: ")

    choice = int(input(
        "Enter a number between (1-5):\n"
        "1. Uppercase\n"
        "2. Lowercase\n"
        "3. Title Case\n"
        "4. Remove spaces\n"
        "5. Count characters and words\n"
        "Your choice: "
    ))

    match choice:
        case 1:
            print(text.upper())

        case 2:
            print(text.lower())

        case 3:
            print(text.title())

        case 4:
            print(text.strip())

        case 5:
            character_count = len(text.strip())
            word_count = len(text.split())

            print(f"The number of characters is {character_count}")
            print(f"The number of words is {word_count}")

        case _:
            print("Invalid choice! Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
