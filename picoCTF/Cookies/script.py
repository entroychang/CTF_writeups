import requests

url = 'http://mercury.picoctf.net:17781/check'

for i in range(0, 20):
    cookies = {
        'name' : str(i)
    }
    html = requests.get(url, cookies=cookies).text
    if 'picoCTF' in html:
        print(html)
        print(i)