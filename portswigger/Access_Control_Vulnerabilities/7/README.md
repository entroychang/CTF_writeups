# Lab: User ID controlled by request parameter with data leakage in redirect

This lab contains an access control vulnerability where sensitive information is leaked in the body of a redirect response.

To solve the lab, obtain the API key for the user carlos and submit it as the solution.

You can log in to your own account using the following credentials: wiener:peter

## Access Control Vulnerabilities
* 題目說問題在 redirect 的時候會有資訊洩漏，所以在給 `/my-account?id=carlos` 的時候用 burp 攔截一下可以看到 carlos 的資訊