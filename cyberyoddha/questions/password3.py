import base64

def checkPassword(password):
#  if(len(password) != 40):
#    return False
  newPass = list(password)
  for i in range(0,40):
    newPass[i] = chr(ord(newPass[i]) ^ 0x55)
  finalPass = "".join(newPass)
  passBytes = finalPass.encode("ascii")
  base64_bytes = base64.b64encode(passBytes) 
  base64_string = base64_bytes.decode("ascii")
  print(base64_string)
  return base64_string == "FgwWARMuF2UhPQotZScKFTsxCjcVJmYKY2FqCiE9FSEmCjJlMTksKA=="

password = input("Enter password: ")
if(checkPassword(password)):
  print("PASSWORD ACCEPTED\n")
else:
  print("PASSWORD DENIED\n")
