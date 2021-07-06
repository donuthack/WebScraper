import json
import re

with open('res.json', "r") as f:
    res = f.read()
print(4, res)

string = re.sub(re.compile('new Date(.*?)'), "", res).replace('(', '').replace(")", '')
print(55, type(string))
struct = json.loads(string)
print(666, type(struct))
