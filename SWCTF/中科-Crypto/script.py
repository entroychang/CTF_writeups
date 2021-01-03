f = open('./code.txt')
codes = f.readlines()
count = 0

for code in codes:
    for i in code.replace('\n', ''):
        if i == '1':
            print('.', end='')
        else:
            print('-', end='')
        count += 1
        if count == 4:
            print(' ', end='')
            count = 0

print()