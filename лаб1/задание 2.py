text = input("Введите строку текста: ")

current_number = ''
for char in text:
    if char.isdigit():
        current_number += char
    elif current_number:
        print(current_number)
        current_number = ''

# Проверка на наличие последнего числа, если оно есть в конце строки
if current_number:
    print(current_number)
