# Скачайте файл. В нём указан адрес другого файла, который нужно скачать с
# использованием модуля requests и посчитать число строк в нём.
# Используйте функцию get для получения файла (имеет смысл вызвать метод
# strip к передаваемому параметру, чтобы убрать пробельные символы по краям).
# После получения файла вы можете проверить результат, обратившись к полю
# text. Если результат работы скрипта не принимается, проверьте поле url на
# правильность. Для подсчёта количества строк разбейте текст с помощью метода
# splitlines.
# В поле ответа введите одно число или отправьте файл, содержащий одно число.

import os
import requests

# Вывод длинны списка (строк). request.get считывает адрес из строки
# входящего файла, strip - убираем служебные символы, text - получаем
# хранящийся по url данные (строки), splitlines - создаем список (строк)
with open(os.path.join('C:', 'Users', 'Somiko', 'PycharmProjects',
                       'dataset_3378_2.txt'), 'r') as input_string:
    result = len(
        requests.get(input_string.readline().strip()).text.splitlines())

with open(os.path.join('C:', 'Users', 'Somiko', 'PycharmProjects',
                       'result.txt'), 'w') as output_string:
    output_string.write(str(result))
