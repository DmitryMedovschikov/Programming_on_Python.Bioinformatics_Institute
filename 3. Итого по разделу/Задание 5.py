# Дан файл с таблицей в формате TSV с информацией о росте школьников разных
# классов. Напишите программу, которая прочитает этот файл и подсчитает для
# каждого класса средний рост учащегося. Файл состоит из набора строк,
# каждая из которых представляет собой три поля: Класс Фамилия Рост
# Класс обозначается только числом. Буквенные модификаторы не используются.
# Номер класса может быть от 1 до 11 включительно. В фамилии нет пробелов,
# а в качестве роста используется натуральное число, но при подсчёте среднего
# требуется вычислить значение в виде вещественного числа.
# Выводить информацию о среднем росте следует в порядке возрастания номера
# класса (для классов с первого по одиннадцатый). Если про какой-то класс нет
# информации, необходимо вывести напротив него прочерк.

import os

start = []
group = 1
average_sum = 0
count = 0
finish = []

with open(os.path.join('C:', 'Users', 'Somiko', 'PycharmProjects',
                       'dataset_3380_5.txt'), 'r',
          encoding='utf-8') as input_string:
    for line in input_string:
        start.append(line.split())

while group < 12:
    for learner in start:
        if int(learner[0]) == group:
            average_sum += int(learner[2])
            count += 1
    if count == 0:
        finish.append([group, '-'])
    else:
        average_height = average_sum / count
        finish.append([group, average_height])
    count = 0
    average_sum = 0
    group += 1

with open(os.path.join('C:', 'Users', 'Somiko', 'PycharmProjects',
                       'output.txt'), 'w', encoding='utf-8') as output_string:
    for result in finish:
        output_string.write(''.join('{} {}\n'.format(*result)))
