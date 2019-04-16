import requests,chardet
# url = 'http://dl.wkcdn.com/txtgbk/0/1.txt'
urls = ['https://www.wenku8.net/book/%s.htm' % n for n in range(1,2550)]
# url = 'http://dl.wenku8.com/down.php?type=utf8&id=1'
# url = 'http://t1.aixinxi.net/o_233qwe6667788.txt'
print(len(urls))
for i in urls:
    print(i)
    resRespone = requests.get(url=i)
    resRespone.encoding = chardet.detect(resRespone.content)['encoding']
    if resRespone.encoding == "GB2312":
        resRespone.encoding = "GBK"
    # print(resRespone.text)
    if '版权问题' in resRespone.text:
    # 输出成文本
        print('发现版小说，%s'%i)
        with open('版权小说统计.txt', 'a+', encoding='utf-8') as f:
            f.write(i+"\n")
    if '不存在' in resRespone.text:
    # 输出成文本
        print('发现错误ID，%s'%i)
        with open('错误id.txt', 'a+', encoding='utf-8') as f:
            f.write(i+"\n")