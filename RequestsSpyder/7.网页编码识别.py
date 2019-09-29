import requests

# 方法一
url = 'http://www.langzi.fun'
r = requests.get(url)
encoding = requests.utils.get_encodings_from_content(r.text)[0]
res = r.content.decode(encoding,'replace')
print(res)

# 方法二
# 其实requests里面用的就是chardet
import chardet
r = requests.get(url=url)

# 获取网页编码格式，并修改为request.text的解码类型
r.encoding = chardet.detect(r.content)['encoding']
if r.encoding == "GB2312":
    r.encoding = "GBK"
