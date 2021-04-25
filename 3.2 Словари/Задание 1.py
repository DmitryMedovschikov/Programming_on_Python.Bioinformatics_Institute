# Напишите функцию update_dictionary(d, key, value), которая принимает на
# вход словарь d и два числа: key и value. Если ключ key есть в словаре d,
# то добавьте значение value в список, который хранится по этому ключу. Если
# ключа key нет в словаре, то нужно добавить значение в список по ключу 2 ∗
# key. Если и ключа 2 ∗ key нет, то нужно добавить ключ 2 ∗ key в словарь и
# сопоставить ему список из переданного элемента [value].
# Пример работы функции:
# d = {}
# print(update_dictionary(d, 1, -1))  # None
# print(d)                            # {2: [-1]}
# update_dictionary(d, 2, -2)
# print(d)                            # {2: [-1, -2]}
# update_dictionary(d, 1, -3)
# print(d)                            # {2: [-1, -2, -3]}

d = {2: [-1, -2]}


def update_dictionary(d, key, value):
    if key in d:
        a = d[key]
        a.append(value)
        d[key] = a
    elif key * 2 in d:
        a = d[key * 2]
        a.append(value)
        d[key * 2] = a
    else:
        d[key * 2] = [value]

    return d


print(update_dictionary(d, 1, -3))
