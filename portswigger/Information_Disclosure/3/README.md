# Lab: Source code disclosure via backup files

This lab leaks its source code via backup files in a hidden directory. To solve the lab, identify and submit the database password, which is hard-coded in the leaked source code.

## Information Disclosure
* 題目說在隱藏的 directory 中有 backup file，裡面有寫死的密碼，在 robots.txt 有隱藏的路徑，之後就可以找到密碼了