# Простейшая система проверки орфографии может быть основана на использовании
# списка известных слов. Если введённое слово не найдено в этом списке,
# оно помечается как "ошибка".
#
# На вход программе первой строкой передаётся количество d известных нам
# слов, после чего на d строках указываются эти слова. Затем передаётся
# количество l строк текста для проверки, после чего l строк текста.
#
# Выведите уникальные "ошибки" в произвольном порядке. Работу производите без
# учёта регистра.

words = set()
text = set()
list_text = []

quantity_words = int(input())

while quantity_words != 0:
    words.add(input().lower())
    quantity_words -= 1

quantity_text = int(input())

while quantity_text != 0:
    list_text.append(input().lower().split(' '))
    quantity_text -= 1

for number in list_text:
    for word in number:
        text.add(word)

text.difference_update(words)

for word in text:
    print(word)
