'''
data参数是可选的
未使用时，通常是get请求，即普通的URL传参，可以直接在网址上看见这些参数
如果使用了data,那就是post请求，URL上看不见，是加密的。
另外，如果data附加数据需要传的是字节流编码（bytes类型）则需要通过bytes()方法转化
'''

import urllib.request
import urllib.parse
# urlencode()方法可将参数字典转化为字符串
data = bytes(urllib.parse.urlencode({"key":"value"}),encoding='utf-8')
response = urllib.request.urlopen("http://httpbin.org/post",data=data)
print(response.read().decode("utf-8"))

'''
由此可知，附加数据data是在请求的from字段中
'''