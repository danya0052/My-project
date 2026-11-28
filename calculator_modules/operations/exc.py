def get_number(text):
    while True:
        try:
            return float(input(text))
        except ValueError:
            print("Введите число!")