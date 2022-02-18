# Lab: User role controlled by request parameter

This lab has an admin panel at /admin, which identifies administrators using a forgeable cookie.

Solve the lab by accessing the admin panel and using it to delete the user carlos.

You can log in to your own account using the following credentials: wiener:peter

## Access Control Vulnerabilities
* 題目說在 cookie 有辨認目標是不是 admin，用 burp 擷取一下可以看到 `Admin=false`，改成 true 就可以訪問 admin panel 了