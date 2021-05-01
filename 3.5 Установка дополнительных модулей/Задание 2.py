# Имеется набор файлов, каждый из которых, кроме последнего, содержит имя
# следующего файла. Первое слово в тексте последнего файла: "We". Скачайте
# предложенный файл. В нём содержится ссылка на первый файл из этого набора.
# Все файлы располагаются в каталоге по адресу:
# https://stepic.org/media/attachments/course67/3.6.3/

import os
import requests

url = 'https://stepic.org/media/attachments/course67/3.6.3/'

with open(os.path.join('C:', 'Users', 'Somiko', 'PycharmProjects',
                       'dataset_3378_3.txt'), 'r') as input_string:
    read_text = requests.get(input_string.readline().strip()).text

while read_text[:2] != 'We':
    read_text = requests.get(url + read_text.strip()).text

with open(os.path.join('C:', 'Users', 'Somiko', 'PycharmProjects',
                       'result.txt'), 'w') as output_string:
    output_string.write(read_text)
