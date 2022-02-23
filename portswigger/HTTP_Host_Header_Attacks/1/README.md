# Lab: Basic password reset poisoning

This lab is vulnerable to password reset poisoning. The user carlos will carelessly click on any links in emails that he receives. To solve the lab, log in to Carlos's account.

You can log in to your own account using the following credentials: wiener:peter. Any emails sent to this account can be read via the email client on the exploit server.


## HTTP Host Header Attack
* 題目說要登入 carlos 的帳號，可以看到有一個功能是 forget password，然後有一組 temp token 的東西，把 header 中的 Host 改成自己的 exploit server 之後看 log 就可以看到跳轉的頁面，其中一個就是 token，訪問之後改掉 carlos 的 password 就可以登入了