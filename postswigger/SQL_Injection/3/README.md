# Lab: SQL injection UNION attack, retrieving data from other tables
This lab contains an SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response, so you can use a UNION attack to retrieve data from other tables. To construct such an attack, you need to combine some of the techniques you learned in previous labs.

The database contains a different table called users, with columns called username and password.

To solve the lab, perform an SQL injection UNION attack that retrieves all usernames and passwords, and use the information to log in as the administrator user.

## SQL injection
* 注入點在 `category`
* 照題目的說法，要拿別的 table 中的資料，可以用 NULL 來確定一下是多少個 columns，可以發現是兩個，剛好跟題目要求的 `users` table 是一樣的，所以可以直接拿
```
payload = 'union select username,password from users -- -
```
* 可以拿到 `administrator` 的帳號密碼