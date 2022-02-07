# Lab: Basic SSRF against the local server

This lab has a stock check feature which fetches data from an internal system.

To solve the lab, change the stock check URL to access the admin interface at http://localhost/admin and delete the user carlos.

## SSRF
* 題目說要訪問 admin 頁面刪除使用者 carlos
* 觀察一下可以看到 stock 有發一個 request 到一個 url 會回傳答案，把那個 url 改成 http://localhost/admin 就可以訪問到 admin 頁面，之後就可以看一下怎麼刪除 carlos 就過了
```
payload = stockApi=http%3A%2F%2Flocalhost%2Fadmin%2Fdelete?username=carlos
```