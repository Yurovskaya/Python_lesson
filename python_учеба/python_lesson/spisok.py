# personal = ['Alex', 'Ivan', 'Olga', 'Ada']
# resalt = personal[0] + " " + personal[2]
# print(resalt + " - лучшая пара")
#
# number = [1, 15, 23, 4]
# num_1 = number[1]
# print(num_1)
# resalt_num = number[1] + number[3]
# print(resalt_num)
#
#
# L = [123, 'spam', 1.23, 'Даша']
# print(L)
# a = len(L)
# print(a)
# a = 123 in L
# print(a)
#
#
# M = ['bb', 'aa', 'cc']
# M.sort()
# print(M)
# M.reverse()
# print(M)
#
# M = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]
#      ]
# col14 = [row[1] for row in M if row[1] % 2 == 0]
# print(col14)
#
# a = [1, 2, 3]
# for x in a:
#     print(x, end='')
#
#
# bicycles = ['trek', ]


# string = str(input("Введите предложение: "))
# string_list = string.split(' ')
# print(len(string_list))

string = input("Введите что-нибудь")
words = []
i = 0
word = ''
while i < len(string):
    if string[i] == ' ':
        # если текущий символ в строке
        # пробел (разделитель), то нужно
        # добавить все, что
        # накопилось в переменной word в список
        # и очистить переменную
        words.append(word)
        word = ''
    else:
        # если текущий символ не разделитель
        # то добавим его в переменную
        # с текущим словом
        word += string[i]
    i += 1
# все, то накопилось в текущем слове
# нужно добавить в список слов
words.append(word)
print(words)


