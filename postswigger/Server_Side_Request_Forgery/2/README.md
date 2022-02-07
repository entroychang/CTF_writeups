# Lab: Basic SSRF against another back-end system

This lab has a stock check feature which fetches data from an internal system.

To solve the lab, use the stock check functionality to scan the internal 192.168.0.X range for an admin interface on port 8080, then use it to delete the user carlos.

## SSRF
* 這一題直白一點的說就是要用腳本跑哪一個內網的 ip 是 可以訪問 admin 的頁面，所以說不管用什麼方式只要從 192.168.0.1 ~ 192.168.0.255 一個一個試，只要可以訪問 admin 就是正確的，之後記得刪 user carlos