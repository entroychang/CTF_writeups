# Lab: User ID controlled by request parameter

This lab has a horizontal privilege escalation vulnerability on the user account page.

To solve the lab, obtain the API key for the user carlos and submit it as the solution.

You can log in to your own account using the following credentials: wiener:peter

## Access Control Vulnerabilities
* 題目說找到 carlos 的 api key，稍微觀察一下可以看到在 my-account 後面的網址帶著 id 這一個參數，把它改成 carlos 就可以拿到他的 api key 了