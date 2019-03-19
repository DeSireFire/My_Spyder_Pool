import requests,chardet,re
# texturl = ['http://dl.wenku8.com/packtxt.php?aid=1&vid=%s&charset=utf-8'%n for n in range(100,200)]
texturl = ['http://dl.wkcdn.com/txtutf8/0/%s.txt'%n for n in range(1,999)]
# http://dl.wenku8.com/packtxt.php?aid=1&vid=1&charset=utf-8
w8LoginHeader = {
'origin':'https://www.wenku8.net',
'referer':'https://www.wenku8.net/login.php?jumpurl=http%3A%2F%2Fwww.wenku8.net%2Findex.php',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
}

def HtmlDownLoader(url,**kwargs):
    resRespone = requests.get(url=url,**kwargs)
    resRespone.encoding = chardet.detect(resRespone.content)['encoding']
    if resRespone.encoding == "GB2312":
        resRespone.encoding = "GBK"
    return resRespone.text[34:-76]

def main():
    for i in texturl:
        fulltext1 = HtmlDownLoader(i)
        fulltext2 = HtmlDownLoader(texturl[texturl.index(i)+1])
        text = fulltext1[:-len(fulltext2)]
        with open('%s.txt' % (i[39:-14]), 'a',encoding='utf-8') as f:
            f.write(text)

if __name__ == '__main__':
    main()