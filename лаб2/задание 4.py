def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Ошибка: деление на ноль")
        return None
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None
    finally:
        print("Выполнение блока finally")
    return result


try:
    a = float(input("Введите число a: "))
    b = float(input("Введите число b: "))

    result = divide_numbers(a, b)
    if result is not None:
        print(f"Результат деления {a} на {b} равен: {result}")
except ValueError:
    print("Ошибка: Введите числа.")
