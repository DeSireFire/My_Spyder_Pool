import requests



url = 'https://tu.aixinxi.net/includes/delete_file.php'
# url = 'https://tu.aixinxi.net/views/fileJump.php?key=da8dfdcc0cc21eb523ce881f4f934461&ming=o_1cs10bedkn4d1l9q1o0f1e8if6ra.png'

req = requests.post(url=url,headers=H,data=data)
print(req.status_code)
print(req.text)
print(req.encoding)
print(req.reason)
print(req.content)
print(req.headers)