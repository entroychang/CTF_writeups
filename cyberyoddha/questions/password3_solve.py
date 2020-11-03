import base64

base64_string = "FgwWARMuF2UhPQotZScKFTsxCjcVJmYKY2FqCiE9FSEmCjJlMTksKA=="
base64_bytes = base64.b64decode(base64_string)
newPass = list(base64_bytes.decode("ascii"))
for i in range(0,40):
    newPass[i] = chr(ord(newPass[i]) ^ 0x55)

print(''.join(newPass))