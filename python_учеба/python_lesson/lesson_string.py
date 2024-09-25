# s = "Spam"
# print(help(s.replace))


# S = "A\0B\0C"
# print(S)
import re
match = re.match('Hello[ \t]*(.*)world', 'Hello   Python world')
print(match.group(1))


pattern = 'Hello[ \t]*(.*)world'
input_string = 'Hello   Python world'

match = re.match(pattern, input_string)

if match:
    result = match.group(1)
    print(result)
else:
    print("Сопоставление не найдено")

#  Решение квадратного уравнения на Python
# import cmath
#
# a = int(input("Введите число a: "))
# b = int(input("Введите число b: "))
# c = int(input("Введите число c: "))
#
# # Вычисляем дискриминант
# d = (b**2) - (4*a*c)
#
# # Ищем корни
# sol1 = (-b-cmath.sqrt(d))/(2*a)
# sol2 = (-b+cmath.sqrt(d))/(2*a)
#
# print('Корень 1 равен:', sol1,'Корень 2 равен: ',sol2)

import random

print(random.randint(0,9))