# Lab: Manipulating WebSocket messages to exploit vulnerabilities

This online shop has a live chat feature implemented using WebSockets.

Chat messages that you submit are viewed by a support agent in real time.

To solve the lab, use a WebSocket message to trigger an alert() popup in the support agent's browser.

## WebSockets
* 攔截一下改一下就可以了
```
payload = </td><img src=# onerror=alert(1)>
```