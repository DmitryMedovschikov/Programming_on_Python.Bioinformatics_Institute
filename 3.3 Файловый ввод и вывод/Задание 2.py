# Напишите программу, которая считывает текст из файла (в файле может быть
# больше одной строки) и выводит самое частое слово в этом тексте, а через
# пробел то, сколько раз оно встретилось. Если таких слов несколько, вывести
# лексикографически первое (можно использовать оператор < для строк). Слова,
# написанные в разных регистрах, считаются одинаковыми.

import os

start_string = ''
dictionary = {}
max_count = 0
dictionary_max = {}
max_lex = ''

with open(os.path.join('C:', 'Users', 'Somiko', 'PycharmProjects',
                       'dataset_3363_3.txt'), 'r') as input_string:
    for line in input_string:
        start_string += line.lower().strip() + ' '
        list_start_string = start_string.split()

for word in list_start_string:
    dictionary[word] = list_start_string.count(word)
    if dictionary[word] > max_count:
        max_count = dictionary[word]
        dictionary_max = {word: list_start_string.count(word)}
    elif dictionary[word] == max_count:
        for key in dictionary:
            if key > max_lex:
                dictionary_max = {word: list_start_string.count(word)}
for key, value in dictionary_max.items():
    print(key, value)

with open(os.path.join('C:', 'Users', 'Somiko', 'PycharmProjects',
                       'dataset_3363_3.txt'), 'w') as output_string:
    for key, value in dictionary_max.items():
        output_string.write(''.join('{} {}'.format(key, value)))