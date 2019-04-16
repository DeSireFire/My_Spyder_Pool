import requests,chardet
file_object = open('版权小说统计.txt','r')
urls = file_object.readlines()
file_object.close()
print(urls)
newlist = []
for i in urls:
    i = i.replace('\n','')
    url = 'http://dl.wkcdn.com/txtutf8/%s/%s.txt'%(int(int(i[28:-4])/1000),i[28:-4])
    print(url)
    resRespone = requests.get(url=url)
    resRespone.encoding = chardet.detect(resRespone.content)['encoding']
    if resRespone.encoding == "GB2312":
        resRespone.encoding = "GBK"
    if len(resRespone.text)>10000:
        print('%s 存在全文本'%i)
        with open('存在全本的版全小说.txt', 'a+', encoding='utf-8') as f:
            f.write(i+'\n')