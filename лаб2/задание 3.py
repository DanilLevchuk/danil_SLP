def find_negative_column_average(matrix):
    if not matrix:
        return None
    rows, cols = len(matrix), len(matrix[0])
    for j in range(cols):
        all_negative = True
        column_sum = 0
        for i in range(rows):
            if matrix[i][j] >= 0:
                all_negative = False
                break
            column_sum += matrix[i][j]
        if all_negative:
            return column_sum / rows
    return None


# Ввод матрицы с клавиатуры
try:
    rows = int(input("Введите количество строк матрицы: "))
    cols = int(input("Введите количество столбцов матрицы: "))

    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Введите элемент матрицы [{i}][{j}]: "))
            row.append(element)
        matrix.append(row)

    print("Матрица:")
    for row in matrix:
        print(row)

    result = find_negative_column_average(matrix)
    if result is not None:
        print(f"Среднее арифметическое элементов первого отрицательного столбца: {result}")
    else:
        print("Нет отрицательных столбцов в матрице.")
except ValueError:
    print("Ошибка: Введите целые числа для элементов матрицы.")
