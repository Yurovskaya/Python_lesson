# Написать программу, которая сможет проверить входные данные на палиндром (строка или число одинаково читается в прямом и обратном направлении)
# word = input()
# a = word[::-1]
# if word == a:
#     print(True)
# else:
#     print(False)
#
# text = input().lower()
# print(text == text[::-1])

# print((lambda x: str(x) == str(x)[::-1])('tttt'))


# Подсчет суммы четных чисел
# Напишите функцию calculate_even_sum, которая принимает на вход список чисел и возвращает сумму всех четных чисел в этом списке.
# Напишите также тесты, чтобы проверить правильность работы функции на разных входных данных.

# numbers = [1, 4, 5, 6, 14, 17]
#
# def calculate_even_sum(numbers):
#     even_sum = 0
#     for i in numbers:
#         if i % 2 == 0:
#             even_sum += i
#     return even_sum
#     assert even_sum % 2 == 0, f'Сумма числе нечетная {even_sum}'
#
# print(calculate_even_sum(numbers))

# Напишите функцию count_words, которая принимает на вход строку, представляющую предложение, и возвращает количество слов в этом предложении.
# Предполагается, что слова разделены пробелами. Напишите также тесты, чтобы проверить правильность работы функции на разных входных данных.

user_words = input()

def count_words(user_words):
    word = user_words.split()
    assert len(word) != 0, f'Ошибка'
    return len(word)

print(count_words(user_words))


# Написать программу, которая сможет проверить входные данные на палиндром (строка или число одинаково читается в прямом и обратном направлении)
# word = input()
# a = word[::-1]
# if word == a:
#     print(True)
# else:
#     print(False)
#
# text = input().lower()
# print(text == text[::-1])
# from decorator import append
# from soupsieve.util import lower

# print((lambda x: str(x) == str(x)[::-1])('tttt'))


# Подсчет суммы четных чисел
# Напишите функцию calculate_even_sum, которая принимает на вход список чисел и возвращает сумму всех четных чисел в этом списке.
# Напишите также тесты, чтобы проверить правильность работы функции на разных входных данных.

# numbers = [1, 4, 5, 6, 14, 17]
#
# def calculate_even_sum(numbers):
#     even_sum = 0
#     for i in numbers:
#         if i % 2 == 0:
#             even_sum += i
#     return even_sum
#     assert even_sum % 2 == 0, f'Сумма числе нечетная {even_sum}'
#
# print(calculate_even_sum(numbers))

# Напишите функцию count_words, которая принимает на вход строку, представляющую предложение, и возвращает количество слов в этом предложении.
# Предполагается, что слова разделены пробелами. Напишите также тесты, чтобы проверить правильность работы функции на разных входных данных.

# user_words = input()
#
# def count_words(user_words):
#     word = user_words.split()
#     assert len(word) != 0, f'Ошибка'
#     return len(word)
#
# print(count_words(user_words))


# text_test = "Python programming is fun!"
#
# def count_words(text):
#     text_mod = len(text.split())
#     print(text_mod)
#     assert text_mod != 0, "текст не заполнен"
#     return text_mod
#
#
# assert count_words(text_test) == 4
#
# count_words(text_test)


# Напишите функцию count_vowels, которая принимает на вход строку, состоящую из латинских букв, и возвращает количество гласных букв
# (а и
# менно буквы A, E, I, O, U, a, e, i, o, u) в этой строке.

# words = input().lower()
#
# def count_vowels(words):
#     a = list(words)
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     count = 0
#     for i in a:
#         if i in vowels:
#             count += 1
#     assert count!= 0, "Не содержит гласные буквы из списка"
#     return count
#
# print(count_vowels(words))



# Напишите функцию calculate_sum, которая принимает на вход одно целочисленное значение N и возвращает сумму всех чисел от 1 до N включительно.

n = int(input('Введите N: '))

def summa_n(n):
    return (n * (n + 1)) // 2

assert summa_n(5) == 15, 'Ошибка'
assert summa_n(1) == 1, 'Ошибка'
assert summa_n(0) == 0, 'Ошибка'
assert not summa_n(-11) == 0, 'Ошибка'



def  is_palindrome(num):
    str_num = str(num)
    return str_num == str_num[::-1]

# я ввожу на вход целое число
n = input()
#  вывожу тип
a = (type(n))
print(a)

# если а не равно строке строке - ошибки не будет
# если а равно строке, то буде ошибка
assert not a == str, 'Ошибка'
#
# def calculate_sum(N):
#     return sum(range(1, N + 1))
#
#
#
#
#
#
# n='txt'
# assert not type(n) == int














