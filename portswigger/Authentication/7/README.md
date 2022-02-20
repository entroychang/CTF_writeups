# Lab: Username enumeration via account lock

This lab is vulnerable to username enumeration. It uses account locking, but this contains a logic flaw. To solve the lab, enumerate a valid username, brute-force this user's password, then access their account page.

* Candidate usernames
* Candidate passwords

## Authentication
* 題目說如果輸入太多次錯誤的密碼，帳戶會鎖定，比較有問題的是我不知道怎麼加快密碼的爆破，因為我就單純的等 1 分鐘 QQ，詳情請看腳本