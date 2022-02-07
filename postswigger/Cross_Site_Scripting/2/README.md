# Lab: Stored XSS into HTML context with nothing encoded

This lab contains a stored cross-site scripting vulnerability in the comment functionality.

To solve this lab, submit a comment that calls the alert function when the blog post is viewed.

## Cross Site Scripting
* 可以看到網頁中有留言的地方，稍微看一下可以看到留言被包在 `<p>` 標籤裡面，跳脫之後就可以過關了
```
payload = </p><script>alert(1)</script>
```