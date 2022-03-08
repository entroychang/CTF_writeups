# Lab: Reflected XSS into attribute with angle brackets HTML-encoded

This lab contains a reflected cross-site scripting vulnerability in the search blog functionality where angle brackets are HTML-encoded. To solve this lab, perform a cross-site scripting attack that injects an attribute and calls the alert function. 

## XSS
* 題目說有經過 html encode，所以新增標籤是沒辦法了，指能透過 `"` 截斷下面的 value 之後加個 onmouseover 之類的東西就可以了
```
payload = entroy" onmouseover="alert(1)
```