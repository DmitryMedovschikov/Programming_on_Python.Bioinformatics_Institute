# Напишите программу, которая считывает с консоли числа (по одному в строке)
# до тех пор, пока сумма введённых чисел не будет равна 0 и сразу после этого
# выводит сумму квадратов всех считанных чисел.

num = int(input())
sum_num = 0
sum_square = 0
num_list = []

while True:
    num_list.append(num**2)
    sum_num += num
    if sum_num == 0:
        break
    num = int(input())

for number in num_list:
    sum_square += number

print(sum_square)
