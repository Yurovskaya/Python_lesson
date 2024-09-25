import os
import requests

def api_test6929():
    headers = {
        'accept': '*/*',
        'Authorization': 'Bearer sso_1.0_de7074a3-c5be-4cf0-980e-b344507f9e56',
    }

    response = requests.get(
        'https://lk.d.exportcenter.ru/bpmn/api/v1/bpmn/process-definition/all_counterparty_checks/bpmn',
        headers=headers,
    )

    # Получение текущей директории, где выполняется скрипт
    current_directory = os.getcwd()

    # Имя файла, каким вы хотите его сохранить
    file_name = 'all_counterparty_checks.bpmn'

    full_path = os.path.join(current_directory, file_name)

    # Сохранение файла
    with open(full_path, 'wb') as file:
        file.write(response.content)

    return response.status_code

api_test6929()
