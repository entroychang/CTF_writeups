# Lab: Host header authentication bypass

This lab makes an assumption about the privilege level of the user based on the HTTP Host header.

To solve the lab, access the admin panel and delete Carlos's account.

## HTTP Host Header Attack
* 題目說訪問 admin panel 之後刪掉 carlos 的帳號，我們訪問 admin panel 之後會出現 `Admin interface only available to local users`，因此我們需要是 localhost 才能訪問 admin panel，把 host header 改成 localhost 就可以訪問 admin panel 了