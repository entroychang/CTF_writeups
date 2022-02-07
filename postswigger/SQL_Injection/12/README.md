# Lab: Blind SQL injection with time delays and information retrieval

This lab contains a blind SQL injection vulnerability. The application uses a tracking cookie for analytics, and performs an SQL query containing the value of the submitted cookie.

The results of the SQL query are not returned, and the application does not respond any differently based on whether the query returns any rows or causes an error. However, since the query is executed synchronously, it is possible to trigger conditional time delays to infer information.

The database contains a different table called users, with columns called username and password. You need to exploit the blind SQL injection vulnerability to find out the password of the administrator user.

To solve the lab, log in as the administrator user.

## SQL injection
* 注入點在 cookie
* 題目說不會有任何不同的反饋如果 sql 語句有錯誤的話
* 所以說能造成不同的只有時間上的差異，加上 case when 語句造成 true false 的差異，透過時間的延遲來判斷
* dump 的時間真的很久，建議泡杯咖啡洗個澡 = = 
* 其他的就看 `script.py` 吧！