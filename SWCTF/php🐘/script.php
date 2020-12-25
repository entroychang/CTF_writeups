<?php
    for ($i = 0; $i < 999999999; $i ++) {
        if (substr(md5("CMRDB" . $i), 0, 6) == md5("s1885207154a")) {
            print_r($i);
            break;
        }
    }
?>