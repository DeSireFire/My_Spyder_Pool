import requests,chardet

url = 'https://tw.manhuagui.com/comic/24591/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
}
reps = requests.get(url,headers = headers)
reps.encoding = chardet.detect(reps.content)['encoding']
if reps.encoding == "GB2312":
    reps.encoding = "GBK"

print(reps.text)
print(reps.encoding)
