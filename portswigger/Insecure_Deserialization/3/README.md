# Lab: Using application functionality to exploit insecure deserialization

 This lab uses a serialization-based session mechanism. A certain feature invokes a dangerous method on data provided in a serialized object. To solve the lab, edit the serialized object in the session cookie and use it to delete the morale.txt file from Carlos's home directory.

You can log in to your own account using the following credentials: wiener:peter

You also have access to a backup account: gregg:rosebud 

## Insecure Deserialization
* 看一下 session 的內容，其中有一個大頭貼的路徑，只要把路徑改成 `/home/carlos/morale.txt` 經過 delete account 發送就可以了