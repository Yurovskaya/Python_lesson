import fitz  # PyMuPDF

def extract_text_and_images_from_pdf(pdf_path):
    with fitz.open(pdf_path) as doc:
        for page_num in range(doc.page_count):
            page = doc[page_num]

            # Извлекаем текст
            text = page.get_text()

            # Извлекаем информацию об изображениях
            images_info = page.get_images(full=True)

            # Выводим информацию об изображениях на странице
            print(f"Страница {page_num + 1} (Текст и изображения):")
            print(f"Текст:\n{text}\n")

            print("Изображения:")
            for img_index, img_info in enumerate(images_info):
                image_reference = img_info[5]
                image_dict = {
                    'index': img_index,
                    'width': img_info[0],
                    'height': img_info[1],
                    'color_space': img_info[2],
                    'bits_per_component': img_info[3],
                    'color_components': img_info[4],
                    'image_reference': image_reference
                }

                # Проверяем, есть ли информация об имени изображения
                if isinstance(image_reference, dict) and "name" in image_reference:
                    image_dict['image_name'] = image_reference['name']

                print(f"Image {img_index + 1}:", image_dict)

            print("\n" + "=" * 50 + "\n")

# Пример использования
pdf_file_path = '/home/yurovskaya/Рабочий стол/python_учеба/python_lesson/file.pdf'
extract_text_and_images_from_pdf(pdf_file_path)
