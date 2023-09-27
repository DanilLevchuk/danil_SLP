text = input("Введите строку текста: ")

current_number = ''
for char in text:
    if char.isdigit():
        current_number += char
    elif current_number:
        print(current_number)
        current_number = ''

if current_number:
    print(current_number)
