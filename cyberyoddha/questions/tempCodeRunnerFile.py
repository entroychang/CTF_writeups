for i in list(sympy.primerange(0, 999999999)):
    if int(decoded) % i == 0:
        print('p and q =', i, int(decoded) / i)
        conn.sendline(str(i))
        conn.sendline(str(int(decoded) / i))
        break