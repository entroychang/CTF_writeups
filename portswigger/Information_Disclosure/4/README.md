# Lab: Authentication bypass via information disclosure

This lab's administration interface has an authentication bypass vulnerability, but it is impractical to exploit without knowledge of a custom HTTP header used by the front-end.

To solve the lab, obtain the header name then use it to bypass the lab's authentication. Access the admin interface and delete Carlos's account.

You can log in to your own account using the following credentials: wiener:peter

## Information Disclosure
* 題目說要 bypass 驗證訪問 admin panel，登入之後用 TRACE method 看一下 admin page 可以看到一個 header `X-Custom-IP-Authorization`，之後用 GET method，可以發現他說指能允許 local user 訪問，所以改成 127.0.0.1 就可以訪問了