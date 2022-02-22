# Lab: Password reset poisoning via middleware

This lab is vulnerable to password reset poisoning. The user carlos will carelessly click on any links in emails that he receives. To solve the lab, log in to Carlos's account. You can log in to your own account using the following credentials: wiener:peter. Any emails sent to this account can be read via the email client on the exploit server.

## Authentication
* 題目說我需要改 carlos 的密碼，不過這題我卡關了，稍微看了一下答案發現有一個 header 叫做 `X-Fowarded-Host`，把自己的 exploit server 的 host 放進去，之後看一下 log 可以看到跳轉的 token，訪問之後改成自己喜歡的密碼就可以登入 carlos 的帳號了