import sys
import os
import string
if __name__ == '__main__':
    # dropping priv.
    os.setgroups([])
    os.setgid(1000)
    os.setuid(1000)
    os.umask(0o077)

    spell = sys.argv[1].strip()
    unlocked = sys.argv[2].strip()
    unlocked = unlocked.split(",") if len(unlocked) != 0 else []
    max_length = int(sys.argv[3])
    rebirthed = int(sys.argv[4])
    
    try:
        spell.encode('ascii')
    except UnicodeEncodeError:
        print("YOU SHALL NOT PASS!1")
        exit()

    if not rebirthed and len(spell) > max_length:
        print("YOU SHALL NOT PASS!2")
        exit()

    curses = list(string.ascii_lowercase+string.digits+"()'\".")
    blacklist = set(curses)
    print(unlocked)
    for i in unlocked:
        blacklist -= set(curses[int(i)])
    print(rebirthed)
    if rebirthed:
        blacklist -= set("'\".")
    print(blacklist)
    print(spell)
    for char in spell:
        if char in blacklist:
            print("YOU SHALL NOT PASS!3")
            exit()

    _eval = __builtins__.eval
    del __builtins__.exec
    del __builtins__.eval
    del __builtins__.__import__
    print("[+] Casting Magic... ", _eval(spell, {}))

# a0ffa2a9fd16f33581274bf2b88aa4b8