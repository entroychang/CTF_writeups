# Lab: Modifying serialized data types

 This lab uses a serialization-based session mechanism and is vulnerable to authentication bypass as a result. To solve the lab, edit the serialized object in the session cookie to access the administrator account. Then, delete Carlos.

You can log in to your own account using the following credentials: wiener:peter 

## Insecure Deserialization
* 登入之後看到 cookie，base64 decode 過後可以看到 username 的部份，先把它改成 administrator，這個時候會發現頁面會吐 token 給我們，在把 token 改掉就可以了