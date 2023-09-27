def seconds_to_time(seconds):
    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    return f"{days}:{hours:02}:{minutes:02}:{seconds:02}"


while True:
    user_input = input("Введите количество секунд: ")

    try:
        seconds = int(user_input)
        formatted_time = seconds_to_time(seconds)
        print(formatted_time)
        break
    except ValueError:
        print("Ошибка: Введите целое число.")