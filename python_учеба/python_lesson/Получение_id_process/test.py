import time
import requests
import json
import urllib3

BASE_URL = "https://lk.t.exportcenter.ru/"
process_id = None
# Отключаем предупреждения для тестового сервера
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# URL вашего запроса
url = BASE_URL+f'bpmn/api/v1/bpmn/process/all_counterparty_checks/start'

# Параметры, передаваемые в запросе
params = {'client': '444bdebc-b11d-4290-90c8-af0bde35034a'}

# Тело запроса в формате JSON
data = {
    "checkType": {
        "type": "string",
        "value": "stopFactors"
    },
    "criterionTypeMap": {
        "type": "Object",
        "value": '[{"critType":"tax_debts"}]',
        "valueInfo": {
            "objectTypeName": "java.util.ArrayList",
            "serializationDataFormat": "application/json"
        }
    }
}

# Заголовок запроса с токеном авторизации
headers = {
    'Authorization': 'Bearer sso_1.0_ac1e38ab-ee64-4216-a6e9-7993d41efc84'
}

# Отправка POST-запроса с указанными параметрами, телом запроса и заголовком с токеном
response = requests.post(url, params=params, json=data, headers=headers)

response_json = response.text
data = json.loads(response_json)


camunda_id = data.get('camundaId')
process_instance_id = data.get('processInstanceId')

print("Camunda ID:", camunda_id)
print("Process Instance ID:", process_instance_id)\


#Старт

def get_ProcessInstance(token):
    BASE_URL = "https://lk.t.exportcenter.ru/"

    # URL вашего запроса
    url = BASE_URL + 'bpmn/api/v1/bpmn/process/all_counterparty_checks/start'

    # Параметры, передаваемые в запросе
    params = {'client': '444bdebc-b11d-4290-90c8-af0bde35034a'}

    # Заголовок запроса с токеном авторизации
    headers = {'Authorization': token}

    # Отправка POST-запроса с указанными параметрами и заголовком с токеном
    response = requests.post(url, params=params, headers=headers)

    # Проверка статуса ответа
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return None

    response_json = response.json()
    camunda_id = response_json.get('camundaId')
    process_instance_id = response_json.get('processInstanceId')

    print("Camunda ID:", camunda_id)
    print("Process Instance ID:", process_instance_id)

    return process_instance_id


# Пример использования функции
token = 'Bearer sso_1.0_ac1e38ab-ee64-4216-a6e9-7993d41efc84'
process_instance_id = get_ProcessInstance(token)

time.sleep(10)



def get_process_id(data, token):
    headers = {
        'accept': '*/*',
        'Authorization': token,
        'Content-Type': 'application/json',
    }

    params = {
        'camundaId': 'camunda-exp-search-a',
    }

    json_data = {
        'superProcessInstance': data.get('processInstanceId'),
        'processDefinitionKey': 'KYC_Checker_0afy6gk',
    }

    response = requests.post(
        'https://lk.t.exportcenter.ru/bpmn/api/v1/bpms-process/filter',
        params=params,
        headers=headers,
        json=json_data,
    )

    response_json = response.json()
    print(response_json)

    if response_json:
        id = response_json[0]['id']
        print(id)
        return  id
    else:
        print("Список response_json пустой.")
        return None


token = "Bearer sso_1.0_e244fe9e-b26b-46ae-b8a5-3f4c17f82df7"
process = get_process_id(data, token)

time.sleep(15)




headers = {
    'accept': '*/*',
    'Authorization': 'Bearer sso_1.0_e244fe9e-b26b-46ae-b8a5-3f4c17f82df7',
    'Content-Type': 'application/json',
}

params = {
    'camundaId': 'camunda-exp-search-a',
}

json_data = {
    'superProcessInstance': id,
    'processDefinitionKey': 'KYC_autocheck',
}

response = requests.post(
    'https://lk.t.exportcenter.ru/bpmn/api/v1/bpms-process/filter',
    params=params,
    headers=headers,
    json=json_data,
)