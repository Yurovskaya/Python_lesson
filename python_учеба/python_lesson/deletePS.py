import requests

def create_unconfirmed_user():
    headers = {
        'accept': '*/*',
        'content-type': 'application/json',
    }

    json_data = {
        'fields': {
            'username': 'Autotest_21#106mRjRV@example.com',
            'firstName': 'Autotest_21#106',
            'middleName': '',
            'fioEng': '',
            'fioParentCase': '',
            'birthDate': None,
            'gender': '',
            'position': 'AUTOTEST',
            'positionEng': '',
            'positionParentCase': '',
            'orgId': '2f237496-b9ec-4eb5-b239-17e24a39d078',
            'staffStructId': '9355194d-9a76-4cc6-b043-2afb124304a4',
            'bossId': '',
            'inn': '',
            'available': True,
            'fizLink': '',
            'inila': '',
            'internal': True,
            'isEcP': False,
            'isEsIa': False,
            'jobPosition': '',
            'lastName': 'Autotest_21#106',
            'powerOfAttorney': False,
            'userAgreement': '',
            'emsRegDate': None,
            'timezone': '',
            'blocked': True,
            'actual_1c': True,
            'actual_1cDateTo': None,
        },
    }

    response = requests.post(
        'https://lk.d.exportcenter.ru/mdm-adapter/api/v1/catalogs/user_profile/items',
        headers=headers,
        json=json_data,
    )

    return response.status_code, response.json()