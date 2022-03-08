# Lab: Reflected XSS into a JavaScript string with angle brackets HTML encoded

This lab contains a reflected cross-site scripting vulnerability in the search query tracking functionality where angle brackets are encoded. The reflection occurs inside a JavaScript string. To solve this lab, perform a cross-site scripting attack that breaks out of the JavaScript string and calls the alert function. 

## XSS 
* 觀察一下可以看到 search 的 value 會在 script 標籤裡面，這個時候只要截斷一下就可以執行到指定的指令了
```
payload = entroy';alert(1);'
```