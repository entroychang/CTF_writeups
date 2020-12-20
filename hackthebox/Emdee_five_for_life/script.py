import requests
import hashlib
from bs4 import BeautifulSoup

def send_request():
    while True:
        s = requests.Session()
        url = 'http://167.99.85.197:31859/'
        hashed = hashlib.md5((BeautifulSoup(s.get(url).text, 'html.parser').find('h3').get_text()).encode('utf-8')).hexdigest()
        data = {'hash' : hashed}
        flag = s.post(url, data=data).text
        if 'HTB{' in flag:
            print(BeautifulSoup(flag, 'html.parser').find('p').get_text())
            break

if __name__ == '__main__':
    send_request()
