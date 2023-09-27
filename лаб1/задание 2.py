import re

text = input("Введите строку текста: ")
numbers = re.findall(r'\d+', text)

for number in numbers:
    print(number)