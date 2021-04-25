# Выведите таблицу размером n×n, заполненную числами от 1 до n^2
# по спирали, выходящей из левого верхнего угла и закрученной по часовой
# стрелке, как показано в примере (n=5):
# 1  2  3  4  5
# 16 17 18 19 6
# 15 24 25 20 7
# 14 23 22 21 8
# 13 12 11 10 9

n = int(input())
matrix_nn = [[0 for column in range(n)] for row in range(n)]
number = 1
count_table = 0

while number <= n * n:

    for right in range(count_table, n - count_table):
        matrix_nn[count_table][right] = number
        number += 1
    for down in range(count_table + 1, n - count_table):
        matrix_nn[down][n - count_table - 1] = number
        number += 1
    for left in range(n - count_table - 2, count_table - 1, -1):
        matrix_nn[n - count_table - 1][left] = number
        number += 1
    for up in range(n - 2 - count_table, count_table, -1):
        matrix_nn[up][count_table] = number
        number += 1
    count_table += 1

for row in range(n):
    for column in range(n):
        print(matrix_nn[row][column], end=' ')
    print()
