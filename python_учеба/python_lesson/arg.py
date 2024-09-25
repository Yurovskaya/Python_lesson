n = "Anna"
a = 25


def descriotion (name, age, gender):
    print(f"Имя {name}, Возраст {age}, Пол {gender}")

descriotion(n, a, "woman")
# descriotion("Анна", 30, "man")  # позиционный аргумент
# #  именованный аргумент
# descriotion(name= "Анна", age= 23, gender= "woman")

# def identification (name):
#     print("Вы являетесь")
#     if name == "Alex":
#         print("Автором")
#     else:
#         print("Студентом")
#
# name = input("Ведите имя: ")
#
# identification(name)

# def identification (name):
#     print("Вы являетесь")
#     if name == "Alex":
#         result = "Автором"
#     else:
#         result = "Студентом"
#
#     return result
#
# name = input("Ведите имя: ")
#
# print(identification(name))
#
# f = "Alex"
# s = identification(name)
#
# print (f"{f} {s}")

def identification (name):
    print("Вы являетесь")
    if name == "Alex":
        result = "Автором"
    else:
        result = "Студентом"

    return result

def status(result):
    print(result)

name = input("Ведите имя: ")
status(identification(name))