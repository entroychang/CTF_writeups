def gen_keys(id: int):
    keys = list()
    temp = id
    for i in range(4):
        keys.append(temp % 96)
        temp = int(temp / 96)
    return keys


encode = open("output.txt", "r").read().strip()

encode_list = []
count = 0
tmp = []
for c in encode:
    count += 1
    tmp.append(ord(c)-32)
    if count % 4 == 0:
        tmp.reverse()
        encode_list.append(tmp)
        tmp = []

for i in range(96*96*96*96):
    keys = gen_keys(i)
    count = 0
    ans = ""
    for encode_block in encode_list:
        for encode_char in encode_block:
            ans += chr(((96+encode_char - keys[count % 4]) % 96)+32)
            count += 1
#if 'AIS3{' in ans:
    print(ans)
