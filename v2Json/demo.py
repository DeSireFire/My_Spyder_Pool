import json
v2File = open('config.json','r')
v2Json = json.loads(v2File.read())
print(type(v2Json))
for i in v2Json:
    print(i,v2Json[i])

for i in v2Json['inbounds']:
    print(i)