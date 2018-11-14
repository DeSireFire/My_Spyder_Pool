import requests

# url = 'http://httpbin.org/post'
url = 'http://tu-t1.oss-cn-hangzhou.aliyuncs.com'
H = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0',
    'Origin':'https://tu.aixinxi.net',
}

update_data = {
'name':'o_1cs10bedkn4d1l9q1o0f1e8if6rc.jpg',
'policy':'eyJleHBpcmF0aW9uIjoiMjAxOC0xMS0xM1QxMzo1NToyOVoiLCJjb25kaXRpb25zIjpbWyJjb250ZW50LWxlbmd0aC1yYW5nZSIsMCwxMDQ4NTc2MF0sWyJzdGFydHMtd2l0aCIsIiRrZXkiLCIiXV19',
'signature':'s0jhm0FbtgFMW4nJluLGgO2nhnI=',
'OSSAccessKeyId':'LTAIyUoGoXRUSdwm',
'key':'o_1cs10bedkn4d1l9q1o0f1e8if6rc.jpg',
'success_action_status':'200',
}
f = open('1.jpg', 'rb')
files = {'file': f}
req = requests.post(url=url,headers=H,data=update_data,files=files)
f.close()
print(req.status_code)
print(req.text)
# print(req.encoding)
# print(req.reason)
print(req.content)
print(req.headers)
