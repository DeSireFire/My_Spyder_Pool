import requests
from Spyder.aixinxi.aixinxi_config import *


# 登陆aixinxi
def login():
    """

    :return:登陆成功后返回cookie
    """
    header = get_header()
    req1 = requests.post(url=login_url, headers=header, data=login_dirt)
    # req = requests.post(url=login_url, headers=get_header())
    if req1.status_code == 200:
        header.update({'cookie':req1.headers['Set-Cookie'][:36],'referer':'https://tu.aixinxi.net/views/pages.php?id=explore','upgrade-insecure-requests':'1',})
        if logining(header):
            print('登陆成功！')
            return header
        else:
            print('登陆失败！')
            return False
    else:
        return False

# 检测当前cooke的登陆状态
def logining(header = logining_Header):
    """

    :param header: 字典，请求头
    :return: 布尔值
    """
    req = requests.post(url=index_url, headers=header)
    if '<a href="https://tu.aixinxi.net/views/login.php"><i class="fa fa-user" aria-hidden="true"></i> 登录/注册</a>' not in req.text:
        return True
    else:
        return False

# 读取文件列表
def userFiles(header):
    """

    :param header: 字典，请求头
    :return:
    """
    header['referer'] = 'https://tu.aixinxi.net/views/userFiles.php'
    page = 1
    filesList = []
    tempfilesList = ['fist']
    while tempfilesList != []:
        url = 'https://tu.aixinxi.net/views/userFiles.php?page=%s'%(page)
        req = requests.post(url=url, headers=header)
        if '共有 0 条记录' in req.text:
            print('没有文件记录！')
            tempfilesList = []
            filesList += tempfilesList
        else:
            print(req.text)
    print(filesList)

# 上传文件


# 退出aixinxi
def loginOutloginOut(outcookie):
    """

    :param outcookie: 传入已经登陆了的cookie值
    :return:
    """
    loginOut_Header['cookie'] = outcookie
    req = requests.post(url=loginOut_url, headers=loginOut_Header, data=loginOut_dirt)
    if req.status_code == 200:
        print('退出成功！')
        return True
    else:
        return False
    # print(req.status_code)
    # print(req.text)
    # print(req.encoding)
    # print(req.reason)
    # print(req.headers)

def main():
    # ok = login()
    # if ok:
    #     print(ok)
    # else:
    #     print('No')
    # userFiles({'User-Agent': 'Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5',
    #            'cookie': 'PHPSESSID=lbse9bru4au0dmurarpgboshh4',
    #            'referer': 'https://tu.aixinxi.net/views/pages.php?id=explore', 'upgrade-insecure-requests': '1'})
    loginOutloginOut('PHPSESSID=lbse9bru4au0dmurarpgboshh4')
if __name__ == '__main__':
    main()