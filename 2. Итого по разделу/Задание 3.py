# Напишите программу, которая считывает список чисел lst из первой строки
# и число x из второй строки, которая выводит все позиции, на которых
# встречается число x в переданном списке lst.
# Позиции нумеруются с нуля, если число x не встречается в списке, вывести
# строку "Отсутствует" (без кавычек, с большой буквы).
# Позиции должны быть выведены в одну строку, по возрастанию абсолютного
# значения.

num_list = [int(i) for i in input().split()]
num = int(input())
result = []

count = num_list.count(num)
if count != 0:
    position = 0
    while count != 0:
        num_index = num_list.index(num, position)
        result.append(num_index)
        position = num_index + 1
        count -= 1
else:
    print("Отсутствует")

print(*result)
