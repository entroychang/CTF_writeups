# Lab: DOM XSS in document.write sink using source location.search

This lab contains a DOM-based cross-site scripting vulnerability in the search query tracking functionality. It uses the JavaScript document.write function, which writes data out to the page. The document.write function is called with data from location.search, which you can control using the website URL.

To solve this lab, perform a cross-site scripting attack that calls the alert function.

## Cross Site Scripting
* 題目說在 search query 有問題，稍微觀察一下可以看到在 `img` 標籤裡面有回饋剛剛打的字，一樣截斷就過了
```
payload = "><script>alert(1)</script>
```