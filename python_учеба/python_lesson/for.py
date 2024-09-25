# students = ["Alex", "Даша", "Ольга", "Ada", "Ivan", "Semen"]
#
# for f in students:
#    print(len(f))
#
#
# for i in 'Python':
#     print(i)
#
# lst1 = ['1', '2', '3', '4', '5']
# lst2 = ['a', 'b', 'c', 'd', 'e']
# for i in lst1:
#     for j in lst2:
#         print(i + j)

#
# list = [1, 4, 6, 8, 12]
#
# for i  in list:
#     if i == 6:
#         print("Ура 6")
#         break
#     print(i)


# login = input("Введите Ваш логин: ")
#
# while True:
#     if login == "Alex":
#         print("Вы ввели верный пароль")
#         password = input("Введите пароль: ")
#     else:
#         print("Вы ввели некорректный логин")
#         break


# list = [1, 4, 6, 8, 10, 12]
#
# for i  in list:
#     if i == 10:
#         print("Плохо 10")
#         break
#
#     elif i == 4:
#      print("Ура 4")
#
#     elif i == 6:
#      print("Ура 6")
#      continue
#
#     print(i)

for x in ["spam", "eggs", "ham"]:
    print(x, end=' ')

sum_1 = 0
for x in [1, 2, 3, 4]:
    sum_1 = sum_1 + x
    print(sum_1)