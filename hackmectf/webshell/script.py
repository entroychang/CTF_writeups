import hashlib
import string

m = hashlib.sha512()
char = string.ascii_letters + string.punctuation
ip_address = '211.75.8.130'

for i in char:
    for j in char:
        cmd = hashlib.new("sha512", ip_address.encode("utf8")).hexdigest() ^ (i + j)
        print(cmd)
        if cmd == 'ls':
            print(i + j)
            break