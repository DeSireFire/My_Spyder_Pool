from aixinxi.axx import *
# 默认cookie头部
default_h = {
    'User-Agent': 'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52',
    'cookie': 'PHPSESSID=ns4e93j1oppq5qkn51dl5dko62',
    'referer': 'https://tu.aixinxi.net/views/pages.php?id=explore',
    'upgrade-insecure-requests': '1'
}
if not logining(default_h):
    default_h = login()



def strUper(tempStr,header=default_h,logout = False,fileName = fileNameIter()):
    '''
    传入字符串，上传爱信息图床工具
    :param headrs: 头部，包含默认值
    :param fileName: 字符串，不含有
    :param tempStr: 需要上传的字符串
    :return:
    '''
    # 检查登陆状态

    files = {'file': bytes(tempStr, encoding = "utf8")}
    updata(header, 'o_%s.txt'%fileName, files)
    if logout:
        loginOutloginOut(header['cookie'])

if __name__ == '__main__':

    tempStr = '大河向东流哇'
    try:
        strUper(tempStr,default_h)
    except Exception as e:
        pass
        # print(e)
    finally:
        pass
        # loginOutloginOut(default_h['cookie'])