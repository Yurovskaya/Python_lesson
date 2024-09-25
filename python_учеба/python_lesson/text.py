# def contains_digits(text):
#     return any(char.isdigit() for char in text)
#
# # Пример использования
# text = "Пример текста с цифрами 123"
# if contains_digits(text):
#     print("Текст содержит цифры.")
# else:
#     print("Текст не содержит цифры.")
#
#
# contains_digits("Даща Даша 5677")


Str='это пример строки....wow!!!'
suffix='!!'
print (Str.endswith(suffix))
print (Str.endswith(suffix,20))
suffix='прим'
print (Str.endswith(suffix))
print (Str.endswith(suffix, 0.9))