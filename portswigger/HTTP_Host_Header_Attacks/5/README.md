# Lab: SSRF via flawed request parsing

This lab is vulnerable to routing-based SSRF due to its flawed parsing of the request's intended host. You can exploit this to access an insecure intranet admin panel located at an internal IP address.

To solve the lab, access the internal admin panel located in the 192.168.0.0/24 range, then delete Carlos.

## HTTP Host Header Attack
* 這一題跟上一題差不多，只是這一題有驗證 host，詳細可以參考 https://www.796t.com/article.php?id=414439 我覺得講的滿細的，至少我在沒有看這篇的時候是不懂的，後來花了比較久的時間在找怎麼用 python 達到這種效果，用了 http.client，requests 模組應該達不太到我的要求，之後用腳本爆破也是差不多的流程，如果懶得用的話就一樣用 burp 的 intruder 也可以，反而比較方便 w