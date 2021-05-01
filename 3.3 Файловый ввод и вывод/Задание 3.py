# Имеется файл с данными по успеваемости абитуриентов. Он представляет из
# себя набор строк, где в каждой строке записана следующая информация:
# Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку
# Поля внутри строки разделены точкой с запятой, оценки — целые числа.
# Напишите программу, которая считывает исходный файл с подобной структурой и
# для каждого абитуриента записывает его среднюю оценку по трём предметам на
# отдельной строке, соответствующей этому абитуриенту, в файл с ответом.
# Также вычислите средние баллы по математике, физике и русскому языку по
# всем абитуриентам и добавьте полученные значения, разделённые пробелом,
# последней строкой в файл с ответом.

import os

rating_enrol_sum = 0
rating_math_sum = 0
rating_physic_sum = 0
rating_rus_sum = 0
list_enrollee_start = []
list_enrollee_result = []
list_enrollee_result_all = []

with open(os.path.join('C:', 'Users', 'Somiko', 'PycharmProjects',
                       'dataset_3363_4.txt'), 'r',
          encoding='utf-8') as input_string:
    for line in input_string:
        list_enrollee_start.append(line.strip().split(';'))

for enrol in range(len(list_enrollee_start)):
    for eval in range(len(list_enrollee_start[enrol])):
        if eval > 0:
            rating_enrol_sum += int(list_enrollee_start[enrol][eval])
            if eval == 1:
                rating_math_sum += int(list_enrollee_start[enrol][eval])
            elif eval == 2:
                rating_physic_sum += int(list_enrollee_start[enrol][eval])
            elif eval == 3:
                rating_rus_sum += int(list_enrollee_start[enrol][eval])
    list_enrollee_result.append(rating_enrol_sum / 3)
    rating_enrol_sum = 0
list_enrollee_result_all.append(rating_math_sum / len(list_enrollee_start))
list_enrollee_result_all.append(rating_physic_sum / len(list_enrollee_start))
list_enrollee_result_all.append(rating_rus_sum / len(list_enrollee_start))

with open(os.path.join('C:', 'Users', 'Somiko', 'PycharmProjects',
                       'dataset_3363_4.txt'), 'w',
          encoding='utf-8') as output_string:
    for rait in list_enrollee_result:
        output_string.write(''.join('{}\n'.format(rait)))
    for rait in list_enrollee_result_all:
        output_string.write(''.join('{} '.format(rait)))
