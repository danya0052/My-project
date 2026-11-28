from calculator_modules.operations.basic import add, subtract, multiply, divide
from calculator_modules.operations.advanced import power, square_root
from calculator_modules.operations.trigonometry import sin, cos
from calculator_modules.operations.exc import get_number

def main():
    print("Добро пожаловать в калькулятор")

    a = get_number("Введите 1 число: ")

    b = get_number("Введите 2 число: ")

    operation = input("Введите операцию (+, -, *, /, **, sqrt, sin, cos)")
    if operation == "+":
        result = add(a, b)
    elif operation == "-":
        result = subtract(a, b)
    elif operation == "*":
        result = multiply(a, b)
    elif operation == "/":
        result = divide(a, b)
    elif operation == "**":
        result = power(a, b)
    elif operation == "sqrt":
        result = square_root(a, b)
    elif operation == "sin":
        result = sin(a)
    elif operation == "cos":
        result = cos(a)

    print(f"Результат {result}")

if __name__ == "__main__":
    main()