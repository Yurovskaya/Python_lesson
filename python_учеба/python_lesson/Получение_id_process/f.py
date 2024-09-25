import requests
import json
import time

BASE_URL = "https://lk.t.exportcenter.ru/"
url = BASE_URL + 'bpmn/api/v1/bpmn/process/all_counterparty_checks/start'

CLIENT_ID = '444bdebc-b11d-4290-90c8-af0bde35034a'
AUTH_TOKEN = "Bearer sso_1.0_d8d00614-4320-4340-8be4-303f044fdce0"
schemes = ["KYC_Checker_0afy6gk", "KYC_autocheck"]

def get_process_id(process_instance_id, scheme):
    time.sleep(10)
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
    response = requests.post(
        'https://lk.t.exportcenter.ru/bpmn/api/v1/bpms-process/filter',
        params=params,
        headers=headers,
        json=json_data,
    )
    calledProcesses = response.json()
    if calledProcesses:
        print(f"Id процесса {scheme}: {calledProcesses[0]['id']}")
        return calledProcesses[0]['id']
    else:
        raise Exception(f"Список {scheme} пустой.")

params = {'client': CLIENT_ID}
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
headers = {
    'Authorization': AUTH_TOKEN
}
response = requests.post(url, params=params, json=data, headers=headers)
response_json = response.text
data = json.loads(response_json)
camunda_id = data.get('camundaId')
process_instance_id = data.get('processInstanceId')

print("Camunda ID:", camunda_id)
print("Id процесса all_counterparty_checks:", process_instance_id)

for scheme in schemes:
    process_instance_id = get_process_id(process_instance_id, scheme)
