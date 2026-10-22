
import re


# ---------------- CALCULATOR ----------------

def calculator():
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
    except ValueError:
        print("Error: Please enter valid numbers.")
        return

    print("-" * 60)
    print(
        "Choose an operation:\n"
        "1. Addition\n"
        "2. Subtraction\n"
        "3. Multiplication\n"
        "4. Division\n"
        "5. Find remainder"
    )
    print("-" * 60)

    try:
        choice = int(input("Enter your choice (1-5): "))
    except ValueError:
        print("Invalid choice!")
        return

    match choice:
        case 1:
            print("Result:", a + b)

        case 2:
            print("Result:", a - b)

        case 3:
            print("Result:", a * b)

        case 4:
            if b == 0:
                print("Error: Cannot divide by zero.")
            else:
                print("Result:", a / b)

        case 5:
            if b == 0:
                print("Error: Cannot find remainder with zero.")
            else:
                print("Result:", a % b)

        case _:
            print("Invalid operator!")


# ---------------- INPUT PARSER ----------------

def parse_value(user_input):
    match = re.fullmatch(
        r"([-+]?\d+(?:\.\d+)?)\s*([a-zA-Z]+)",
        user_input.strip()
    )

    if match:
        value = float(match.group(1))
        unit = match.group(2)
        return value, unit

    return None, None


# ---------------- LENGTH CONVERTER ----------------

def findLength():
    units = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1,
        "km": 1000,
        "in": 0.0254,
        "ft": 0.3048
    }

    print("\nAvailable units: mm, cm, m, km, in, ft")

    user_input = input("Enter initial value (e.g., 500m): ")
    value, unitFrom = parse_value(user_input)

    if value is None:
        print("Invalid input! Example: 500m")
        return

    unitFrom = unitFrom.lower()
    unitTo = input("Enter destination unit: ").strip().lower()

    if unitFrom not in units or unitTo not in units:
        print("Invalid unit!")
        return

    result = value * units[unitFrom] / units[unitTo]

    print(f"Result: {value:g}{unitFrom} = {result:g}{unitTo}")


# ---------------- WEIGHT CONVERTER ----------------

def findWeight():
    units = {
        "mg": 0.000001,
        "g": 0.001,
        "kg": 1,
        "lb": 0.45359237
    }

    print("\nAvailable units: mg, g, kg, lb")

    user_input = input("Enter initial value (e.g., 5kg): ")
    value, unitFrom = parse_value(user_input)

    if value is None:
        print("Invalid input! Example: 5kg")
        return

    unitFrom = unitFrom.lower()
    unitTo = input("Enter destination unit: ").strip().lower()

    if unitFrom not in units or unitTo not in units:
        print("Invalid unit!")
        return

    result = value * units[unitFrom] / units[unitTo]

    print(f"Result: {value:g}{unitFrom} = {result:g}{unitTo}")


# ---------------- TEMPERATURE CONVERTER ----------------

def findTemperature():
    print("\nAvailable units: C, F, K")

    user_input = input("Enter initial temperature (e.g., 100C): ")
    value, unitFrom = parse_value(user_input)

    if value is None:
        print("Invalid input! Example: 100C")
        return

    unitFrom = unitFrom.upper()
    unitTo = input("Enter destination unit: ").strip().upper()

    if unitFrom not in ("C", "F", "K") or unitTo not in ("C", "F", "K"):
        print("Invalid unit!")
        return

    # Convert the original temperature to Celsius.
    if unitFrom == "C":
        celsius = value
    elif unitFrom == "F":
        celsius = (value - 32) * 5 / 9
    else:
        celsius = value - 273.15

    # Convert Celsius to the destination unit.
    if unitTo == "C":
        result = celsius
    elif unitTo == "F":
        result = celsius * 9 / 5 + 32
    else:
        result = celsius + 273.15

    print(f"Result: {value:g}{unitFrom} = {result:.2f}{unitTo}")


# ---------------- UNIT CONVERTER MENU ----------------

def unitConverter():
    print("=" * 60)
    print("                   UNIT CONVERTER")
    print("=" * 60)

    print(
        "1. Length\n"
        "2. Weight\n"
        "3. Temperature"
    )

    try:
        choice = int(input("Enter your choice (1-3): "))
    except ValueError:
        print("Invalid choice!")
        return

    match choice:
        case 1:
            findLength()

        case 2:
            findWeight()

        case 3:
            findTemperature()

        case _:
            print("Invalid option!")


# ---------------- MAIN MENU ----------------

def main():
    while True:
        print("\n" + "=" * 60)
        print("          CALCULATOR AND UNIT CONVERTER")
        print("=" * 60)

        print(
            "1. Use Calculator\n"
            "2. Use Unit Converter\n"
            "3. Exit"
        )

        try:
            choice = int(input("Enter your choice (1-3): "))
        except ValueError:
            print("Invalid input! Enter a number.")
            continue

        match choice:
            case 1:
                calculator()

            case 2:
                unitConverter()

            case 3:
                print("Thank you for using the program!")
                break

            case _:
                print("Invalid choice! Select 1, 2, or 3.")


if __name__ == "__main__":
    main()
