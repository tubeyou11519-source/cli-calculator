def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Cannot divide by zero"
        return num1 / num2
    elif operator == '%':
        if num2 == 0:
            return "Error: Cannot divide by zero"
        return num1 % num2
    elif operator == '**':
        return num1 ** num2
    else:
        return "Error: Unknown operator"

def main():
    print("Simple Calculator")
    print("Operators: + - * / % ** (type 'quit' to exit)")

    while True:
        first_input = input("\nEnter first number (or 'quit'): ")
        if first_input.lower() == 'quit':
            print("Goodbye!")
            break

        try:
            num1 = float(first_input)
            operator = input("Enter operator (+, -, *, /, %, **): ")
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Error: Please enter valid numbers.")
            continue

        result = calculate(num1, num2, operator)
        print(f"Result: {result}")

if __name__ == "__main__":
    main()