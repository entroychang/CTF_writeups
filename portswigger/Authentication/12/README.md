# Lab: Password brute-force via password change

This lab's password change functionality makes it vulnerable to brute-force attacks. To solve the lab, use the list of candidate passwords to brute-force Carlos's account and access his "My account" page.

* Your credentials: wiener:peter
* Victim's username: carlos
* Candidate passwords

## Authentication
* 題目說在改密碼那裏有點問題，稍微看了一下發現如果 current password 錯誤的話會 redirect 到 login page，如果把新密碼不匹配的話，會說 new password does not match，卡著之後就可以輸入錯的 current password 了，詳細的可以看腳本