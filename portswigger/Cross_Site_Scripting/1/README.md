# Lab: Reflected XSS into HTML context with nothing encoded

This lab contains a simple reflected cross-site scripting vulnerability in the search functionality.

To solve the lab, perform a cross-site scripting attack that calls the alert function.

## Cross Site Scripting
* 觀察一下網頁可以看到搜尋的結果包在 `<h1>` 標籤裡面，所以跳出標籤之後用 `<script>` 標籤 alert 出任意值就可以過關了
```
payload = </h1><script>alert(1)</script>
```