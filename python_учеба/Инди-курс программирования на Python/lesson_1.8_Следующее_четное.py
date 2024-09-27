# Задача - Следующее четное
# Дано целое число n. Выведите следующее за ним четное число.

#  Объяснение решения:
#  Если число четное то остаток от деления на 2 будет равен 0
#  У нечетного числа остаток от деления на 2 будет 1, и при вычитании 1 будет получаться следующее четное число
n = int(input())
next_even = n + 2 - (n % 2)
print(next_even)
