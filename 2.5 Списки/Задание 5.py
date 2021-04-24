# Напишите программу, которая принимает на вход список чисел в одной строке и
# выводит на экран в одну строку значения, которые встречаются в нём более
# одного раза. Для решения задачи может пригодиться метод sort списка.
# Выводимые числа не должны повторяться, порядок их вывода может быть
# произвольным.

list_num = [int(i) for i in input().split()]
list_num.sort()
list_num_end = []

for i in range(len(list_num)):
    if i < 1:
        continue
    elif list_num[i] == list_num[i-1]:
        if list_num[i] not in list_num_end:
            list_num_end.append(list_num[i])
    else:
        continue

print(*list_num_end)