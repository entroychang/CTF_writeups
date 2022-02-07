# Lab: Blind SQL injection with conditional responses

This lab contains a blind SQL injection vulnerability. The application uses a tracking cookie for analytics, and performs an SQL query containing the value of the submitted cookie.

The results of the SQL query are not returned, and no error messages are displayed. But the application includes a "Welcome back" message in the page if the query returns any rows.

The database contains a different table called users, with columns called username and password. You need to exploit the blind SQL injection vulnerability to find out the password of the administrator user.

To solve the lab, log in as the administrator user.

## SQL injection
* 題目說要用 blind based 拿到資料
* 然後說 `The application uses a tracking cookie for analytics` 可以猜到注入點在 cookie 有一個跟 track 有關的
* 之後就是用腳本拿資料了
* 然後要 dump 滿久的，建議去泡一杯咖啡或是洗個澡吧！