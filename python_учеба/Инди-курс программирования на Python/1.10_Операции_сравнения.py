# Операции сравнения
# Прежде чем рассмотрим сами операции стоит отметить, что результатом любого допустимого сравнения будет логический тип: либо значение True, либо False
#
# При любом сравнении участвуют всегда два операнда: левый операнд (стоит слева от операции сравнения) и правый операнд. Python поддерживает следующие операции сравнения:
#
# == Возвращает True, если оба операнда равны. ...
# != Возвращает True, если оба операнда НЕ равны. ...
# > (больше чем) Возвращает True, если первый операнд больше второго.
# < (меньше чем) ...
# >= (больше или равно) ...
# <= (меньше или равно)


# КОНЪЮНКЦИЯ(союз "and"), ДИЗЪЮНКЦИЯ(союз "or") И ИНВЕРСИЯ(союз "not") и также уметь строить таблицы истинности.

# На вход поступает целое число.
#
# Программа должна вывести True, если введенное значение не делится на 9, в противном случае - False.
#
# Сделать задачу необходимо без использования условного оператора.

a = int(input())
print(a % 9 != 0)