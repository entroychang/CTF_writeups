# Lab: Multi-step process with no access control on one step

This lab has an admin panel with a flawed multi-step process for changing a user's role. You can familiarize yourself with the admin panel by logging in using the credentials administrator:admin.

To solve the lab, log in using the credentials wiener:peter and exploit the flawed access controls to promote yourself to become an administrator.

## Access Control Vulnerabilities
* 個人認為這一題遠比上一題簡單很多，至少我完全明白題目的意思，也可以想像可能的應用場景就是了 QQ
* 一樣需要兩組 cookie 可以發現在確認頁面是沒有做身分驗證的，所以可以用非 admin 的身分為自己提權