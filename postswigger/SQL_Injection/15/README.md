# Lab: SQL injection vulnerability in WHERE clause allowing retrieval of hidden data

This lab contains an SQL injection vulnerability in the product category filter. When the user selects a category, the application carries out an SQL query like the following:

SELECT * FROM products WHERE category = 'Gifts' AND released = 1

To solve the lab, perform an SQL injection attack that causes the application to display details of all products in any category, both released and unreleased.

## SQL injection
* 很直白的題目，要拿到所有的 products
* 注入點在 `catagory`
```
payload = Pets%27%20or%20123=123%20--%20-
```