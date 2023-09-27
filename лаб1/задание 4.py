def merge_dicts(*dicts):
    result = {}
    for d in dicts:
        result.update(d)
    return result


merged_dict = {}

while True:
    try:
        key = input("Введите ключ (или 'exit' для завершения ввода): ")
        if key.lower() == '':
            break

        value = input(f"Введите значение для ключа '{key}': ")

        try:
            value = int(value)
        except ValueError:
            pass

        merged_dict[key] = value
    except KeyboardInterrupt:
        print("\nВвод прерван.")
        break

print("Объединенный словарь:")
print(merged_dict)