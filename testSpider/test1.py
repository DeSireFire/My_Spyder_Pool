import requests
import re
from urllib import parse

def SearchNovel(k):
    url='http://www.biqudu.com/searchbook.php?keyword={}'.format(parse.quote(k))
    temp = requests.get(url,verify=False)
    print(temp.text)

if __name__ == '__main__':
    pass