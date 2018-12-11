import requests,re,json,hashlib
from Spyder.aixinxi.aixinxi_config import *


# 登陆aixinxi
def login():
    """

    :return:登陆成功后返回cookie
    """
    header = get_header()
    req1 = requests.post(url=login_url, headers=header, data=login_dirt, proxies=proxy_list())
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
def logining(header):
    """

    :param header: 字典，请求头
    :return: 布尔值
    """
    req = requests.post(url=index_url, headers=header, proxies=proxy_list())
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
    temp_data = token_get(header)
    if temp_data:
        update_data['policy'] =  temp_data['policy']
        update_data['signature'] =  temp_data['signature']
        update_data['AccessKeyId'] =  temp_data['AccessKeyId']
        update_data['name'] =  fileName
        update_data['key'] =  fileName
    else:
        print("token获取失败")
        return False
    req = requests.post(url=update_url, headers=header, data=update_data, files=filesRead)
    if req.status_code == 200:
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
    return req.text.split(',')[:2]

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
    req = requests.post(url=delete_url, headers=header, data=data_delete, proxies=proxy_list())
    if 'ok' in req.text:
        print('OK')
        print(req.status_code)
        print(req.text)
        print(req.headers)
        return True
    else:
        print(req.status_code)
        print(req.text)
        print(req.headers)
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

# token密钥获取
def token_get(header):
    """
    {'policy': 'xx', 'signature': 'xx', 'AccessKeyId': 'xx'}/False
    :param header: 请求头部
    :return: 成功，传回字典；失败传回False
    """
    header.update(token_header)
    del header['upgrade-insecure-requests']
    req = requests.get(url=token_url, headers=header)
    if req.status_code == 200:
        return json.loads(req.text)
    else:
        print('token请求失败！')
        return False

# 文件名生成器
def fileNameIter():
    hash_md5 = hashlib.md5(fileName_data)
    return hash_md5.hexdigest()

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

def proxy_list(url = PROXYURL,testURL = testURL):
    """
    获取并检测代理池返回的IP
    :param url: 获取IP的代理池地址
    :param testURL: 检测网址
    :return: 一个能用的ip组成的proxies字典
    """
    count = 0 # 获取的IP数
    try:
        r = requests.get(url)
        count = len(json.loads(r.text))
        while count != 0:
            r = requests.get(url)
            ip_ports = json.loads(r.text)
            count = len(ip_ports)
            for i in range(0,4):
                ip = ip_ports[i][0]
                port = ip_ports[i][1]
                proxies = {
                    'http': 'http://%s:%s' % (ip, port),
                    'https': 'https://%s:%s' % (ip, port)
                }
                r = requests.get(testURL, proxies=proxies,timeout=TIMEOUT)
                if (not r.ok) or len(r.content) < 500:
                    r = requests.get(delproxyIP%(ip,port))
                else:
                    return proxies

    except Exception as e:
        # print(e)
        return None

def main():
    # ok = login()
    # if ok:
    #     print(ok)
    # else:
    #     print('No')
    header_test = {'User-Agent': 'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)',
               'cookie': 'PHPSESSID=8snmttr07uetioomcjpjslge57',
               'referer': 'https://tu.aixinxi.net/views/pages.php?id=explore',
               'upgrade-insecure-requests': '1'}
    # with open('1.jpg', 'rb') as f:
    #     files = {'file': f}
    # a = logining(header=ok)
    # print(a)
    # fl = userFiles(header_test)
    # print(fl)
    # delete(header_test,'44764c752081126b509b12091356f56c')
    # filesFind({'User-Agent': 'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)',
    # f = open('1.jpg', 'rb')
    # files = {'file':f}
    updata(header_test,'o_1cq3oq991g0q1lt3121t04dada.jpg',files)
    # f.close()
    # save(header_test,'o_1chq3v5e43um1bocaru1iqn7b8c.gif')
    # delete(header_test, '0bf0577871ccd5d890b9b7ccfc243ec0')
    # token_get(header_test)
    # loginOutloginOut('PHPSESSID=29botdjah0n9seekpdm2n9d0o5')
    # print(fileNameIter())
if __name__ == '__main__':
    main()