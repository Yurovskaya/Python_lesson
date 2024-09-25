import requests
import json
import time

BASE_URL = "https://lk.t.exportcenter.ru"
schemes = ['multi_sig']
AUTH_TOKEN = "Bearer sso_1.0_55570095-e3c9-47c3-a827-18bd062864cb"
process_instance_id = 'ccd85c45-669b-11ef-ae39-de6c9124117f'

def get_process_id_in_shemes(process_instance_id, schemes):
    # Создается пустой список process_ids
    # Происходит итерация по элементам списка schemes (который мы передаем в качестве аргумент) для получения порядкового номера
    # и значения элемента
    process_ids = []
    for enum, scheme in enumerate(schemes):
        headers = {
            'accept': '*/*',
            'Authorization': AUTH_TOKEN,
            'Content-Type': 'application/json',
        }
        params = {
            'camundaId': 'camunda-exp-search-a',
        }
        json_data = {
            'superProcessInstance': process_instance_id,
            'processDefinitionKey': scheme,
        }
        time.sleep(10)
        response = requests.post(
            f'{BASE_URL}/bpmn/api/v1/bpms-process/filter',
            params=params,
            headers=headers,
            json=json_data,)

        calledProcesses = response.json()
        print(calledProcesses)
        # Если calledProcesses содержит хотя бы один элемент, то выводим идентификатор первого процесса из списка calledProcesses
        # Обновляет переменную process_instance_id значением идентификатора первого процесса из списка calledProcesses.
        # Добавляет идентификатор первого процесса из списка calledProcesses в список process_ids.
        # Иначе выводим сообщение о том, что список для определенной схемы scheme пустой.
        if calledProcesses:
            print(f"Id процесса {scheme}: {calledProcesses[0]['id']}",)
            process_instance_id = calledProcesses[0]['id']
            process_ids.append(calledProcesses[0]['id'])
        else:
            raise Exception(f"Список {scheme} пустой.")
    return process_ids

process_ids = get_process_id_in_shemes('process_instance_id', 'schemes')
print("Полученные ID процессов:", process_ids)