import json

passwords = open('../../wordlist/password.txt')

password_list = []
for password in passwords:
    password_list.append(password.replace('\n', ''))

print(json.dumps(password_list))