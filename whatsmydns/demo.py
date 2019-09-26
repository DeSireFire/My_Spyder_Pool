import requests,re
import json,os

def test():
    for i in range(0,10):
        URL = "https://www.whatsmydns.net/"
        headers={"accept-encoding":'gzip'}
        req = requests.get(URL, headers=headers)
        pattern = re.compile('<input type="hidden" name="_token" id="_token" value="(.*?)" />',re.S)
        titles = re.findall(pattern,req.text)
        print("%s:%s"%(i,titles))

if __name__ == '__main__':
    test()