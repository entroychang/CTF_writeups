# Lab: Remote code execution via web shell upload

This lab contains a vulnerable image upload function. It doesn't perform any validation on the files users upload before storing them on the server's filesystem.

To solve the lab, upload a basic PHP web shell and use it to exfiltrate the contents of the file /home/carlos/secret. Submit this secret using the button provided in the lab banner.

You can log in to your own account using the following credentials: wiener:peter

## File Upload
* 用 wiener:peter 登入之後，有一個上傳頭像的地方，直接上傳 php 就可以了
* 題目說要讀取 /home/carlos/secret，用 readfile 就可以了
* 最後記得 submit 答案
```
<?php readfile("/home/carlos/secret"); ?>
```