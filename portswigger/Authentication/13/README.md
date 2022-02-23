# Lab: Broken brute-force protection, multiple credentials per request

This lab is vulnerable due to a logic flaw in its brute-force protection. To solve the lab, brute-force Carlos's password, then access his account page.

* Victim's username: carlos
* Candidate passwords

## Authentication
* 題目是說 brute force 的 protection 是有問題的，攔截一下看一下可以看到是用 json 傳遞帳號密碼，這個時候用 json 的 array 包著所有的密碼可以導入到 account page，詳細可以看腳本