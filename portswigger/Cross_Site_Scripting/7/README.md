# Lab: DOM XSS in jQuery anchor href attribute sink using location.search source

This lab contains a DOM-based cross-site scripting vulnerability in the submit feedback page. It uses the jQuery library's $ selector function to find an anchor element, and changes its href attribute using data from location.search.

To solve this lab, make the "back" link alert document.cookie.

## Cross Site Scripting
* 題目說在 submit feedback 的地方有問題，稍微觀察一下，back 對應的 href 是根據給的 param 來變換的，因為在 href 裡面，用 javascript:alert(1) 就可以過了
* 題目要求要 alert 出 cookie
```
payload = https://acd71f751fb147cac02dd3a8004100ec.web-security-academy.net/feedback?returnPath=javascript:alert(document.cookie)
```