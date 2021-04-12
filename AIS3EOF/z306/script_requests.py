# import requests
# from bs4 import BeautifulSoup

# url = 'http://eof01.zoolab.org:40000/'

# cipher = []
# result = ''

# for i in range(20):
#     cipher.append(''.join(BeautifulSoup(requests.get(url).text, 'html.parser').find('span').get_text().split()))

# for i in range(0, len(cipher[0])):
#     char_compared = cipher[0][i]
#     for j in cipher:
#         if char_compared != j[i]:
#             break
#     else:
#         result += char_compared

# print(result)

string = '!$A%^@A*&!**!L@@'

alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

with open('string.txt', 'w') as f:
    for i in alp:
        for j in alp:
            for k in alp:
                for l in alp:
                    for m in alp:
                        for n in alp:
                            for o in alp:
                                f.write(string.replace('@', i).replace('*', j).replace('!', k).replace('$', l).replace('%', m).replace('^', n).replace('&', o))

'''

+ -> F
A, S -> L
H, P, k, <, y -> A
7, 6, d, t -> G

FLAG{EDH58*H-LT&UZAOl}
FLAG{--A---A------L--}
FLAG{STAR-@A*-S**SL@@}
STAR-@A*-S**SL@@
!$A%-@A*-!**!L@@

'''