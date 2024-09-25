from docx import Document
from docx.shared import Pt
from docx.oxml import OxmlElement


def rotate_text_paragraph(paragraph):
    # Создаем элемент fldSimple для вставки кода SET
    fld_simple = OxmlElement('w:fldSimple')
    fld_simple.set('xmlns:w', 'http://schemas.openxmlformats.org/wordprocessingml/2006/main')
    fld_simple.set('w:instr', 'QUOTE ' + paragraph.text)

    # Вставляем элемент fldSimple перед существующими элементами параграфа
    paragraph._p.insert(0, fld_simple)

    # Находим элемент instrText и меняем его текст
    fld_code = fld_simple.find('.//w:instrText')
    fld_code.text = fld_code.text.replace('QUOTE', 'SET')


# Создаем документ
doc = Document()

# Добавляем параграф с текстом
paragraph = doc.add_paragraph("тест")

# Поворачиваем текст на 90 градусов
rotate_text_paragraph(paragraph)

# Сохраняем документ
doc.save("output.docx")
