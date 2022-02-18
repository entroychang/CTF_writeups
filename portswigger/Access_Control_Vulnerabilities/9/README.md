# Lab: Insecure direct object references

This lab stores user chat logs directly on the server's file system, and retrieves them using static URLs.

Solve the lab by finding the password for the user carlos, and logging into their account.

## Access Control Vulnerabilities
* 題目說會儲存使用者對話的 log，稍微觀察一下可以看到在 view transcript 的地方可以下載對話記錄，這個時候往前下載就可以看到其他使用者的 log 其中就有 password