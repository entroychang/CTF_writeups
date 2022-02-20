# Lab: 2FA broken logic

This lab's two-factor authentication is vulnerable due to its flawed logic. To solve the lab, access Carlos's account page.

* Your credentials: wiener:peter
* Victim's username: carlos
You also have access to the email server to receive your 2FA verification code.

## Hint 
Carlos will not attempt to log in to the website himself.

## Authentication
* 題目說在信箱驗證那裡會有問題，稍微觀察一下可以發現 cookie 中有 `verify: wiener`，把它改成目標就可以了，就可以用腳本爆破驗證碼，詳細可以看腳本