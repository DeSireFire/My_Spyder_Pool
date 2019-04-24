import requests
# 下载其他文件
# with open("Sublime_Build_203207.dmg", "wb") as code:
#     code.write(requests.get(url="https://download.sublimetext.com/Sublime%20Text%20Build%203207.dmg").content)

# 下载图片文件
req = requests.get(url="https://www.seselah.com/uploads/2a/2a71e0d8fdf1c870596b2be33c27dc18.jpg")
print(req.content)
with open("1.jpg", "wb") as code:
    code.write(req.content)
req = requests.get(url="http://t1.aixinxi.net/o_1d6l2rdi21910gk01o22187c1sqja.jpg")
print(req.content)
with open("2.jpg", "wb") as code:
    code.write(req.content)
req = requests.get(url="http://img.wkcdn.com/image/0/2/2s.jpg")
print(req.content)
with open("3.jpg", "wb") as code:
    code.write(req.content)
req = requests.get(url="http://t1.aixinxi.net/o_1cnu5m83210v1oi41ca4n56r6la.jpg")
print(req.content)
with open("4.jpg", "wb") as code:
    code.write(req.content)

req = requests.get(url="http://t1.aixinxi.net/o_1d96s8ha36po1o2dumm10me1t8ga.jpg-j.jpg")
print(req.content)
with open("5.jpg", "wb") as code:
    code.write(req.content)
