# CyberYoddhaCTF write up

### Misc
* Lorem Ipsum
    > 125
    > Lorem ipsum dolorc sit amet, consectetury adipiscing celit, sed dot eiusmod tempor incifdidunt ut labore et dolore magna aliqual. Ut enim ad minima veniam, quist nostrud exercitation ullamcoi laboris nisin ut aliquip ex eai commodos consequat. Duis caute irure dolor in reprehenderit in voluptate velit oesse cillum dolore eu fugiat nulla pariatur. Excepteur osint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim lid est laborum.
    * 基本上就是把 `Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.` 對著刪掉就可以了，
* Bashing My Head
    > 450 
    > This program won't let me get in! It says im not a bot, but I believe I am! I think so, because I can't solve captchas. Are you bot level brain?
    > nc cyberyoddha.baycyber.net 10006

### Forensics
* Image Viewer
    > 125
    > My friend took this image in a cool place
    * 用 strings 檢查一下 `strings shoob_2.jpeg | grep CYCTF{`
    * 想不到吧
    * flag : `CYCTF{h3h3h3_1m@g3_M3t@d@t@_v13w3r_ICU}`
* The row beneath
    > 150
    > We intercepted a super secret plan. Can you find anything inside of it?
    * 一樣用 strings 檢查一下 `strings plan.png | grep CYCTF{`
    * 想不到吧
    * flag : `CYCTF{L00k_1n_th3_h3x_13h54d56}`
* What’s the password?
    > 175
    > My friend gave me this file, he said there was something hidden
    > hint : You may need to use the contents in the image to help you.
    * 用的是 steghide，詳細怎麼用可以參考一下[這一篇](https://ctftime.org/writeup/17314)
    * 基本上解法是一樣的，把 passphrase 改成 sudo 就可以了
    * flag : `CYCTF{U$3_sud0_t0_achi3v3_y0ur_dr3@m$!}`
* Flag delivery
    > 225 
    > Our good friend Yeltsa Kcir ordered a flag for us from the renowned flag delivery service. We got their letter today, but we can’t see the flag they sent us. Apparently Yeltsa has been talking with the scientist Odec Esrom. Can you find the flag he hid for us?
* Steg 2
    > 300
    > Where's the pizza?
    * 用 stegsolve 解
    * flag : `CYCTF{l$b_st3g@n0gr@phy_f0r_th3_w1n}`
* Steg Ultimate
    > 450
    > You reached the final stage, can you unravel your way out of this one?
* I’m Not Lying
    > 450 
    > Our field agents had captured someone who we had suspected to have information about a flag. The recording of their conversation is attached below.
    > hint : Listen very carefully around the 12 second mark.

### Cryptography
* Beware the Ides of March
    > 50 
    > JFJAM{j@3$@y_j!wo3y}
    * caeser
    * flag : `CYCTF{c@3$@r_c!ph3r}`
* Home Base
    > 125
    > 4a5a57474934325a47464b54475632464f4259474336534a4f564647595653574a354345533454434b52585336564a524f425556435533554e4251574f504a35
    * 第一步先用 hex 轉譯一下 `JZWGI42ZGFKTGV2FOBYGC6SJOVFGYVSWJ5CES4TCKRXS6VJROBUVCU3UNBQWOPJ5`
    * 再用 base32 `NldsY1U3WEppazIuJlVVODIrbTo/U1piQSthag==`
    * 再用 base64 `6WlcU7XJik2.&UU82+m:?SZbA+aj`
    * 再用 base85
    * flag : `CYCTF{it5_@_H0m3_2un!}`
* Sus
    > 200
    > We picked up on some suspicious activity at a nearby salad bar. We sat down to talk with the manager. He was quite nervous during the interview, but he slid this message to us: ooflgqofllcedopwvtnhyacwllhehdl. Can you find out what it means?
    > hint : We ordered some salad as well, and we made sure to have it drizzled with some vinegar.
    * 以 hint 來看的話滿明顯是 [Vigenère](https://www.guballa.de/vigenere-solver)
    * flag : `CYCTF{wouldyoulikesomevinegarwiththat}`
* Rak 1
    > 250
    > you might want to get some popcorn for this one: df 48 b8 6e 14 87 f6 8b a8 9c 2c c8 d3 2b ec 73 06 01 0a 01 e2 75 26 fe 38 d5 67 59 e6 55 33 b2 aa e0 2d 67 34 48 7d 52 8a 18 0d 36 d7 f2 18 8f: B55D3CE3183E06928 BA82F8980B661A30A 6C4B2BA499062CF6A 31EB1CD581E55: 00 01 02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f.
    > hahabox0 解的
    * 普通的AES CBC
    * 上面是encrypt
    * 中間是key
    * 下面是vector
    * 丟進下面的鏈接就解好了
    * http://aes.online-domain-tools.com/
* GATTACA
    > 300
    > We were following a suspect in hot pursuit when he suddenly disappeared. We were left standing in front of a mysterious lab. We didn’t find much, except for a small sheet of paper with this message printed on it. Can you help us decipher it?
    > hint : Note: You may find multiple similar ciphers. Use what you know to find the right one
* (un)F0r7un@t3
    > 450
    > Three of our best agents: Ron, Adi, and Leonard, were investigating the notorious hacker group known as the unF0r7un@t3s. Fortunately, one of their members dropped a fortune cookie behind from their last scandal. We believe it might be a clue to where they will attack next. The fortune inside read: You will find your fortune at 23441987, 31018357. The lucky numbers on the back were, n52035749, e101, and *10^-6. What location do you think they will be heading to next?
    > hint : Multiply the last lucky number to the two answers for good fortune.

### OSINT
* Back to the Future IV
    > 150
    > I thought I got some points, but they got deleted. Can you find them?
    > hahabox0 解的
    * 用 wayback machine `https://cyberyoddha.baycyber.net/*`
    * 找 `https://cyberyoddha.baycyber.net/api/v1/teams/2/solves` 可以拿到 flag
    * flag : `CYCTF{Tr@v3l_b@ck_1n_t1m3_t0_g3t_th3_fl@g}`
* Flag Storage 3
    > 350
    > Yeltsa Kcir is back at it again. He made us a website to store flags, and he said that he stored a demo flag in there. He said if you had any questions to contact him at yeltsakcir@gmail.com, and he mentioned that he liked to reuse passwords, whatever that means. Anyways, can you get the flag?
    > https://flag-storage-3.web.app
### Web Exploitation
> web 出的超爛 der
* Look Closely
    > 50 
    > https://inspect.cyberyoddha.team
    * 找原始碼 ctrl + f `CYCTF{`
    * flag : `CYCTF{1nSp3t_eL3M3nt?}`
* Disallow
    > 100
    > My friend helped make this website, but he said that there was a page thtat I couldn't visit. Can you find it?
    > https://crawlies.cyberyoddha.team
    * `I hate creepy crawlies.` 推測是 robots.txt
    * 訪問 https://crawlies.cyberyoddha.team/robots.txt 
        ```
        Disallow: /n0r0b0tsh3r3/flag.html
        ```
    * 既然都 disallow 了，當然要訪問一下啊 X)
    * flag : `CYCTF{d33r0b0t$_r_sUp3r10r}`
* Data Store
    > 175
    > I like shopping online, but this sight isn’t letting me in for some reason… 
    > https://cyberyoddha.baycyber.net:33002/
    * 基本的 sql injection 
    * payload : `'or 1=1 -- `
    * flag : `CYCTF{1_l0v3_$q1i}`
#### 在 Data Store 系列裡面，存在一個嚴重的漏洞，因為他是用 session 判斷是否成功在登入狀態，用的是 flask session，我直接用第一題的 session 拿到所有系列的 flag，不過考的都是 sql injection，waf 要自己猜而且他的回饋感很不好
* Data Store 2
    > 225
    > You got past the first one, can you get this?
    > https://cyberyoddha.baycyber.net:33003
* Data Store 3
    > 300
    > It's been a long journey, so let's do one last one! Apparently there's a debug parameter somewhere, i'm just not sure where...
    > https://cyberyoddha.baycyber.net:33004/
* Something Sw33t
    > 200
    > My sweet friend tried telling me about something on this page, but I can’t seem to find anything… Can you help me:
    > https://cyberyoddha.baycyber.net:33001
    * 直接看 cookies
        ```
        don't look here = .eJyVU2tPwjAU_StLP4tsA9QR90EUxMWRQHQvNdh1d6zYDrOHZiP7746pgUhsoGna5tzTnnNvbtfoKs0YFK0R5pQVLRO4D0mK-mcnKGwg1F-j6yLOIoqlby7qP61RAClJ6HtGV_GGIQW02fz5HPVRTAmgqqqfYHixH_a5Jjuq1cXORHbtntxQY8xhn_pHuaqZB2iDLlB3-aj0HtzaASudzkQhY4P59qMucDFeJZjAESainONY4GGD6k3of9HnXJZDbbMC2Z5DvINcNKu_gwRb_AcJ925BV2mfqu1Lpf2qtLvqIflkEUjijKYKu7GG3rl5m4WmpZWebYVga4qjKhHYBnM67COwtIhwKyQ1RuKZJkh-RsnbEfUuAILfuRkCo8HY6DnqKHZtlgsM3EMM0gDnKV5AcoiFPOJc1PPLwWddE-ZNdVGnGbiodU2cpNFBfUYjKhYN3eVAJoq2Mjt3pUB4WP91utviL1X1BXD8TWE.X4ovdw.rz4sSG_k2heOMf7Cw_C6Kliw7Ms
        ```
    * 用 flask_session_cookie_manager decode 一下
    * `python3 flask_session_cookie_manager3.py decode -c ".eJyVU2tPwjAU_StLP4tsA9QR90EUxMWRQHQvNdh1d6zYDrOHZiP7746pgUhsoGna5tzTnnNvbtfoKs0YFK0R5pQVLRO4D0mK-mcnKGwg1F-j6yLOIoqlby7qP61RAClJ6HtGV_GGIQW02fz5HPVRTAmgqqqfYHixH_a5Jjuq1cXORHbtntxQY8xhn_pHuaqZB2iDLlB3-aj0HtzaASudzkQhY4P59qMucDFeJZjAESainONY4GGD6k3of9HnXJZDbbMC2Z5DvINcNKu_gwRb_AcJ925BV2mfqu1Lpf2qtLvqIflkEUjijKYKu7GG3rl5m4WmpZWebYVga4qjKhHYBnM67COwtIhwKyQ1RuKZJkh-RsnbEfUuAILfuRkCo8HY6DnqKHZtlgsM3EMM0gDnKV5AcoiFPOJc1PPLwWddE-ZNdVGnGbiodU2cpNFBfUYjKhYN3eVAJoq2Mjt3pUB4WP91utviL1X1BXD8TWE.X4ovdw.rz4sSG_k2heOMf7Cw_C6Kliw7Ms"`
        ```
        '{"Astley-Family-Members":6,"family":{"Cynthia Astley":[{"description":{" di":{" b__":"nice"}},"flag":{" di":{" b__":"bm90X2V4aXN0YW50"}},"name":{" di":{" b__":"Cynthia Astley"}}},{"description":{" di":{" b__":"nicee="}},"flag":{" di":{" b__":"YmFzZTY0X2lzX3N1cHJlbWU="}},"name":{" di":{" b__":"Horace Astley"}}},{"description":{" di":{" b__":"human"}},"flag":{" di":{" b__":"flag=flag"}},"name":{" di":{" b__":"\\u00f9\\u00ec\\u00f9\\u00fa\\u00ec\\u00f8\\u00fb\\u00ec\\u00fd\\u00f8\\u00ec\\u00ff\\u00fa\\u00ec\\u00fe41/.2/<1/`1/42"}}},{"description":{" di":{" b__":"the man"}},"flag":{" di":{" b__":"Q1lDVEZ7MGtfMV9zZWVfeW91X21heWJlX3lvdV9hcmVfc21hcnR9"}},"name":{" di":{" b__":"Rick Astley"}}},{"description":{" di":{" b__":"yeedeedeedeeeeee"}},"flag":{" di":{" b__":"dHJ5X2FnYWlu"}},"name":{" di":{" b__":"Lene Bausager"}}},{"description":{" di":{" b__":"uhmm"}},"flag":{" di":{" b__":"bjBwZWVlZQ=="}},"name":{" di":{" b__":"Jayne Marsh"}}},{"description":{" di":{" b__":"hihi"}},"flag":{" di":{" b__":"bjBfYjB0c19oM3Iz"}},"name":{" di":{" b__":"Emilie Astley"}}}]}}'
        ```
    * 其中把 `Q1lDVEZ7MGtfMV9zZWVfeW91X21heWJlX3lvdV9hcmVfc21hcnR9` base64 decode 一下
    * flag : `CYCTF{0k_1_see_you_maybe_you_are_smart}`

### Binary Exploitation
> 我的 pwn 跟 reverse 超爛 der
> 除了第一題，其他的都不是我解的
* Overflow 1
    > 125
    > ez overflow.
    > nc cyberyoddha.baycyber.net 10001
    * 用 `AAAAAAAAAAAAAAAAa` 就可以拿到 shell 了
    * flag : `CYCTF{st@ck_0v3rfl0ws_@r3_3z}`
* Overflow 2
    > ez overflow (or is it?)
    > nc cyberyoddha.baycyber.net 10002
    > hahabox0 解的
    * stack return address
    * pwntool丟offset(16+12就可以了)
    * 0x08049172 sym.run_shell
    * flag:`CYCTF{0v3rfl0w!ng_v@ri@bl3$_i$_3z}`
* Overflow 3
    > looks like buffer overflows aren’t so easy anymore.
    > nc cyberyoddha.baycyber.net 10003
    > hahabox0 解的
    * stack 下面的變數
    * pwntool offset 16
    * p32 d3adb33f
    * flag:`CYCTF{wh0@_y0u_jump3d_t0_th3_funct!0n}`
### Reverse Engineering
* Password 1
    > 125
    > We uncovered the first password encryption file. Can you crack it for us?
    * password1.py
        ```python=
        import random

        def checkPassword(password):
            if(len(password) != 43):
              return False
            if(password[26] == 'r' and
              password[33] == 't' and
              password[32] == '3' and
              password[16] == '3' and
              password[4] == 'F' and
              password[21] == 'r' and
              password[38] == '1' and
              password[18] == 'c' and
              password[22] == '@' and
              password[31] == 'g' and
              password[7] == 'u' and
              password[0] == 'C' and
              password[6] == 'p' and
              password[39] == '3' and
              password[3] == 'T' and
              password[25] == '3' and
              password[29] == 't' and
              password[42] == '}' and
              password[12] == 'g' and
              password[23] == 'c' and
              password[30] == '0' and
              password[40] == '3' and
              password[28] == '_' and
              password[20] == '@' and
              password[27] == '$' and
              password[17] == '_' and
              password[35] == '3' and
              password[8] == '7' and
              password[24] == 't' and
              password[41] == '7' and
              password[13] == '_' and
              password[5] == '{' and
              password[2] == 'C' and
              password[11] == 'n' and
              password[9] == '7' and
              password[15] == 'h' and
              password[34] == 'h' and
              password[1] == 'Y' and
              password[10] == '1' and
              password[37] == '_' and
              password[14] == 't' and
              password[36] == 'r' and
              password[19] == 'h'):
              return True
            return False

        password = input("Enter password: ")
        if(checkPassword(password)):
          print("PASSWORD ACCEPTED\n")
        else:
          print("PASSWORD DENIED\n")
        ```
    * 基本上把它組一組就有 flag 了
    * python script
        ```python=
        string = '''
        password[26] == 'r' and
        password[33] == 't' and
        password[32] == '3' and
        password[16] == '3' and
        password[4] == 'F' and
        password[21] == 'r' and
        password[38] == '1' and
        password[18] == 'c' and
        password[22] == '@' and
        password[31] == 'g' and
        password[7] == 'u' and
        password[0] == 'C' and
        password[6] == 'p' and
        password[39] == '3' and
        password[3] == 'T' and
        password[25] == '3' and
        password[29] == 't' and
        password[42] == '}' and
        password[12] == 'g' and
        password[23] == 'c' and
        password[30] == '0' and
        password[40] == '3' and
        password[28] == '_' and
        password[20] == '@' and
        password[27] == '$' and
        password[17] == '_' and
        password[35] == '3' and
        password[8] == '7' and
        password[24] == 't' and
        password[41] == '7' and
        password[13] == '_' and
        password[5] == '{' and
        password[2] == 'C' and
        password[11] == 'n' and
        password[9] == '7' and
        password[15] == 'h' and
        password[34] == 'h' and
        password[1] == 'Y' and
        password[10] == '1' and
        password[37] == '_' and
        password[14] == 't' and
        password[36] == 'r' and
        password[19] == 'h'
        '''

        string = string.replace(' ', '').replace('==', '=').replace('and', '')

        password = [''] * 43
        for i in string.split():
            exec(i)
        print(''.join(password))
        ```
    * flag : `CYCTF{pu771ng_th3_ch@r@ct3r$_t0g3th3r_1337}`
* Password 2
    > 175
    > You did so well on the last one, can you try this?
    * password2.py
        ```python=
        import random

        def checkPassword(password):
            if(len(password) != 47):
              return False
            newPass = list(password)
            for i in range(0,9):
              newPass[i] = password[i]
            for i in range(9,24):
              newPass[i] = password[32-i]
            for i in range(24,47,2):
              newPass[i] = password[70-i]
            for i in range(45,25,-2):
              newPass[i] = password[i]
            password = "".join(newPass);
            
            # 我自己加的
            print(password)
            return password == "CYCTF{ju$@rcs_3l771l_@_t}bd3cfdr0y_u0t__03_0l3m"

        password = input("Enter password: ")
        if(checkPassword(password)):
          print("PASSWORD ACCEPTED\n")
        else:
          print("PASSWORD DENIED\n")
        ```
    * 直接帶入 `CYCTF{ju$@rcs_3l771l_@_t}bd3cfdr0y_u0t__03_0l3m` 拿到 flag
    * flag : `CYCTF{ju$t_@_l177l3_scr@mbl3_f0r_y0u_t0_d3c0d3}`
* YayRev
    > 200
    > Let’s brush up sum pythan skillz… (no flag wrapper)
    > hahabox0 解的
    * yayrev.py
        ```python=
        flag="**REDACTED**"
        proficuous =flag
        saxicolous = [ord(excogitate) for excogitate in proficuous]
        ebullient  = (saxicolous[-5:]);  import random
        second = (saxicolous[:-5])
        sesquipedalian = ''.join(map(chr,ebullient)) + ''.join(map(chr,second))
        vravar = ''.join([chr(permutation.islower() and ((ord(permutation) - 84) % 26) + 97
                                or permutation.isupper() and ((ord(permutation) - 52) % 26) + 65
                                or ord(permutation))
                            for permutation in sesquipedalian])

        auspicious = []
        for luminescent in vravar:
            auspicious.append(luminescent)
        for cupidity in range(200):
            second = []
            superabundant=random.choice(auspicious)
            print( "mac>>>[" + str(auspicious.index(superabundant)) + "] " + "== " + "\"" + superabundant + "\"" + " and")


        """
        mac>>>[15] == "Q" and
        mac>>>[3] == "B" and
        mac>>>[8] == "n" and
        mac>>>[9] == "_" and
        mac>>>[8] == "n" and
        mac>>>[17] == "C" and
        mac>>>[9] == "_" and
        mac>>>[14] == "a" and
        mac>>>[14] == "a" and
        mac>>>[4] == "A" and
        mac>>>[6] == "u" and
        mac>>>[0] == "l" and
        mac>>>[10] == "y" and
        mac>>>[8] == "n" and
        mac>>>[15] == "Q" and
        mac>>>[13] == "R" and
        mac>>>[5] == "J" and
        mac>>>[2] == "U" and
        mac>>>[17] == "C" and
        mac>>>[8] == "n" and
        mac>>>[3] == "B" and
        mac>>>[2] == "U" and
        mac>>>[7] == "0" and
        mac>>>[16] == "-" and
        mac>>>[11] == "3" and
        mac>>>[8] == "n" and
        mac>>>[14] == "a" and
        mac>>>[5] == "J" and
        mac>>>[15] == "Q" and
        mac>>>[5] == "J" and
        mac>>>[9] == "_" and
        mac>>>[11] == "3" and
        mac>>>[7] == "0" and
        mac>>>[17] == "C" and
        mac>>>[16] == "-" and
        mac>>>[17] == "C" and
        mac>>>[17] == "C" and
        mac>>>[4] == "A" and
        mac>>>[6] == "u" and
        mac>>>[1] == "g" and
        mac>>>[13] == "R" and
        mac>>>[1] == "g" and
        mac>>>[11] == "3" and
        mac>>>[5] == "J" and
        mac>>>[2] == "U" and
        mac>>>[14] == "a" and
        mac>>>[17] == "C" and
        mac>>>[8] == "n" and
        mac>>>[11] == "3" and
        mac>>>[1] == "g" and
        mac>>>[15] == "Q" and
        mac>>>[4] == "A" and
        mac>>>[12] == "t" and
        mac>>>[1] == "g" and
        mac>>>[15] == "Q" and
        mac>>>[12] == "t" and
        mac>>>[3] == "B" and
        mac>>>[5] == "J" and
        mac>>>[16] == "-" and
        mac>>>[4] == "A" and
        mac>>>[1] == "g" and
        mac>>>[17] == "C" and
        mac>>>[11] == "3" and
        mac>>>[4] == "A" and
        mac>>>[4] == "A" and
        mac>>>[9] == "_" and
        mac>>>[7] == "0" and
        mac>>>[14] == "a" and
        mac>>>[9] == "_" and
        mac>>>[10] == "y" and
        mac>>>[9] == "_" and
        mac>>>[2] == "U" and
        mac>>>[1] == "g" and
        mac>>>[14] == "a" and
        mac>>>[12] == "t" and
        mac>>>[8] == "n" and
        mac>>>[12] == "t" and
        mac>>>[7] == "0" and
        mac>>>[9] == "_" and
        mac>>>[0] == "l" and
        mac>>>[0] == "l" and
        mac>>>[4] == "A" and
        mac>>>[1] == "g" and
        mac>>>[15] == "Q" and
        mac>>>[17] == "C" and
        mac>>>[15] == "Q" and
        mac>>>[15] == "Q" and
        mac>>>[11] == "3" and
        mac>>>[9] == "_" and
        mac>>>[3] == "B" and
        mac>>>[6] == "u" and
        mac>>>[3] == "B" and
        mac>>>[13] == "R" and
        mac>>>[6] == "u" and
        mac>>>[15] == "Q" and
        mac>>>[14] == "a" and
        mac>>>[16] == "-" and
        mac>>>[10] == "y" and
        mac>>>[3] == "B" and
        mac>>>[13] == "R" and
        mac>>>[9] == "_" and
        mac>>>[10] == "y" and
        mac>>>[12] == "t" and
        mac>>>[6] == "u" and
        mac>>>[7] == "0" and
        mac>>>[13] == "R" and
        mac>>>[16] == "-" and
        mac>>>[17] == "C" and
        mac>>>[2] == "U" and
        mac>>>[7] == "0" and
        mac>>>[2] == "U" and
        mac>>>[4] == "A" and
        mac>>>[8] == "n" and
        mac>>>[5] == "J" and
        mac>>>[5] == "J" and
        mac>>>[16] == "-" and
        mac>>>[0] == "l" and
        mac>>>[6] == "u" and
        mac>>>[8] == "n" and
        mac>>>[8] == "n" and
        mac>>>[1] == "g" and
        mac>>>[9] == "_" and
        mac>>>[11] == "3" and
        mac>>>[15] == "Q" and
        mac>>>[12] == "t" and
        mac>>>[9] == "_" and
        mac>>>[2] == "U" and
        mac>>>[14] == "a" and
        mac>>>[5] == "J" and
        mac>>>[9] == "_" and
        mac>>>[16] == "-" and
        mac>>>[12] == "t" and
        mac>>>[3] == "B" and
        mac>>>[4] == "A" and
        mac>>>[2] == "U" and
        mac>>>[5] == "J" and
        mac>>>[0] == "l" and
        mac>>>[2] == "U" and
        mac>>>[10] == "y" and
        mac>>>[0] == "l" and
        mac>>>[7] == "0" and
        mac>>>[11] == "3" and
        mac>>>[15] == "Q" and
        mac>>>[4] == "A" and
        mac>>>[10] == "y" and
        mac>>>[15] == "Q" and
        mac>>>[1] == "g" and
        mac>>>[10] == "y" and
        mac>>>[0] == "l" and
        mac>>>[8] == "n" and
        mac>>>[6] == "u" and
        mac>>>[15] == "Q" and
        mac>>>[7] == "0" and
        mac>>>[8] == "n" and
        mac>>>[17] == "C" and
        mac>>>[11] == "3" and
        mac>>>[1] == "g" and
        mac>>>[1] == "g" and
        mac>>>[15] == "Q" and
        mac>>>[14] == "a" and
        mac>>>[4] == "A" and
        mac>>>[2] == "U" and
        mac>>>[3] == "B" and
        mac>>>[17] == "C" and
        mac>>>[14] == "a" and
        mac>>>[7] == "0" and
        mac>>>[1] == "g" and
        mac>>>[12] == "t" and
        mac>>>[6] == "u" and
        mac>>>[7] == "0" and
        mac>>>[17] == "C" and
        mac>>>[3] == "B" and
        mac>>>[17] == "C" and
        mac>>>[12] == "t" and
        mac>>>[13] == "R" and
        mac>>>[15] == "Q" and
        mac>>>[3] == "B" and
        mac>>>[0] == "l" and
        mac>>>[2] == "U" and
        mac>>>[9] == "_" and
        mac>>>[3] == "B" and
        mac>>>[6] == "u" and
        mac>>>[16] == "-" and
        mac>>>[0] == "l" and
        mac>>>[16] == "-" and
        mac>>>[2] == "U" and
        mac>>>[8] == "n" and
        mac>>>[15] == "Q" and
        mac>>>[16] == "-" and
        mac>>>[1] == "g" and
        mac>>>[0] == "l" and
        mac>>>[17] == "C" and
        mac>>>[7] == "0" and
        mac>>>[3] == "B" and
        mac>>>[7] == "0" and
        mac>>>[6] == "u" and
        mac>>>[1] == "g" and
        mac>>>[10] == "y" and
        mac>>>[12] == "t" and
        mac>>>[11] == "3" and
        """
        ```
    * 基本上把 mac 排好 `lgUBAJu0n_y3tRaQ-C`，再經過 ROT-13 `ytHONWh0a_l3gEnD-P`
    * 需要注意一點：前五個字要丟到後面，在上面的 py 有寫到 `Wh0a_l3gEnD-PytHON`
    * flag : `Wh0a_l3gEnD-PytHON`
* Password 3
    > 225
    > This one won’t be so easy
    * password3.py
        ```python=
        import base64

        def checkPassword(password):
        if(len(password) != 40):
          return False
          newPass = list(password)
          for i in range(0,40):
            newPass[i] = chr(ord(newPass[i]) ^ 0x55)
          finalPass = "".join(newPass)
          passBytes = finalPass.encode("ascii")
          base64_bytes = base64.b64encode(passBytes)
          base64_string = base64_bytes.decode("ascii")
          print(base64_string)
          return base64_string == "FgwWARMuF2UhPQotZScKFTsxCjcVJmYKY2FqCiE9FSEmCjJlMTksKA=="

        password = input("Enter password: ")
        if(checkPassword(password)):
          print("PASSWORD ACCEPTED\n")
        else:
          print("PASSWORD DENIED\n")
        ```
    * 基本上這一題需要還原一下他的邏輯
    * 不變的還是 base64_string，需要拿它來進行解密
    * 之後先經過 decode 過後，直接丟到迴圈裡面去做 xor
    * 出來的就是 flag 了
    * python script
        ```python=
        import base64

        base64_string = "FgwWARMuF2UhPQotZScKFTsxCjcVJmYKY2FqCiE9FSEmCjJlMTksKA=="
        base64_bytes = base64.b64decode(base64_string)
        newPass = list(base64_bytes.decode("ascii"))
        for i in range(0,40):
            newPass[i] = chr(ord(newPass[i]) ^ 0x55)

        print(''.join(newPass))
        ```
    * flag : `CYCTF{B0th_x0r_@nd_b@s3_64?_th@ts_g0dly}`
* babyrev
    > 300
    > We didn’t want to overwhelm you, so let's start with baby rev;

### Shebang
* shebang0
    > 125
    > Welcome to the Shebang Linux Series. Here you will be tested on your basic command line knowledge! These challenges will be done threough an ssh connection. Also please do not try and mess up the challenges on purpose, and report any problems you find to the challenge author. You can find the passwords at /etc/passwords. The username is the challenge title, shebang0-6, and the password is the previous challenges flag, but for the first challenge, its shebang0
    > The first challenge is an introductory challenge. Connect to cyberyoddha.baycyber.net on port 1337 to recieve your flag!
    * 這一題直接 ssh 進去看
    * `ssh shebang0@cyberyoddha.baycyber.net -p 1337`
    * password : `shebang0`
    * 輸入 `ls -al`，看到 `.flag.txt`
    * 直接 cat 他 `cat .flag.txt`
    * flag : `CYCTF{w3ll_1_gu3$$_b@sh_1s_e@zy}`
* shebang1
    > 125
    > This challenge is simple.
    * 直接 `ls -al` 看到 flag.txt
    * 直接 `cat flag.txt` 發現太多輸出
    * 用 `cat flag.txt | grep CYCTF{` 來查看
    * flag : `CYCTF{w3ll_1_gu3$$_y0u_kn0w_h0w_t0_gr3p}`
* shebang2
    > 150
    > This is a bit harder
    * 進去可以看到有 100 個目錄，每個目錄下有 100 個 file 
    * 用迴圈一個一個訪問直到找到 flag
    * payload : 
        ```bash=
        for i in `ls`; \
        do \
            cd ~/$i; \
            for j in `ls`; \
                do \
                cat $j | grep CYCTF{ ; 
            done \
        done
        ```
    * flag : `CYCTF{W0w_th@t$_@_l0t_0f_f1l3s}`
* shebang3
    > 150
    > These files are the same...
    * 有兩個 file 
    * 用 diff 來比較兩者 `diff file.txt file2.txt`
    * flag : `CYCTF{SPOT_TH3_D1FF}`
* shebang4
    > 200
    > Since you have been doing so well, I thought I would make this an easy one.
    > hahabox0 解的
    * payload : `scp -P 1337 shebang4@cyberyoddha.baycyber.net:flag.png ~/`
    * 在本地端執行歐
    * 在本地端執行歐
    * 在本地端執行歐
    * 因為我做了傻事，提醒一下自己 Ｑ
    * flag : `CYCTF{W3ll_1_gu3$$_th@t_w@s_actually_easy}`
* shebang5
    > 250
    > there is a very bad file on this Server. can yoU fInD it.
    * 這題有給一個提示是 SUID
    * `find / -perm /4000 -exec ls -al {} \;` 找一下符合的條件
    * 如果不知道指令是什麼意思，可以參考一下鳥哥的文章 [link](http://linux.vbird.org/linux_basic/0220filemanager.php#find)
    * 之後可以看到一個關鍵的人名 `shebang6`
    * 之後找一下這個人 `find / -user shebang6`
        ```bash=
        /var/cat
        /etc/passwords/shebang6
        ```
    * 可以看到兩個關鍵的檔案
    * 分別 file 一下可以知道 cat 是 `setuid executable`
    * shebang6 是 `regular file`
    * 所以用 cat 跑一下 shebang6 會發身什麼事 `/var/cat /etc/passwords/shebang6`
    * flag : `CYCTF{W3ll_1_gu3$$_SU1D_1$_e@$y_fl@g$}`

### Password Cracking
* secure (i think?)
    > 150
    > smh I can’t even crack this password: b0439fae31f8cbba6294af86234d5a28 Note: Don’t use a flag wrapper for this challenge
    * md5 hash 
    * 直接上網搜就有答案了
    * flag : `securepassword`
* Crack the Zip!
    > 200
    > I'm not able to get into this zip file ...
    * 用 fcrackzip 來解
    * 直接用 rockyou.txt 來爆破
    * payload : `fcrackzip -u -v -D -p rockyou.txt flag.zip`
    * 找到的 pw = `not2secure`
    * 輸入後拿到 flag.txt
    * flag : `cyctf{y0u_cr@ck3d_th3_z!p...}`
* supa secure
    > 225
    > This time it’s a little tricker to crack the password: 19d14c463333a41a1538dbf9eb76aadf
    > You might also need this for something: cyctf
    > Are you up for the challenge?
    > hahabox0 解的
    * 這題一樣是 md5 
    * 用這個[網站](https://www.md5online.org/md5-decrypt.html)解的
    * flag : `cyctf{cyctfilovesalt}`
* Me, Myself, and I
    > 225
    > What even is this hash??? (Make sure to include flag wrapper)
    * 裡面是 sha512 hash
    * 直接上網找就可以了
    * flag : `cyctf{whoami}`

### Trivia
* Trivia 1
    > 100
    > Who created linux? {no wrapper}
    * flag : `Linus Torvalds`
* Trivia 2
    > 150
    > Who’s operating system was IBM going to buy before MS-DOS? {no wrapper needed}
    * flag : `Gary Kildall`
* Trivia 3
    > 100
    > Which company invented the original hadoop software?{no wrapper needed}
    * flag : `Yahoo`
* Trivia 4
    > 50
    > Microsoft has been threatened by a secret hacker for the last couple of years. This hacker has been infiltrating their network and exposing secret information about them to the world. Microsoft is determined to catch this hacker. They set up a computer with vulnerabilities and attempt to lure this hacker into trying to hack this computer in order to reveal his origins. What is this type of system called?{no wrapper needed}
    * flag : `honeypot`
* Trivia 5
    > 50
    > What is a social engineering attack in which someone watches someone else enter private information such as a password called?{no wrapper needed}
    * flag : `shoulder surfing`
* Trivia 6
    > 100
    > A Hacker infiltrated one of Microsoft's servers and set up malware inside. The malware laid dormant for months, being unnoticed by the server admins. On Thanksgiving Day, the malware was activated, and it crashed all of the servers and the entire network. What is this type of malware called?{no wrapper needed}
* Trivia 7
    > 50
    > What built-in Windows tool can you use to repair corrupted files?{no wrapper needed}
    * flag : `SFC`
* Trivia 8
    > 50
    > What programming language has this logo:{no wrapper needed}
    * flag : `haskell`

### Welcome
* Welcome
    > 10
    > Join our discord! Use Carl-bot's flag command to capture this flag!
    * 進到 discord 的 bot command channal 然後輸入 ?flag 拿到 flag 
    * flag : `CYCTF{W3lc0m3_t0_Cyb3rY0ddh@_CTF_2020!}`

### 特別感謝 hahabox0 的幫助
