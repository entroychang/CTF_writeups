# Lab: User ID controlled by request parameter with password disclosure

This lab has user account page that contains the current user's existing password, prefilled in a masked input.

To solve the lab, retrieve the administrator's password, then use it to delete carlos.

You can log in to your own account using the following credentials: wiener:peter

## Access Control Vulnerabilities
* 題目說找到 administrator 的 password，送出 id=administrator 就可以拿到密碼了，之後登入 administrator 刪除 carlos 就可以了