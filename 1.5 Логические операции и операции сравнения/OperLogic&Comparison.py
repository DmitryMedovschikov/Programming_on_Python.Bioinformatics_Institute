# Расставьте скобки в выражении: a and b or not a and not b
# В соответствии с порядком вычисления выражения (приоритетом операций).

# Ответ: ((a and b) or ((not a) and (not b)))

# Выполните код в интерпретаторе Python 3:
# x = 5
# y = 10
# y > x * x or y >= 2 * x and x < y
# Постарайтесь разобраться, почему интерпретатор выдал именно такой ответ.
# Помните, что любые арифметические операции выше по приоритету операций
# сравнения и логических операторов.

x = 5
y = 10
print(y > x * x or y >= 2 * x and x < y)
# x*x=25, 2*x=10, 10>25=False, 10>=10=True, 5<10=True, True and True = True,
# False or True = True

# Найдите результат выражения для заданных значений a и b:
# a = True
# b = False
# a and b or not a and not b

a = True
b = False
print(a and b or not a and not b)
