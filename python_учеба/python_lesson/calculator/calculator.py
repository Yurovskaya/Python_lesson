# Напишите проект "Калькулятор".
#
# Инструкции к заданию:
#
# Напишите скрипт "калькулятор", который будет принимать от пользователя на вход:
#
# 1-е число
#
# арифметический знак, один из: +, -, *, /
#
# 2-е число
#
# производить сложение, вычитание, умножение или деление, в зависимости от введенного знака
#
# А так же предусмотрите проверку на то, что на ноль делить нельзя. И другие виды некорректно введенных данных.
#
# Данное задание Вам необходимо выполнить самостоятельно и стараться не пользоваться сторонними источниками

import Calculation


def arithmetic_sign(arithmetic, num_1, num_2):
    arithmetic_sign_list = ['-', '+', '*', '/', '**']

    if arithmetic in arithmetic_sign_list:
        if arithmetic == '+':
            result = Calculation.sum(num_1, num_2)
        elif arithmetic == '-':
            result = Calculation.sub(num_1, num_2)
        elif arithmetic == '/':
            result = Calculation.div(num_1, num_2)
        elif arithmetic == '*':
            result = Calculation.mult(num_1, num_2)
        elif arithmetic == '**':
            result = Calculation.exponentiation(num_1, num_2)

        return result

while True:
    try:
        num_1 = float(input("Введите число: "))
        num_2 = float(input("Введите число: "))
        arithmetic = input("Введите арифметический знак: ")

        if arithmetic in ['-', '+', '*', '/', '**']:
            break  # Если ввод успешен и арифметический знак существует, выходим из цикла
        else:
            print("Ошибка! Вы ввели несуществующий арифметический знак. Пожалуйста, повторите ввод.")
    except ValueError:
        print("Ошибка! Введенное значение не является числом. Пожалуйста, повторите ввод.")

result = arithmetic_sign(arithmetic, num_1, num_2)
# Для заданной точности число округляется до значащих цифр,
# а затем форматируется результат либо в формате с фиксированной запятой,
# либо в экспоненциальном представлении, в зависимости от его величины.

if result is not None:
    print(f'Результат: {result:g}')
else:
    print("Результат:", result)
