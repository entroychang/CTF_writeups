# Lab: Reflected XSS into HTML context with most tags and attributes blocked

 This lab contains a reflected XSS vulnerability in the search functionality but uses a web application firewall (WAF) to protect against common XSS vectors.

To solve the lab, perform a cross-site scripting attack that bypasses the WAF and calls the print() function. 

## XSS
* 有 waf 要 bypass，可以發現 onresize 沒有被擋掉，在 exploit server 用 iframe 的方式嵌入目標網站，記得用 onload 改一下 size