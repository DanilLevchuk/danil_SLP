def process_data(data):
    if isinstance(data, list):
        even_count = len([x for x in data if x % 2 == 0])
        max_num = max(data)
        data = [x for x in data if x >= 0]
        return {
            "Even Count": even_count,
            "Max Number": max_num,
            "Updated List": data
        }
    elif isinstance(data, dict):
        sorted_dict = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))
        return sorted_dict
    elif isinstance(data, int):
        return int(str(data)[::-1])
    elif isinstance(data, str):
        char_count = {}
        for char in data:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        return char_count
    else:
        return None

# Ввод данных с клавиатуры
user_input = input("Введите данные (список, словарь, число или строку): ")

try:
    # Попробуйте интерпретировать ввод как различные типы данных
    eval_data = eval(user_input)
    result = process_data(eval_data)
    if result is not None:
        print(result)
    else:
        print("Не удалось обработать введенные данные.")
except Exception as e:
    print(f"Произошла ошибка: {e}")
