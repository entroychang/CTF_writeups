# Lab: Brute-forcing a stay-logged-in cookie

This lab allows users to stay logged in even after they close their browser session. The cookie used to provide this functionality is vulnerable to brute-forcing.

To solve the lab, brute-force Carlos's cookie to gain access to his "My account" page.

* Your credentials: wiener:peter
* Victim's username: carlos
* Candidate passwords

## Authentication
* 題目說會有一個 cookie 是可以記是誰登入的，觀察一下 `stay-logged-in` 這一個參數的架構
```
base64encode(username:md5(password))
```
* 詳情參考腳本