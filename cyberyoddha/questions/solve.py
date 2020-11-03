from pwn import *
import base64
import sympy
import time

# def decode_base64(data):
#     """Decode base64, padding being optional.

#     :param data: Base64 data as an ASCII byte string
#     :returns: The decoded byte string.

#     """
#     missing_padding = len(data) % 4
#     if missing_padding != 0:
#         data += b'='* (4 - missing_padding)
#     return base64.decodestring(data)

conn = remote('cyberyoddha.baycyber.net', 10006)
conn.recvuntil('Question #0')
conn.recvline()
encoded = conn.recvline().encode('utf-8').replace('\x1b[34mFirst question!  Quick, decrypt this: \x1b[0m', '').replace('\x1b[34m!\x1b[0m \n', '')
# encoded = str(encoded)
print('encode : ', encoded)
# missing_padding = 4 - len(encoded) % 4
# if missing_padding:
#     encoded += b'=' * missing_padding
decoded = base64.b64decode(encoded).replace('\n', '')
print(decoded)
conn.sendline(decoded)

conn.recvuntil('Question #1')
conn.recvline()
encoded = conn.recvline().encode('utf-8').replace('\x1b[34mSecond question!  Supa ez.  Is it possible for p to equal \x1b[0m', '').replace('\x1b[34m? [y/n]\x1b[0m \n', '')
print('encode : ', encoded)
decoded = base64.b64decode(encoded)
conn.sendline('n')
print(decoded)

time.sleep(1)
conn.recvline()
time.sleep(1)
conn.recvline()
conn.recvline()
encoded = conn.recvline().encode('utf-8').replace('\x1b[34mQuick give me the p and q (where p < q) values for when n is \x1b[0m', '').replace('\x1b[34m!\x1b[0m\n', '')
print('encode : ', encoded)
decoded = base64.b64decode(encoded)
print(decoded)
for i in list(sympy.primerange(0, 99999)):
    if int(decoded) % i == 0:
        print('p and q =', i, int(decoded) / i)
        conn.send(str(i) + ', ')
        conn.sendline(str(int(decoded) / i))
        print(conn.recvline())
        break
conn.interactive()