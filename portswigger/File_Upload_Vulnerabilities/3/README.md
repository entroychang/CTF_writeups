# Lab: Web shell upload via path traversal

This lab contains a vulnerable image upload function. The server is configured to prevent execution of user-supplied files, but this restriction can be bypassed by exploiting a secondary vulnerability.

To solve the lab, upload a basic PHP web shell and use it to exfiltrate the contents of the file /home/carlos/secret. Submit this secret using the button provided in the lab banner.

You can log in to your own account using the following credentials: wiener:peter

## File Upload
* 這一題說檔案有 path traversal 的問題，稍微看了一下，如果正常上傳的話是可以的，可是 php code 不會被執行，這樣的話就回到上一層試一試，因為會過濾 ../ 用 ..%2f bypass 就可以了，這樣就可以 bypass 了
```
payload = <?php readfile("/home/carlos/secret"); ?>
```