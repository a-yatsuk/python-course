def dodawanie(a, b):
    return a + b

def odejmowanie(a, b):
    return a - b

def mnozenie(a, b):
    return a * b

def dzielenie(a, b):
    return a / b

def potegowanie(a, b):
    return a ** b

def srednia(numbers):
    return sum(numbers) / len(numbers)


def wyswietl_menu():
    print("""
========== CALCULATOR ==========
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exponentiation
6. Average
0. Exit
================================
""")


def main():
    while True:
        wyswietl_menu()

        option = input("Choose an option: ")

        if option == "0":
            print("Goodbye!")
            break

        elif option in ["1", "2", "3", "4", "5"]:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if option == "1":
                result = dodawanie(a, b)

            elif option == "2":
                result = odejmowanie(a, b)

            elif option == "3":
                result = mnozenie(a, b)

            elif option == "4":
                if b == 0:
                    print("Cannot divide by zero!")
                    continue

                result = dzielenie(a, b)

            elif option == "5":
                result = potegowanie(a, b)

            print(f"Result: {result}")

        elif option == "6":
            numbers = []

            n = int(input("How many numbers? "))

            for i in range(n):
                number = float(input(f"Number {i + 1}: "))
                numbers.append(number)

            result = srednia(numbers)
            print(f"Average: {result}")

        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()