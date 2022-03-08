# Lab: Stored XSS into anchor href attribute with double quotes HTML-encoded

This lab contains a stored cross-site scripting vulnerability in the comment functionality. To solve this lab, submit a comment that calls the alert function when the comment author name is clicked. 

## XSS
* 題目說要觸發 XSS 如果 attacker 的 username 被點擊的話，直接在 website 的地方輸入 payload 就可以了
```
payload = javascript:alert(1)
```