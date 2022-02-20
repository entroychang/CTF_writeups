# Lab: URL-based access control can be circumvented

This website has an unauthenticated admin panel at /admin, but a front-end system has been configured to block external access to that path. However, the back-end application is built on a framework that supports the X-Original-URL header.

To solve the lab, access the admin panel and delete the user carlos.

## Access Control Vulnerabilities
* 題目說有 X-Original_URL 這一個 header，稍微查了一下發現可以用它繞過題目的限制，卡的比較久的地方是我不知道參數要在哪裡帶入，找了一下發現還是在 GET 後面帶入，本來是寫在 X-Original_URL 裡面的，感覺像隔傻子