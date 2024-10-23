# В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами.
# За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов.
# Выведите наименьшее число парт, которое нужно приобрести для них.
#
# Программа получает на вход три натуральных числа: количество учащихся в каждом из трех классов (числа не превышают 1000).

import math

students_1 = int(input())
students_2 = int(input())
students_3 = int(input())
# Одна парта равно 2 ученика
# Находим сколько парт нужно для каждого класса, а потом получившиеся значения суммируем и узнаем общее количество парт
desk_1 = students_1 / 2
table_1 = math.ceil(desk_1)
desk_2 = students_2 / 2
table_2 = math.ceil(desk_2)
desk_3 = students_3 / 2
table_3 = math.ceil(desk_3)

desk = table_1 + table_2 + table_3
print(desk)
