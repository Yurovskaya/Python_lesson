# a = 10
#
# while a > 1:
#     a -= 1
#     print(a)

# #  Производится отбрасывание первого символа строки до тех пор, пока она не станет пустой и поэтому ложной
# x = 'spam'
# while x:
#     print(x, end=' ')
#     x = x[1:]
#
# a = 0
# b = 10
# while a < b:
#     print(a, end=' ')
#     a+=1

# x = 10
# while x:
#     x = x - 1
#     if x % 2 != 0: continue
#     print(x, end = ' ')
#
while True:
    name = input("Введите имя: ")
    if name == "stop":
        break
    age = int(input("Введите возраст: "))
    print("Привет", name, "=>",  age ** 2)
