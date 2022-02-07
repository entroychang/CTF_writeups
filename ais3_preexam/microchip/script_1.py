# def generate_key(id):
#     keys = list()                                                               
#     temp = id                                                                   
#     for _ in range(4):                                                         
#         keys.append(temp % 96)                                                  
#         temp = int(temp / 96)
#     keys.reverse()
#     return keys

# name = open("output.txt", "r").read().strip()

# for i in range(96*96*96*96):                                                 
#     keys = generate_key(i)
#     padded = name                                                 

#     result = ""                                                                 
#     for i in range(0, len(padded), 4):                                         

#         nums = list()                                                           
#         for j in range(4):                                                    
#             num = ord(padded[i + j]) - 32                                       
#             num = ((num - keys[j]) + 96) % 96                                          
#             nums.append(num + 32)                                               

#         result += chr(nums[3])                                                 
#         result += chr(nums[2])                                                 
#         result += chr(nums[1])                                                 
#         result += chr(nums[0])                                             

#     if 'AIS3{' in result:
#         print(result)

data = ['40B', '20g', '30i', '51J', '606', '01\\', '30w', '401', '30A', '41j', '40\\', '411', '30g', '70u', '30i', '10k', '30l', '407', '60x', '50i', '50X', '10K',
        '10I', '40h', '50X', '00K', '41i', '51l', '706', '70f', '40o', '106', '505', '70K', '11n', '518', '707', '41B', '50-', '118', '40w', '31a', '10r', '41z', '70K']
fake = "AlS3{BasE64_i5+b0rNIng~\\Qwo/-xH8WzCj7vFD2eyVktqOL1GhKYufmZdJpX9}"
flag = ""
for d in data:
    num = 0
    num += int(d[0]) << 6
    num += int(d[1]) << 9
    num += fake.index(d[2])
    flag += "{0:010b}".format(num)

for i in range(0, len(flag), 8):
    print(chr(int(flag[i:i+8], 2)), end='')

print()