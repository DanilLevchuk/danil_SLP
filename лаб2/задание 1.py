def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def prime(n):
    if n <= 0:
        return None
    prime_count = 0
    num = 2
    while True:
        if is_prime(num):
            prime_count += 1
            if prime_count == n:
                return num
        num += 1

while True:
    try:
        n = int(input("Введите номер простого числа: "))
        if n <= 0:
            print("Номер должен быть положительным числом.")
        else:
            result = prime(n)
            if result is not None:
                print(f"{n}-е простое число: {result}")
                break  # Выход из цикла при правильном вводе
            else:
                print("Что-то пошло не так при поиске простого числа.")
    except ValueError:
        print("Ошибка: Введите целое положительное число.")
