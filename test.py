class NegativeNumberError(Exception):
    pass

def square_root(x):
    if x < 0:
        raise NegativeNumberError("Ошибка: Корень из отрицательного числа не определен")
    return x ** 0.5
try:
    num = int(input())
    result = square_root(num)
    print(result)

except NegativeNumberError as e:
    print(e)
except ValueError:
    print("Ошибка: введено не число")












try:
    # В этом блоке мы пишем код, который может вызвать ошибку
    a = 12
    b = 0
    result = a / b
except TypeError:
    # В этом блоке указываем как обработать ошибку
    print("Ошибка: введено не число")
except ZeroDivisionError:
    # В этом блоке указываем как обработать ошибку
    print("Ошибка: Деление на 0 невозможно")
else:
    # Результат выполнения блока try без ошибок
    print (f"результат: {result}")
finally:
    # Выполняется в любом случае
    print("Программа завершена")


