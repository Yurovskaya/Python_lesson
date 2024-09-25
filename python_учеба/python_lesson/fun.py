# num_1 = 10
# num_2 = 20
# result = num_1 + num_2
# print(result)

#
# def summ(num_1, num_2):
#     result = num_1 + num_2
#     print(result)
# summ(10, 20)
# summ(30, 40)
#
# name = input("Введите имя: ")
# age = input("Введите ваш возраст: ")
# def hi(name, age):
#     result = name + " " + age
#     return result
#     # print("Меня зовут "+ name + " мне " + age + " лет")
# h = hi(name,age)
# print(h)

# Возвращение словаря
def build_person(first_name, last_name, age =None):
    person = {'first': 'first_name', 'last': 'last_name'}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=29)
print(musician)

# Передача списка в функцию
def greet_user(names):
    for name in names:
        msg = f'Привет, {name.title()}!'
        print(msg)

usermame = ['Даша', 'Маша','Иван']

greet_user(usermame)

# Изменение списка в функции

# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []
#
# while unprinted_designs:
#     current_designs = unprinted_designs.pop()
#     print(f"Printing model: {current_designs}")
#     completed_models.append(current_designs)
#
# print("\n The following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)


# def print_models(unprinted_designs,completed_models):
#     while unprinted_designs:
#         current_designs = unprinted_designs.pop()
#         print(f"Printing model: {current_designs}")
#         completed_models.append(current_designs)
#
# def show_completed_models(completed_models):
#     print("\n The following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)
#
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []
#
# print_models(unprinted_designs,completed_models)
# show_completed_models(completed_models)

# Заперт изменения списка в функции
#
# Несмотря на то, что  передача копии позволяет сохранить содержимое списка
# обычно функциям следует передавать исходный список
def print_models(unprinted_designs,completed_models):
    while unprinted_designs:
        current_designs = unprinted_designs.pop()
        print(f"Printing model: {current_designs}")
        completed_models.append(current_designs)

def show_completed_models(completed_models):
    print("\n The following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:],completed_models)
show_completed_models(completed_models)

#  Передача произвольного набора аргументов

def make_pizza(*toppings):
    """Вывод списка заказанных топпингов"""
    print("\n Making a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('pepperoni','cheese', 'pepper','basil')

# Позиционные аргументы с произвольными наборами аргументов

def make_pizza(size, *toppings):
    """Вывод списка заказанных топпингов"""
    print(f"\n Making a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16,'pepperoni')
make_pizza(32, 'pepperoni','cheese', 'pepper','basil')

# Использование произвольного набора именнованных аргументов

def build_profile(first, last, **user_info):
    """Строит словарь с информацией о пользователе"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', location='priceton', field='physics')
print(user_profile)


def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Вызываем функцию с различными именованными аргументами
print_info(name='John', age=25, city='New York')