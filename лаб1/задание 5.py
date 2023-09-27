jewelry_store = {
    'Кольцо': ['Золото', 5000, 10],
    'Серьги': ['Серебро', 2000, 20],
    'Браслет': ['Золото', 8000, 5],
    'Подвеска': ['Платина', 10000, 8]
}

while True:
    print("\nМеню:")
    print("1. Просмотр описания")
    print("2. Просмотр цены")
    print("3. Просмотр количества")
    print("4. Вся информация")
    print("5. Покупка")
    print("6. Выход")

    choice = input("Введите номер пункта меню: ")

    if choice == '1':
        item_name = input("Введите название изделия: ")
        if item_name in jewelry_store:
            print(f"{item_name} - {jewelry_store[item_name][0]}")
        else:
            print("Такого изделия нет в магазине.")
    elif choice == '2':
        item_name = input("Введите название изделия: ")
        if item_name in jewelry_store:
            print(f"{item_name} - {jewelry_store[item_name][1]} рублей")
        else:
            print("Такого изделия нет в магазине.")
    elif choice == '3':
        item_name = input("Введите название изделия: ")
        if item_name in jewelry_store:
            print(f"{item_name} - {jewelry_store[item_name][2]} штук")
        else:
            print("Такого изделия нет в магазине.")
    elif choice == '4':
        for item, details in jewelry_store.items():
            print(f"{item}: {details[0]}, Цена: {details[1]} рублей, Количество: {details[2]} штук")
    elif choice == '5':
        item_name = input("Введите название изделия: ")
        if item_name in jewelry_store:
            quantity = int(input("Введите количество: "))
            if quantity <= jewelry_store[item_name][2]:
                cost = quantity * jewelry_store[item_name][1]
                jewelry_store[item_name][2] -= quantity
                print(f"Вы приобрели {quantity} штук {item_name} за {cost} рублей.")
            else:
                print("Такого количества нет в магазине.")
        else:
            print("Такого изделия нет в магазине.")
    elif choice == '6':
        print("До свидания!")
        break
    else:
        print("Неверный выбор. Попробуйте еще раз.")
