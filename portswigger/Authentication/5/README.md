# Lab: Username enumeration via response timing

This lab is vulnerable to username enumeration using its response times. To solve the lab, enumerate a valid username, brute-force this user's password, then access their account page.

Your credentials: wiener:peter

> Candidate usernames

> Candidate passwords

## Hint
To add to the challenge, the lab also implements a form of IP-based brute-force protection. However, this can be easily bypassed by manipulating HTTP request headers.

## Authentication
* 題目說會 ban ip 可以用 `X-Forwarded-For` bypass，這個時候看一下題目說回應的時間會有差別，很認真的試了一下發現啥都看不出來，這個時候看一下 solution 發現只要 username 是存在的，密碼拉長到大概 100 位回應的時間就會有明顯的差異，老實說真的沒有想過這個方法，但是想一想也覺得挺合理的，處理 username 成功過後因為 password 很長，所以要花費更過時間處理，這樣想一想就挺合理的，詳細的可以看腳本