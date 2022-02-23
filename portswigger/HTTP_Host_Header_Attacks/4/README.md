# Lab: Routing-based SSRF

This lab is vulnerable to routing-based SSRF via the Host header. You can exploit this to access an insecure intranet admin panel located on an internal IP address.

To solve the lab, access the internal admin panel located in the 192.168.0.0/24 range, then delete Carlos.

## HTTP Host Header Attack
* 題目說 Host 有 SSRF，用腳本爆破一下，之後訪問 admin panel 刪掉使用者就可以了