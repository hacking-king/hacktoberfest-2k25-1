# Simple Calculator
def read_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Please try again.")

def calculator():
    print("Welcome to Python Calculator!")
    print("Operations: +, -, *, /, ** (power), % (modulo)")
    while True:
        a = read_number("Enter first number: ")
        op = input("Enter operation (+, -, *, /, **, %): ")
        b = read_number("Enter second number: ")

        if op == '+':
            print("Result:", a + b)
        elif op == '-':
            print("Result:", a - b)
        elif op == '*':
            print("Result:", a * b)
        elif op == '/':
            if b != 0:
                print("Result:", a / b)
            else:
                print("Error: Division by zero!")
        elif op == '**' or op == '^':
            print("Result:", a ** b)
        elif op == '%':
            try:
                print("Result:", a % b)
            except ZeroDivisionError:
                print("Error: Modulo by zero!")
        else:
            print("Invalid operation! Supported: +, -, *, /, **, %")

        choice = input("Do you want to continue? (y/n): ")
        if choice.lower() != 'y':
            break

calculator()
