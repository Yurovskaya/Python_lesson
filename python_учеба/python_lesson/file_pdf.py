import pypdf


def read_pdf(pdf_path):
    all_text = ""  # Создаем переменную для сохранения текста всех страниц
    with open(pdf_path, 'rb') as file:
        # Создаем объект для работы с PDF
        pdf_reader = pypdf.PdfReader(file)

        # Получаем количество страниц в документе
        num_pages = len(pdf_reader.pages)

        # Итерируем по страницам и читаем текст
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()
            print(f"Содержимое страницы {page_num + 1}:\n{text}\n")

            all_text += text  # Добавляем текст текущей страницы к общему тексту

    return all_text


# Пример использования
pdf_file_path = '/home/yurovskaya/Рабочий стол/python_учеба/python_lesson/Autotest.pdf'
all_pdf_text = read_pdf(pdf_file_path)

# Проверяем, заканчивается ли текст на заданную строку
if all_pdf_text.endswith("Схема взаимодействия основных участников отсутствует"):
    print("Текст оканчивается на нужную строку.")
else:
    print("Текст не оканчивается на нужную строку.")


# import fitz  # PyMuPDF
#
# def extract_text_from_pdf(pdf_path):
#     all_page_texts = []  # Список для хранения текста каждой страницы
#     with fitz.open(pdf_path) as doc:
#         for page_num in range(doc.page_count):
#             page = doc[page_num]
#
#             # Извлекаем текст
#             text = page.get_text()
#
#             # Добавляем текст в список
#             all_page_texts.append(text)
#
#     return all_page_texts
#
# # Пример использования
# pdf_file_path = '/home/yurovskaya/Рабочий стол/python_учеба/python_lesson/file.pdf'
# all_texts = extract_text_from_pdf(pdf_file_path)
#
# # Проверяем, заканчивается ли текст на заданную строку для каждой страницы
# for page_num, text in enumerate(all_texts):
#     if text.endswith("Схема взаимодействия основных участников отсутствует"):
#         print(f"Текст на странице {page_num + 1} оканчивается на нужную строку.")
#     else:
#         print(f"Текст на странице {page_num + 1} не оканчивается на нужную строку.")
