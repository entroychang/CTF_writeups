# Lab: Web shell upload via obfuscated file extension

This lab contains a vulnerable image upload function. Certain file extensions are blacklisted, but this defense can be bypassed using a classic obfuscation technique.

To solve the lab, upload a basic PHP web shell, then use it to exfiltrate the contents of the file /home/carlos/secret. Submit this secret using the button provided in the lab banner.

You can log in to your own account using the following credentials: wiener:peter

## File Upload Vulnerabilties
* 這一題上傳之後會發現他會看附檔銘，題目說混淆他一下，可以用 null byte bypass 一下
```
payload = a.php%00.jpg
```