import os

# Получить текущую директорию
current_directory = os.getcwd()
print("Текущая директория:", current_directory)

# Получить полный путь к файлу
file_path = os.path.abspath("Autotest.docx")
print("Полный путь к файлу:", file_path)


import PyPDF2

print(PyPDF2.__version__)