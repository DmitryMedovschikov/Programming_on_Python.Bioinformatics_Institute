# Ранее было задание сжать строку, используя кодирование повторов. Теперь
# необходимо сделать наоборот. Напишите программу, которая считывает из файла
# строку, соответствующую тексту, сжатому с помощью кодирования повторов, и
# производит обратную операцию, получая исходный текст. Запишите полученный
# текст в файл. В исходном тексте не встречаются цифры, так что код однозначно
# интерпретируем.

import os

middle_list = []
num_list = []
count = 0
score_num = ''

with open(os.path.join('C:', 'Users', 'Somiko', 'PycharmProjects',
                       'dataset_3363_2.txt'), 'r') as input_string:
    start_list = input_string.readline().strip()

for ind, symbol in enumerate(start_list):
    if symbol.isdigit() and ind == len(start_list) - 1 and count == 0:
        middle_list.append(symbol)
    elif symbol.isdigit() and ind == len(start_list) - 1 and count != 0:
        num_list.append(symbol)
        for num in num_list:
            score_num += num
        middle_list.append(score_num)
    elif symbol.isdigit():
        num_list.append(symbol)
        count += 1
    elif symbol.isalpha() and count == 0:
        middle_list.append(symbol)
    else:
        for num in num_list:
            score_num += num
        middle_list.append(score_num)
        middle_list.append(symbol)
        num_list.clear()
        score_num = ''
        count = 0

output_string = ''

for ind, num in enumerate(middle_list):
    if ind % 2 == 0:
        decode = middle_list[ind] * int(middle_list[ind + 1])
        output_string += decode

with open(os.path.join('C:', 'Users', 'Somiko', 'PycharmProjects',
                       'dataset_3363_2.txt'), 'w') as s:
    s.write(output_string)
