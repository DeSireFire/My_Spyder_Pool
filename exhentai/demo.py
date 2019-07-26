import requests,re
from lxml import etree
exURL = 'https://exhentai.org/?f_cats=881&f_search=female:%22human+pet%24%22&f_sname=on&f_stags=on&f_sr=on&f_srdd=5&advsearch=1'

def getHeads(cookies):
    return {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,ja;q=0.6',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': cookies,
        'Host': 'exhentai.org',
        'Referer': 'https://exhentai.org',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
cookieTemp = 'ipb_member_id=715432; ipb_pass_hash=e05c94c921a9ed3aa93f7937553febc5; igneous=3472f6fa9; sk=6gyz6cmjzamaftpgbfwvcnzpdgpq'
req = requests.get(exURL,headers=getHeads(cookieTemp))
pattern = re.compile('<div class="gl1t"><a href="(.*?)">',re.S)
titles = re.findall(pattern,req.text)

print(titles)

for i in titles[:2]:
    req = requests.get(i, headers=getHeads(cookieTemp))
    html = etree.parse(req.text,etree.HTMLParser())
    # res = html.xpath("//div[@class='gdtm']/div/a/@href")
    # print(res)