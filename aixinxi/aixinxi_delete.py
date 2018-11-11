import requests

H = {
# 'cookie':'PHPSESSID=gb9b12bgkn4a8gv1mf2ur50ud3',
'cookie':'PHPSESSID=vds8c7sspjq06277gnmid6ck45',
'origin':'https://tu.aixinxi.net',
'referer':'https://tu.aixinxi.net/views/pic.php?key=51641ef3e5beadcd1971574833e1aada',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
}
data = {
'key':'o_1cs0thrva5qg1el416in143p7vua.png',
}
url = 'https://tu.aixinxi.net/includes/delete_file.php'
# url = 'https://tu.aixinxi.net/views/fileJump.php?key=da8dfdcc0cc21eb523ce881f4f934461&ming=o_1cs10bedkn4d1l9q1o0f1e8if6ra.png'

r = requests.post(url=url,headers=H,data=data)
print(r.text)