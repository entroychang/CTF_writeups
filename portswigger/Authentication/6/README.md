# Lab: Broken brute-force protection, IP block

This lab is vulnerable due to a logic flaw in its password brute-force protection. To solve the lab, brute-force the victim's password, then log in and access their account page.

* Your credentials: wiener:peter
* Victim's username: carlos
* Candidate passwords

## Hint
Advanced users may want to solve this lab by using a macro or the Turbo Intruder extension. However, it is possible to solve the lab without using these advanced features.

## Authentication
* 題目說會 ban ip，不能用 `X-Forwarded-For` bypass，如果登入成功，該 ip 會解 ban，所以寫個腳本，登入錯的再登入正確的就可以 brute force 了
