def get_number():
    while True:
        try:
            return float(input())
        except ValueError:
            print("Введите число!")