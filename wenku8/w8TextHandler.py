import requests,chardet,re
# textURL = 'http://dl.wenku8.com/packtxt.php?aid=1628&vid=55154&charset=utf-8'
# textURL = 'http://dl.wenku8.com/packtxt.php?aid=2478&vid=92903&charset=utf-8'
textURL = 'http://dl.wenku8.com/down.php?type=utf8&id=1'
# textURL = ['http://dl.wenku8.com/packtxt.php?aid=1627&vid=%s&charset=utf-8' % n for n in range(10000,100000)]

w8LoginHeader = {
'origin':'https://www.wenku8.net',
'referer':'https://www.wenku8.net/login.php?jumpurl=http%3A%2F%2Fwww.wenku8.net%2Findex.php',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
}

w8LoginOutHeader = {
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
}


def HtmlDownLoader(url,**kwargs):
    resRespone = requests.get(url=url,**kwargs)
    resRespone.encoding = chardet.detect(resRespone.content)['encoding']
    if resRespone.encoding == "GB2312":
        resRespone.encoding = "GBK"
    return resRespone.text

# for i in textURL:
#     print(i)
#     if len(HtmlDownLoader(i))>150:
#         print(HtmlDownLoader(i))
#         print('查找到地址为:%s'%i)
#
# fulltext = list(set(HtmlDownLoader(textURL).split(' ')))
fulltext = HtmlDownLoader(textURL)
# print(fulltext)
print('开始正则匹配')
# re_pattern = '第一卷 渴望死亡的小丑 序章 取代自我介绍的回忆—前天才美少女作家([\s\S]*?)第一卷 渴望死亡的小丑 第一章 远子学姐是美食家([\s\S]*?)第一卷 渴望死亡的小丑 第二章 这个世界上最美味的故事'
re_pattern = '第([\s\S]*?)卷 ([\s\S]*?) ([\s\S]*?) ([\s\S]*?) ([\s\S]*?)第([\s\S]*?)卷'

pattern = re.compile(re_pattern)
splittext = pattern.findall(fulltext)
for i in splittext:
    print(i)

print(len(splittext))
'''
爬取思路:
第一步:
首先,请求(如:https://www.wenku8.net/book/1.htm)获取文章的:文库分类,小说作者,文章状态,最后更新,全文长度,内容简介等信息
特殊状况处理:
    文库分类,小说作者,文章状态,最后更新,全文长度可能获取不到的,若如此则全部赋值为'我不知道',来处理.
    '该文章不存在'存在时,关闭爬虫,并抛出url地址.
    在页面页面中如若'版权问题'(例如id:1627,2,1597,1592等)的小说,将小说名记录到单独的文本文件中.
第二步:
抓取小说目录的地址,发送第二次请求,获取 卷名 以及其所属的章节名,
向(例如:http://dl.wenku8.com/down.php?type=utf8&id=2254)发送第三次请求,获取简体U下载点1的地址,
并发送第四次请求,获得全文文本
第三步:
通过第二步获取的卷名 以及其所属的章节名,拼接成正则表达式,通过正则对全文本进行裁切

http://dl.wenku8.com/packtxt.php?aid=1&vid=1&charset=utf-8
'''

