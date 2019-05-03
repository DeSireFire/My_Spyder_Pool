import requests,base64
myheader = {
'Origin':'https://www.qvdv.com',
'Referer':'https://www.qvdv.com/tools/qvdv-img2base64.html',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
}
req = requests.get(url="https://bookcover.yuewen.com/qdbimg/349573/1010734492/180",headers= myheader)
base64_data = base64.b64encode(req.content)
print('data:image/jpg;base64,/'+bytes.decode(base64_data))
# with open("1010734492.jpg", "wb") as code:
#     code.write(req.content)