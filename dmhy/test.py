import requests

# p = {
#     'http': 'http://%s' % ('127.0.0.1:1080'),
#     'https': 'http://%s' % ('127.0.0.1:1080'),
# }
p = {'http': 'http://36.74.102.133:8080', 'https': 'http://36.74.102.133:8080'}
# res = requests.get(url='https://share.dmhy.org')
res = requests.get(url='https://share.dmhy.org', proxies=p)
print(res.text)