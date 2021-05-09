# Напишите программу, которая умеет шифровать и расшифровывать шифр
# подстановки. Программа принимает на вход две строки одинаковой длины,
# на первой строке записаны символы исходного алфавита, на второй строке —
# символы конечного алфавита, после чего идёт строка, которую нужно
# зашифровать переданным ключом, и ещё одна строка, которую нужно расшифровать.
#
# Пусть, например, на вход программе передано:
# abcd
# *d%#
# abacabadaba
# #*%*d*%
#
# Это значит, что символ a исходного сообщения заменяется на символ * в
# шифре, b заменяется на d, c — на % и d — на #. Нужно зашифровать строку
# abacabadaba и расшифровать строку #*%*d*% с помощью этого шифра. Получаем
# следующие строки, которые и передаём на вывод программы: *d*%*d*#*d* dacabac

strings_for_chiper = 2
list_strings = []
dict_for_chiper = {}

while not strings_for_chiper == 0:
    list_strings.append(input())
    strings_for_chiper -= 1

for i in range(len(list_strings) - 1):
    for j in range(len(list_strings[i])):
        dict_for_chiper[list_strings[i][j]] = list_strings[i + 1][j]

string_for_encryption = input()
string_for_decryption = input()


def func_encryption(input_string):
    encryption_string = ''
    for i in input_string:
        for key in dict_for_chiper.keys():
            if i == key:
                encryption_string += dict_for_chiper[key]
    return encryption_string


def func_decryption(input_string):
    decryption_string = ''
    for i in input_string:
        for key, value in dict_for_chiper.items():
            if i == value:
                decryption_string += key
    return decryption_string


print(func_encryption(string_for_encryption))
print(func_decryption(string_for_decryption))
