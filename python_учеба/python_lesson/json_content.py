import re


def extract_id_from_url(url):
    # Находим все подстроки, соответствующие паттерну UUID
    pattern = r'([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})'
    match = re.search(pattern, url)
    return match.group(0)

# Пример использования функции для указанного URL
url_example = 'https://ecm.d.exportcenter.ru/document/c00407.4c88d13c-0d4a-4b7d-9ac9-b772df5597d6'
identifier = extract_id_from_url(url_example)
print(f"Идентификатор из URL: {identifier}")
