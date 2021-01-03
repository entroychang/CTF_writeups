f = open('password.txt')

for line in f.readlines():
    for i in line.replace('\n', '').split():
        print(i)