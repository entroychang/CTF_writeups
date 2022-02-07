# Lab: Blind SQL injection with conditional errors

This lab contains a blind SQL injection vulnerability. The application uses a tracking cookie for analytics, and performs an SQL query containing the value of the submitted cookie.

The results of the SQL query are not returned, and the application does not respond any differently based on whether the query returns any rows. If the SQL query causes an error, then the application returns a custom error message.

The database contains a different table called users, with columns called username and password. You need to exploit the blind SQL injection vulnerability to find out the password of the administrator user.

To solve the lab, log in as the administrator user.

## SQL injection
* 資料庫是 `Oracle`
* 注入點是 cookie 中的 `TrackingId`
* 題目說如果錯的話會回傳 500 其他狀況都是 200，這樣的話可以從 case when 條件以及 time based 兩種方式來 dump 資料，題目希望用 case when 這種可以給定 true false 的情況，如果成立 true 反之 false 回傳 500
* sqlmap 可以檢測出 time based，我自己沒有等他 dump，如果懶得寫腳本的話，sqlmap 理論上應該 dump 的出來不過要等一段時間就是了
* 由於對 `Oracle` sql 的語法比較不熟，湊了好一陣子才弄到一個正確的 payload
* 詳情參考 `script.py` 裡面的內容
* 拿到 password 之後登入