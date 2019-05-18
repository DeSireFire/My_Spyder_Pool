import requests,chardet

url = 'https://www.biquge.com.cn/book/23488/'

reps = requests.get(url)
reps.encoding = chardet.detect(reps.content)['encoding']
if reps.encoding == "GB2312":
    reps.encoding = "GBK"

print(reps.text)