# Lab: Information disclosure in version control history

This lab discloses sensitive information via its version control history. To solve the lab, obtain the password for the administrator user then log in and delete Carlos's account.

## Information Disclosure
* 題目說有敏感資訊洩漏，可以看到 .git directory 洩漏，因此我們可以用 githack 或是 wget 拿到 .git 裡面的所有資訊，用 `git log -p` 可以看到改動的 log 其中就有 admin 的密碼