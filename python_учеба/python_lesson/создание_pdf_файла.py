from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os

def generate_pdf(output_directory, output_file_name, table_text):
    # Создаем объект Canvas с выбранным размером страницы (letter)
    c = canvas.Canvas(os.path.join(output_directory, output_file_name), pagesize=letter)

    # Определяем размеры таблицы
    table_width = 400
    table_height = 200

    # Определяем количество строк и столбцов в таблице
    rows = 5
    cols = 3

    # Определяем размер ячейки
    cell_width = table_width / cols
    cell_height = table_height / rows

    # Рисуем пустую таблицу
    for i in range(rows + 1):
        c.line(100, 600 - i * cell_height, 100 + table_width, 600 - i * cell_height)

    for j in range(cols + 1):
        c.line(100 + j * cell_width, 600, 100 + j * cell_width, 600 - table_height)

    # Заполняем ячейки текстом
    for i in range(rows):
        for j in range(cols):
            text = table_text[i * cols + j] if i * cols + j < len(table_text) else ""
            c.drawString(100 + j * cell_width + 5, 600 - i * cell_height - 15, text)

    # Сохраняем PDF-файл
    c.save()

output_directory = "/home/yurovskaya/Рабочий стол/python_учеба/python_lesson"
output_file_name = "Autotest_pdf.pdf"
table_data = ["test", "test_1", "test_2", "test_3"]

generate_pdf(output_directory, output_file_name, table_data)