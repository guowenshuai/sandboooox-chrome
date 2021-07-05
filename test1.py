import re

EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")
email = "simon9999.aaa@gmail.com--1"
if not EMAIL_REGEX.match(email):
  # whatever
  print("not googd")

hash = {"aa":1,"bb":2}
print(list(hash.values()))


print(list(map(lambda x: 2, range(20) )))

import json, requests
daemonurl = "http://172.18.6.106:1234/rpc/v0"


def lotus(method, params=None):
    if params is None:
        params = []
    payload = {
        "jsonrpc": "2.0",
        "method": "Filecoin.%s" % method,
        "id": 1,
        "params": params
    }
    headers = {'Content-Type': 'application/json'}
    payload = json.dumps(payload)
    response = requests.request("POST", daemonurl, headers=headers, data=payload)
    return json.loads(response.content)

print(lotus("StateMinerPower", ["f021255", [{'/': 'bafy2bzaceau27fjdl2lzfraln4chaqwe6fze2nk4lwkt56lucssx2ryowraow'}, {'/': 'bafy2bzacea4gldguitkbsszxnakr6y4qx3exxtv44g6pfgm4nhmitrjt22o4k'}, {'/':'bafy2bzacebd2ulu75rzntjmrbuobqmi3cc7q4ipteld3hlsbtiqya6tmpelki'}, {'/': 'bafy2bzacebyl7rv3s5hjm4cd4bcawnmswzekth5bchpkx4xxgbpqx3zhhylvo'}]])['result'])
