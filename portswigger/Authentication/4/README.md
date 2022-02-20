# Lab: Username enumeration via subtly different responses

This lab is subtly vulnerable to username enumeration and password brute-force attacks. It has an account with a predictable username and password, which can be found in the following wordlists:

> Candidate usernames

> Candidate passwords

To solve the lab, enumerate a valid username, brute-force this user's password, then access their account page.

## Authentication
* 這一題的 username 正確的提示比較不明顯，兜兜轉轉了一大圈才發現是自己的問題 w，詳細的看腳本就知道我幹了什麼蠢事了 = =，這一題的不同在於 `Invalid username or password.` `Invalid username or password` 就不說哪裡不一樣了