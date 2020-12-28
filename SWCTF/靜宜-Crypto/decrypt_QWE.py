import argparse
str1="QWERTYUIOPASDFGHJKLZXCVBNM"
str2="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
parser=argparse.ArgumentParser()
parser.add_argument('mode',help='encipherment/decipherment')
args=parser.parse_args()
str3=''
if args.mode=='e':
    en_str=input('Please input encrypted string:')
    for s in en_str:
        str3=str3+str1[str2.index(s.upper())]
elif args.mode=='d':
    de_str=input('Please input decryption string:')
    for s in de_str:
        if s not in str2:
            str3 += s
            continue
        str3=str3+str2[str1.index(s.upper())]
print('result:%s'%str3)