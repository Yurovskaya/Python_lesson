# #  Список
# family_1 = ['Ada', 'Alex', 'Olga', 'ivan', 'Alex']
# print(family_1)
#
# # Множества
# family_2 = {'Ada', 'alex', 'Olga', 'ivan', 'Alex'}
# print(family_2)
#
# #  словарь  ключ:значение
#
# family_3 = {'Папа': 'Alex', 'Мама': 'Olga', 'Дочь': 'Ada' , 'Сын': 'Ivan'}
# print(family_3)
# print(family_3['Папа'])
# for k,v in family_3.items():
#     print(f"{k}-{v}")
#
# # Добавить в имеющийся словарь значение
#
# family_3['Бабушка'] = 'Маша'
# family_3['Дедушка'] = 'Петя'
# print(family_3)
#
# # Создание пустого словаря
# color = {}
# color['apple'] = 'green'
# color['strawberry'] = 'red'
# print(color)
#
# # Изменение значений в словаре
# color['apple'] = 'yellow'
# print(color)
#
# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'slow'}
# alien_0['speed'] = 'fast'
# print(f"Оригинальная позиция: {alien_0['x_position']}")
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3
# alien_0['x_position'] = alien_0['x_position'] + x_increment
# print(f"Новая позиция: {alien_0['x_position']}")
#
# # Удаление пар "ключ - значение"
#
# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)
# del alien_0['points']
# print(alien_0)
#
# # Словарь с однотипными объектами
#
# favorite_langauges = {
#     'Ada' : ['python', 'java'],
#     'Ivan' : 'c',
#     'Maria' : 'ruby',
#     'Petr' : 'python',
#     }
# language = favorite_langauges['Ada']
# print(f"Любимый язык програмирования это {language}")
#
#
# favorite_languages = {
#     'Ada1': ['python', 'java'],
#     'Ivan': 'c',
#     'Maria': 'ruby',
#     'Ada2': ['javascript', 'python'],
#     'Petr': 'python',
# }
#
# # Итерируем по ключам в словаре
# for person, languages in favorite_languages.items():
#     # Проверяем, является ли объект списком
#     if isinstance(languages, list):
#         print(f"{person}'s любимые языки программирования: {', '.join(languages)}")
#     else:
#         print(f"{person}'s любимый язык программирования: {languages}")
#
#
#  #  Обращение к значениям методом get()
#
# alien_0 = {'color': 'green', 'speed': 'slow',}
# point_value = alien_0.get('points',  'не содержит значения')
# print(point_value)



import random

list_ = []
a = {}
for i in range(5):
    a['x'] = random.randint(0, 100)
    list_.append(a)

print(a)