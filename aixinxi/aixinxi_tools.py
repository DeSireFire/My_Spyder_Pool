import requests,re
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
    :return: 列表，所有图片文件名和key,例如：[('6472a56c546d31de83a11a15ebcf57bd', 'o_1cq3oq991g0q1lt3121t04boka.jpg'),]
    """
    header['referer'] = 'https://tu.aixinxi.net/views/userFiles.php'
    page = 1
    imgdata = []
    while page != 0:
        url = 'https://tu.aixinxi.net/views/userFiles.php?page=%s' % (page)
        req = requests.post(url=url, headers=header)
        pattern = re.compile(r'<td><a style="color:#000" target="_blank" href="https://tu.aixinxi.net/views/fileJump.php\?key=(.*?)&ming=(.*?)">管理</a>', re.S)
        tempfilesList = re.findall(pattern, req.text)
        if tempfilesList:
            imgdata += tempfilesList
            page += 1
        else:
            page = 0
    return imgdata

# 上传并保存文件
def updata(header,fileName,filesRead):
    """

    :param header: 请求头部
    :param filesRead: 已经读取过的文件数据，例如：filesRead = {'file': open('1.jpg', 'rb')}
    :param filesRead: 字符串，带后缀的文件名，例如：xxx.png
    :return: 布尔值
    """
    if 'referer' in header:
        del header['referer']
        header.update(update_header)
    else:
        header.update(update_header)
    update_data['name'] =  fileName
    update_data['key'] =  fileName
    req = requests.post(url=update_url, headers=header, data=update_data, files=filesRead)
    if req.status_code == '200':
        print('上传成功！')
        info = save(header,fileName)
        if info:
            print('保存成功！')
            print(info)
            return info
        else:
            print('保存失败！')
            return False
    else:
        print("上传失败！")
        print(req.text)
        print(req.headers)
        return False

# 保存文件
def save(header,fileName):
    """
    da2293e8d43a8decf0136c6ee44c0f20,jpg,
    {'Server': 'Tengine', 'Date': 'Mon, 12 Nov 2018 12:18:32 GMT', 'Content-Type': 'text/html; charset=UTF-8', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'Vary': 'Accept-Encoding', 'X-Powered-By': 'PHP/5.6.30', 'Expires': 'Thu, 19 Nov 1981 08:52:00 GMT', 'Cache-Control': 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0', 'Pragma': 'no-cache', 'Content-Encoding': 'gzip'}
    ['04d1cff3e980155df7538088166d0446,png,']
    {'Server': 'Tengine', 'Date': 'Mon, 12 Nov 2018 12:24:09 GMT', 'Content-Type': 'text/html; charset=UTF-8', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'Vary': 'Accept-Encoding', 'X-Powered-By': 'PHP/5.6.30', 'Expires': 'Thu, 19 Nov 1981 08:52:00 GMT', 'Cache-Control': 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0', 'Pragma': 'no-cache', 'Content-Encoding': 'gzip'}

    :param header: 请求头
    :param fileName: 文件名
    :return:列表，例如：[da2293e8d43a8decf0136c6ee44c0f20,jpg,]
    """
    header.update(save_header)
    data_save['ming'] = fileName
    req = requests.post(url=save_url, headers=header, data=data_save)
    print(req.text.split(','))
    print(req.headers)
    return req.text.split(',')

# 删除图片
def delete(header,key):
    """
    {'User-Agent': 'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)', 'cookie': 'PHPSESSID=gb9b12bgkn4a8gv1mf2ur50ud3', 'referer': 'https://tu.aixinxi.net/views/pic.php?key=da2293e8d43a8decf0136c6ee44c0f20', 'upgrade-insecure-requests': '1', 'origin': 'https://tu.aixinxi.net'}
    ok.删除成功
    {'Server': 'Tengine', 'Date': 'Mon, 12 Nov 2018 12:38:01 GMT', 'Content-Type': 'text/html; charset=UTF-8', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'Vary': 'Accept-Encoding', 'X-Powered-By': 'PHP/5.6.30', 'Content-Encoding': 'gzip'}
    :param header: 请求头部
    :param key: 图片的key
    :return:布尔值
    """
    header.update(delete_header)
    header['referer'] += key
    data_delete['key'] = key
    req = requests.post(url=delete_url, headers=header, data=data_delete)
    if 'ok' in req.text:
        print(req.text)
        return True
    else:
        print(req.text)
        return False

# 查找图片信息
def filesFind(header,fileName):
    """

    :param header: 请求头
    :param fileName: 需要查询的文件名
    :return: 列表，[key,fileName] 例如：['1b655e2a822747c3c78af0859ca1b63c', 'o_1cq3gdm9jqcm11g87jv1ghiqaea.jpg']
    """
    fileslist = userFiles(header)
    for t in fileslist:
        if fileName in t:
            fileslist = list(t)
            print(fileslist)
            return fileslist



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
    header_test = {'User-Agent': 'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)',
               'cookie': 'PHPSESSID=gb9b12bgkn4a8gv1mf2ur50ud3',
               'referer': 'https://tu.aixinxi.net/views/pages.php?id=explore',
               'upgrade-insecure-requests': '1'}
    # with open('1.jpg', 'rb') as f:
    #     files = {'file': f}
    f = open('1.jpg', 'rb')
    files = {'file':f}
    # userFiles({'User-Agent': 'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)',
    # save({'User-Agent': 'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)',
    # delete({'User-Agent': 'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)',
    # filesFind({'User-Agent': 'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)',
    updata(header_test,'o_1cq3gdm9jqcm11g87jv1ghiqaez.jpg',files)
    f.close()

    # loginOutloginOut('PHPSESSID=29botdjah0n9seekpdm2n9d0o5')
if __name__ == '__main__':
    main()