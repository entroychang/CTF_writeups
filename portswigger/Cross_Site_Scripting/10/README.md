# Lab: Reflected DOM XSS

This lab demonstrates a reflected DOM vulnerability. Reflected DOM vulnerabilities occur when the server-side application processes data from a request and echoes the data in the response. A script on the page then processes the reflected data in an unsafe way, ultimately writing it to a dangerous sink.

To solve this lab, create an injection that calls the alert() function.

## Cross Site Scripting
* 題目說在 search 有問題，觀察一下 searchResults.js 裡面他把東西直接放到 eval 裡面
* 有一個 api 可以看到說回傳的東西是 json，因為輸入雙引號會被跳脫，所以需要再輸入一個跳脫符號來跳脫跳脫符號，然後閉合一下 json 然後記得註解掉後面的東西
```
payload = \"-alert(1)}//
```