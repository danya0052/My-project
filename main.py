from calculator_modules.operations.basic import add, subtract, multiply, divide
from calculator_modules.operations.basic import power,  square_root
from calculator_modules.operations.trigonometry import sin, cos, tan

def main():
    print ("Добро пожаловать в калькулятор")
    a = float (input("Введите 1 число: "))
    b = float (input("Введите 2 число: "))
    operation = input("Введите операцию(+, -, *, /)")
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
        result =  square_root(a, b)
    elif operation == "sin":
            result =  sin(a)
    elif operation == "cos":
            result =  cos(a)
    elif operation == "tan":
            result =  tan(a)

    print(f"Результат{result}")

if __name__ == "__main__":
    main()

     