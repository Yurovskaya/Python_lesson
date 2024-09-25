# coding=UTF-8

import requests
import json
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def tokens(argv):
    headers = {'Accept': 'application/json',
               'Content-Type': 'application/x-www-form-urlencoded'}
    grant_type = 'urn:roox:params:oauth:grant-type:m2m'
    client_secret = 'password'
    client_id = 'rec_login_m2m'
    needsystem = False

    url = argv[1]

    if url == 'https://lk.exportcenter.ru/sso/oauth2/access_token':
        login = 'mdm_user'
        password = 'mdm_pass'
    else:
        login = 'demo_exporter@expocenter.ru'
        password = 'password'

    print('STEP 1***********************************************************************')
    payload = {'client_id': client_id,
               'realm': '/customer',
               'grant_type': grant_type,
               'response_type': 'token cookie',
               'service': 'expc-login'}

    #print(url)
    #print(headers)
    res = requests.post(url, data=payload, headers=headers, verify=False)
    #print(res.content)
    execution = json.loads(res.content)['execution']
#    print(execution)

    print('STEP 2***********************************************************************')
    payload = {'client_id': client_id,
               'realm': '/customer',
               'grant_type': grant_type,
               'response_type': 'token cookie',
               'execution': execution,
               'regType': 'lkp',
               '_eventId': 'password'
               }

    res = requests.post(url, data=payload, headers=headers, verify=False)
    #print(res.headers)
    #print(res.content)
    execution = json.loads(res.content)['execution']
#    print(execution2)

    print('STEP 3***********************************************************************')
    payload = {'client_id': client_id,
               'realm': '/customer',
               'grant_type': grant_type,
               'response_type': 'token cookie',
               '_eventId': 'next',
               'username': login,
               'password': password,
               'execution': execution
               }

    #print(url)
    #print(headers)
    res = requests.post(url, data=payload, headers=headers, verify=False)
    #print(res.content)
    #print(json.loads(res.content))
    loginOrgs = json.loads(res.content)['view']['availableLoginOrgs']
    print("USING FIRST LOGIN ORG: " + loginOrgs[0]['externalId'])
    loginOrg = loginOrgs[0]['externalId']
    execution = json.loads(res.content)['execution']

    print('STEP 4***********************************************************************')
    payload = {'client_id': client_id,
               'realm': '/customer',
               'grant_type': grant_type,
               'execution': execution,
               '_eventId': 'next',
               'regType': 'lkp',
               'externalOrgId': loginOrg
               }

    #print(url)
    #print(headers)
    res = requests.post(url, data=payload, headers=headers, verify=False)
    #print(res.content)
    #print(json.loads(res.content))

    return 'Bearer sso_1.0_' + json.loads(res.content)['access_token']

src = sys.argv[1]

sso_urls = {
    'dev' : 'http://uidm.uidm-dev.d.exportcenter.ru/sso/oauth2/access_token',
    'test' : 'https://lk.t.exportcenter.ru/sso/oauth2/access_token',
    'preprod' : 'https://lk.d.exportcenter.ru/sso/oauth2/access_token',
    'prod' : 'https://lk.exportcenter.ru/sso/oauth2/access_token'
}

src_token = tokens(['', sso_urls[src]])

print(src + " token = " + src_token)