import urllib.request
import inspect
# 打印出该函数的所有参数值和默认值
print(inspect.getfullargspec(urllib.request.urlopen))
'''
由此可知，urllib.request.urlopen(url, data=None, [timeout,]*,cafile=None,capath=None,cadefault=False,context=None)
url:链接地址
data:附加数据
timeout:超时时间
cafile：CA证书文件名
capath：CA证书文件的路径
cadefault=False：已经废弃的参数，默认值是False
context:指定是SSL设置，必须为ssl.SSLContext类型
'''
