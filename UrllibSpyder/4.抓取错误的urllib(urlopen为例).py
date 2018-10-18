'''
凡是关于网络的事情，意外情况发生的可能性是非常大的
最常见的就是网络请求超时，如果发生了此类情况，爬虫总不能就此停止不工作了
这是就需要抓取错误，让爬虫就算报错了，也不能停止工作
这里使用timeout参数来故意模拟一下超时错误
'''
import urllib.request
import urllib.parse

import urllib.error
# 由于URLError异常属于urllib.error模块

import socket
# 在这里是用来判断异常的类型

try:
    response = urllib.request.urlopen("http://httpbin.org/get",timeout=0.1)
except urllib.error.URLError as ue:
    if isinstance(ue.reason,socket.timeout):
        print(ue.reason)
        print(socket.timeout)

'''
timeout的0.1秒内基本不可能得到服务器的响应，太快了，所以肯定会输出TIME OUT
'''