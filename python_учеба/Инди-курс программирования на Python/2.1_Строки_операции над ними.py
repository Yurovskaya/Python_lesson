# Напишите программу, которая сначала считывает две фразы по очереди, а
# потом воспроизводит их в той же последовательности, каждую на отдельной строке

a = input()
b = input()
print(a,b, sep='\n')


a = 'Ха'
b = a + ' '
print(b * 4)

a = input()
print(len(a))

a = input()
b = ord(a[0])
print(b)
c = ord(a[2])
d = ord(a[4])
print(f"Simvol code {a[0]} is {b}.")
print(f"Simvol code {a[0]} is {c}.")
print(f"Simvol code {a[0]} is {d}.")

a = input()
print(a[1::2])

s = input()
word = input()
print(s.upper == word.upper())





