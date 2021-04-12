str = r"~!@#$%^&*()_+<>?,.;:-[]{}\/"

for i in range(0, len(str)):
    for j in range(0, len(str)):
        a = ord(str[i])^ord(str[j])
        if chr(a) in 'ls':
            print("'" + str[i] + "'^'" + str[j] + "' is " + chr(a))
