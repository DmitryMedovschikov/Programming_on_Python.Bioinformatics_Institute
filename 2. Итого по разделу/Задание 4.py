# Напишите программу, на вход которой подаётся прямоугольная матрица в виде
# последовательности строк. После последней строки матрицы идёт строка,
# содержащая только строку "end" (без кавычек, см. Sample Input). Программа
# должна вывести матрицу того же размера, у которой каждый элемент в позиции
# row, column равен сумме элементов первой матрицы на позициях (row-1,
# column), (row+1, column), (row, column-1), (row, column+1). У крайних
# символов соседний элемент находится с противоположной стороны матрицы. В
# случае одной строки/столбца элемент сам себе является соседом по
# соответствующему направлению.

matrix_start = []

while True:
    matrix_str = input()
    if matrix_str == "end":
        break
    matrix_start.append([int(num) for num in matrix_str.split()])

rows = len(matrix_start)
columns = len(matrix_start[0])
matrix_result = [
    [sum([matrix_start[row - 1][column], matrix_start[(row + 1) % rows][column],
          matrix_start[row][column - 1],
          matrix_start[row][(column + 1) % columns]])
     for column in range(columns)] for row in range(rows)]

for row in range(rows):
    for column in range(columns):
        print(matrix_result[row][column], end=" ")
    print()
