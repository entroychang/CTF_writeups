# Lab: Modifying serialized objects

 This lab uses a serialization-based session mechanism and is vulnerable to privilege escalation as a result. To solve the lab, edit the serialized object in the session cookie to exploit this vulnerability and gain administrative privileges. Then, delete Carlos's account.

You can log in to your own account using the following credentials: wiener:peter 

## Insecure Deserialization
* 登入之後看一下 cookie 明顯可以 base64 decode，之後可以看到序列化的內容，只要把 admin 那邊的 boolean value 改成 1 就可以以 wiener 的身分訪問 admin panel