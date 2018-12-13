import requests
import chardet
URL = 'https://baike.baidu.com/item/%E5%96%80%E7%BA%B3%E6%96%AF%E6%B9%96'

_header = {
    'Host':'baike.baidu.com',
    'Referer':'http://baike.baidu.com/dili',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
}

def BTchecker(URL,_header):
    _respone = requests.post(url=URL,headers=_header)
    _respone.encoding = chardet.detect(_respone.content)['encoding']

    print(_respone.text)

if __name__ == '__main__':
    BTchecker(URL,_header)