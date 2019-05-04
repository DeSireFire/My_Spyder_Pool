import requests,base64,re
from fontTools.ttLib import TTFont
myheader = {
'Origin':'https://www.qvdv.com',
'Referer':'https://www.qvdv.com/tools/qvdv-img2base64.html',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
}
req = requests.get(url="https://book.qidian.com/info/1010734492",headers= myheader)

pattern = re.compile("https://qidian.gtimg.com/qd_anti_spider/([\s\S]*?).ttf'")
ttf = re.findall(pattern,req.content.decode(encoding="utf-8"))
pattern = re.compile('<span class="%s">([\s\S]*?)</span>'%ttf[0].split('/')[-1])
numInfos = re.findall(pattern,req.content.decode(encoding="utf-8"))
print(numInfos) # ['&#100422;&#100421;&#100419;&#100420;&#100415;&#100421;', '&#100424;&#100425;&#100424;&#100417;&#100420;&#100419;&#100422;', '&#100419;&#100415;&#100420;&#100415;&#100423;', '&#100423;&#100424;&#100425;&#100423;&#100420;&#100426;&#100419;', '&#100423;&#100425;&#100420;&#100425;&#100417;']
print([268.36,7975.02,82.56,1790.97,19.85])
req2 = requests.get(url='https://qidian.gtimg.com/qd_anti_spider/%s.ttf'%ttf[0].split('/')[-1])
req3 = requests.get(url='https://qidian.gtimg.com/qd_anti_spider/%s.woff'%ttf[0].split('/')[-1])
with open("%s.ttf"%ttf[0].split('/')[-1], "wb") as code:
    code.write(req2.content)
with open("%s.woff"%ttf[0].split('/')[-1], "wb") as code:
    code.write(req3.content)

font1=TTFont("%s.ttf"%ttf[0].split('/')[-1])
font1.saveXML("%s.xml"%ttf[0].split('/')[-1])

font2=TTFont("%s.woff"%ttf[0].split('/')[-1])
font2.saveXML("%s[2].xml"%ttf[0].split('/')[-1])

obj_list1=font1.getGlyphNames()  #获取所有字符的对象，去除第一个和最后一个
obj_list1.remove('.notdef')
obj_list1.remove('period')
# ['.notdef', 'eight', 'five', 'four', 'nine', 'one', 'period', 'seven', 'six', 'three', 'two', 'zero']
print(obj_list1)
uni_list1=font1.getGlyphOrder()    #获取所有编码，去除前2个
print(uni_list1[2:])
numberDict = {
    'zero':0,
    'one':1,
    'two':2,
    'three':3,
    'four':4,
    'five':5,
    'six':6,
    'seven':7,
    'eight':8,
    'nine':9,
}
