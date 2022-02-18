# Lab: User role can be modified in user profile

This lab has an admin panel at /admin. It's only accessible to logged-in users with a roleid of 2.

Solve the lab by accessing the admin panel and using it to delete the user carlos.

You can log in to your own account using the following credentials: wiener:peter

## Access Control Vulnerabilities
* 題目說只要 roleid 是 2 就可以訪問 admin panel，這個時候就要找一下哪裡可以改 roleid，稍微看了一下可以發現可以改 email，用 burp 抓一下可以看到回傳了一組 json，其中就有 roleid 這一個參數，因此只要在送出的 json 中加入 `"roleid":2` 就可以改 roleid 並且訪問 admin panel 了