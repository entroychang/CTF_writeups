# Lab: Blind OS command injection with time delays

This lab contains a blind OS command injection vulnerability in the feedback function.

The application executes a shell command containing the user-supplied details. The output from the command is not returned in the response.

To solve the lab, exploit the blind OS command injection vulnerability to cause a 10 second delay.

## OS command injection
* 題目說在 feedback 那邊有問題，稍微試了一下在 email 那邊有點問題，用 `||` 隔開
```
payload = 123@123.com||sleep 10||
```