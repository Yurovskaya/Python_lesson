import csv

def read_csv_file(file_path):
    """
    Читает данные из CSV файла и возвращает их в виде строки.
    :param file_path: Путь к CSV файлу.
    :return: Строка с данными из CSV файла.
    """
    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            data_as_string = '\n'.join(','.join(row) for row in csv_reader)
            return data_as_string
    except FileNotFoundError:
        return f"Файл не найден: {file_path}"
    except Exception as e:
        return f"Произошла ошибка при чтении файла: {e}"

# Пример использования функции
csv_file_path = '/home/yurovskaya/Рабочий стол/python_учеба/python_lesson/orgs.csv'
csv_data = read_csv_file(csv_file_path)

if "Ошибка" in csv_data:
    print(csv_data)
else:
    print("Данные из CSV файла:")
    print(csv_data)
