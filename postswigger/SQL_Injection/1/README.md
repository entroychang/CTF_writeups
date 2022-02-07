# Lab: SQL injection UNION attack, determining the number of columns returned by the query

This lab contains an SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response, so you can use a UNION attack to retrieve data from other tables. The first step of such an attack is to determine the number of columns that are being returned by the query. You will then use this technique in subsequent labs to construct the full attack.

To solve the lab, determine the number of columns returned by the query by performing an SQL injection UNION attack that returns an additional row containing null values.

## SQL Injection
* 注入點在 `category`
* 題目說只要確定有多少個 columns 即可，所以用 NULL 來確定一下到底有多少個 columns
```
payload = Toys+%26+Games%27%20union%20select%20NULL,NULL,NULL%20--%20-
```