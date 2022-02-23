# Lab: Flawed enforcement of business rules

This lab has a logic flaw in its purchasing workflow. To solve the lab, exploit this flaw to buy a "Lightweight l33t leather jacket".

You can log in to your own account using the following credentials: wiener:peter

## Business Logic Vulnerabilities
* 題目說要 bypass 他的邏輯，可以看到一開始就送了 coupon，這個時候我們看到主畫面的最下面有一個 sign up new letter，這個時候可以拿到另外一個 coupon，這個時候發現如果輸入同一個 coupon 兩次會說不行，但是可以交叉使用，之後就可以買到目標商品了