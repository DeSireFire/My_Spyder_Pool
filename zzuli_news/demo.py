# import requests,re
#
# def htmlClear(tempStr):
#     return re.sub(r'</?\w+[^>]*>', '', tempStr).replace(' ','').replace('\n','')
#
# req = requests.get(url='https://www.zzuliacgn.com/')
# pattern1 = re.compile('<span><b>(.*?)</b></span>',re.S)
# pattern2 = re.compile('<div class="review">([\s\S]*?)</div>',re.S)
# info = {}
# for m,n in zip(re.findall(pattern1,req.text),re.findall(pattern2,req.text)):
#     info[m] = htmlClear(n)
#     print('部门 : %s'%m)
#     print('简介 : %s'%info[m])


def 一条大咸鱼(tempStr):
    print('你在想屁吃！')
    print(tempStr)

def 一条大狗屎(tempStr):
    print('你不要过来啊！')
    print(tempStr)

def 一个铃果(tempStr):
    print('你再过来，我叫啦！')
    print(tempStr)

if __name__ == '__main__':
    # 一条大咸鱼('喵喵喵')
    # 一条大狗屎('喵喵喵')
    # 一个铃果('喵喵喵')
    狗屎 = 1
    两条狗屎 = 狗屎*2
    print(两条狗屎)