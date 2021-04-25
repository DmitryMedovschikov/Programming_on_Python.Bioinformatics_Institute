# Напишите функцию modify_list(l), которая принимает на вход список целых
# чисел, удаляет из него все нечётные значения, а чётные нацело делит на два.
# Функция не должна ничего возвращать, требуется только изменение переданного
# списка, например:
#
# lst = [1, 2, 3, 4, 5, 6]
# print(modify_list(lst))  # None
# print(lst)               # [1, 2, 3]
# modify_list(lst)
# print(lst)               # [1]
#
# lst = [10, 5, 8, 3]
# modify_list(lst)
# print(lst)               # [5, 4]

lst = [11, 8, 2, 6, 7, 4, 9, 3, 3, 10]


def modify_list(l):
    i = 0
    while i < len(l):
        if l[i] % 2 == 1:
            del l[i]
        else:
            l[i] //= 2
            i += 1
    return


modify_list(lst)
print(lst)
