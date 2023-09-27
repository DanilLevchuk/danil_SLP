def sum_until_negative(numbers):
    total = 0
    for num in numbers:
        if num < 0:
            break
        total += num
    return total

my_tuple = ()
while True:
    input_str = input("Введите элемент кортежа (число) или 'exit' для завершения ввода: ")
    if input_str.lower() == 'exit':
        break

    if input_str.isdigit() or (input_str[0] == '-' and input_str[1:].isdigit()):
        my_tuple += (int(input_str),)
    else:
        print("Ошибка: Введите целое число или 'exit' для завершения ввода.")

result = sum_until_negative(my_tuple)
print(f"Сумма элементов до первого отрицательного: {result}")
