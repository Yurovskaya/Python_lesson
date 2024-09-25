# var = input("Напиши текст: ")
# fw = open("doc/file.txt", "a")
# fw.write(var)
# fw.close()

# a запись новых данных в файл и помещение новых данных в конец файла
# w запись новых данных, но с удалением старых данных

# fw = open("doc/file_2.txt", "w")
# fw.write("Собака")
# fw.close()

# fa = open('doc/file.txt', "r")
# text = fa.read()
# fa.close()
# print(text)

#  a	Откроет для добавления нового содержимого. Создаст новый файл для записи, если не найдет с указанным именем.
file = open("doc/file_test.txt", 'a')
file.write("Учим уроки\n")
file.close()

# r	Только для чтения.
file_read = open("doc/file_test.txt", 'r')
file_read_text = file_read.read()
print(file_read_text)

#  w	Только для записи. Создаст новый файл, если не найдет с указанным именем.
file_w = open("doc/file_test_w.txt", 'w')
file_w.write("Пытаюсь учить урок")
file_w.close()

#  r+	Для чтения и записи.
file_read = open("doc/file_test.txt", 'r+')
file_read_text = file_read.read()
print(file_read_text)

additional_text = "\nНу и денек."
file_read.write(additional_text)
updated_content = file_read.read()
print(updated_content)

file_read.close()