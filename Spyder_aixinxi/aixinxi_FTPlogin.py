#ftp演示，首先要在本机或远程服务器开启ftp功能
import sys,os,ftplib,socket,hashlib,shutil
print("=====================FTP客户端=====================");
# print(ftp.cwd("test"))  # 设置FTP当前操作的路径
# print(ftp.cwd(".."))  # 设置FTP当前操作的路径(返回上级)
# print(ftp.mkd("pathname"))  # 新建远程目录print
# print(ftp.mkd("pathname2"))  # 新建远程目录
# print(ftp.pwd())  # 返回当前所在位置
# print(ftp.rmd("pathname2")) # 删除远程目录
# print(ftp.delete("test")) # 删除远程文件
# print(ftp.rename("pathname", "pathname3"))  # 将fromname修改名称为toname。
# print(ftp.cwd(".."))  # 设置FTP当前操作的路径
# print(ftp.pwd())  # 返回当前所在位置
# ftp.nlst()                        # 获取目录下的文件




# 连接登陆
def connect():
    try:
        ftp = ftplib.FTP(HOST)  # 实例化FTP对象
        ftp.login(username, password)  # 登录
        ftp.set_pasv(False)  # 如果被动模式由于某种原因失败，请尝试使用活动模式。
        print(ftp.getwelcome())
        print('已连接到： %s' % HOST)
        return ftp
    except (socket.error,socket.gaierror):
        print("FTP登陆失败，请检查主机号、用户名、密码是否正确")
        sys.exit(0)

# 获取当前路径
def pwdinfo(ftp):
    pwd_path = ftp.pwd()
    print("FTP当前路径:", pwd_path)

# 中断并退出
def disconnect(ftp):
    ftp.quit()  # FTP.close()：单方面的关闭掉连接。FTP.quit():发送QUIT命令给服务器并关闭掉连接

# 上传文件
def upload(ftp, filepath,file_name = None):
    f = open(filepath, "rb")
    if file_name == None:
        file_name = os.path.split(filepath)[-1]

    if find(ftp, file_name) or file_name == "无后缀格式的文件":
        print("%s 已存在或识别为无后缀格式的文件,上传终止"%file_name) # 上传本地文件,同名文件会替换
        return False
    else:
        try:
            ftp.storbinary('STOR %s'%file_name, f, buffer_size)
            print('成功上传文件： "%s"' %file_name)
        except ftplib.error_perm:
            return False
    return True

# 下载文件
def download(ftp, filename):
    f = open(filename,"wb").write
    try:
        ftp.retrbinary("RETR %s"%filename, f, buffer_size)
        print('成功下载文件： "%s"' % filename)
    except ftplib.error_perm:
        return False
    return True

# 获取目录下文件或文件夹详细信息 [file for file in r_files if file != "." and file !=".."]
def dirInfo(ftp):
    ftp.dir()

# 获取目录下文件或文件夹的列表信息，并清洗去除“. ..”
def nlstListInfo(ftp):
    files_list = ftp.nlst()
    return [file for file in files_list if file != "." and file !=".."]


# 查找是否存在指定文件或目录
def find(ftp,filename):
    ftp_f_list = ftp.nlst()  # 获取目录下文件、文件夹列表
    if filename in ftp_f_list:
        return True
    else:
        return False

# 检查是否有存在指定目录并创建
def mkdir(ftp,dirpath):
    if find(ftp, dirpath):
        print("%s目录已存在！自行跳转到该目录！"%dirpath)
        pwdinfo(ftp, dirpath) # 设置FTP当前操作的路径
    else:
        print("未发现%s同名文件夹！" % dirpath)
        try:
            ftp.mkd(dirpath)    # 新建远程目录
            print("创建新目录%s！并自行跳转到该目录！" % dirpath)
            pwdinfo(ftp, dirpath)    # 设置FTP当前操作的路径
        except ftplib.error_perm:
            print("目录已经存在或无法创建")

# 目录跳转
def pwdinfo(ftp,dirPathName):
    """
    跳转到指定目录
    :param ftp: 调用connect()方法的变量
    :param dirPathName: FTP服务器的绝对路径
    :return:
    """
    try:
        ftp.cwd(dirPathName)             # 重定向到指定路径
    except ftplib.error_perm:
        print('不可以进入目录："%s"' % dirPathName)
    print("当前所在位置:%s" % ftp.pwd())  # 返回当前所在位置

# 文件名加密
def fileNameMD5(filepath):
    """
    文件名加密MD5
    :param filepath: 本地需要加密的文件绝对路径
    :return: 返回加密后的文件名
    """
    file_name = os.path.split(filepath)[-1]     # 获取文件全名
    encryption = hashlib.md5()      # 实例化MD5
    try:
        file_format = os.path.splitext(file_name)[-1]  # 截取文件格式
        file_name_section = os.path.splitext(file_name)[0]
    except IndexError as e:
        print('%s 文件有误！未发现后缀格式！报错信息：%s' %(file_name,e))
        return "无后缀格式的文件"
    else:
        encryption.update(file_name_section.encode('utf-8'))
        newname = "zzuliacgn_" + encryption.hexdigest() + "." + file_format
        print('MD5加密前为 ：' + file_name)
        print('MD5加密后为 ：' + newname)
        return newname

# 删除目录下文件
def DeleteFile(ftp,filepath = "/233",file_name = None):
    pwdinfo(ftp,filepath)   # 跳转到操作目录
    if find(ftp,file_name) and file_name != None:
        ftp.delete(file_name)   # 删除文件
        print("%s 已删除！"%file_name)
    elif file_name == None:
        print("file_name:%s 将删除 %s 目录下所有文件（目录除外）！" % (file_name,ftp.pwd()))
        filelist = ftp.nlst()   # 列出当前目录下的文件和文件夹列表并去掉前两个元素
        # filelist = ftp.nlst()[2:]   # 列出当前目录下的文件和文件夹列表并去掉前两个元素
        print(filelist)
        for i in filelist:
            if os.path.isfile(i):
                ftp.delete(i)  # 删除文件
                print("%s 是文件，已删除！" % i)
            else:
                print("%s 是文件夹" % i)
    else:
        print("%s 未找到，删除中止！" % file_name)

# 删除目录下的文件夹
def DeleteDir(ftp,dirpath,dir_name = None):
    pwdinfo(ftp, dirpath)  # 跳转到操作目录
    if find(ftp,dir_name) and dir_name != None:
        ftp.delete(dir_name)   # 删除文件
        print("%s 已删除！"%dir_name)
    elif dir_name == None:
        print("file_name:%s 将删除 %s 目录下所有文件夹（文件除外）！" % (dir_name,ftp.pwd()))
        filelist = ftp.nlst()[2:]   # 列出当前目录下的文件和文件夹列表并去掉前两个元素
        print(filelist)
        for i in filelist:
            if os.path.isfile(i):
                print("%s 是文件" % i)
            else:
                try:
                    ftp.rmd(i)  # 删除文件)  # 重定向到指定路径
                    print("%s 是文件夹，已删除！" % i)
                except ftplib.error_perm as e:
                    print('无法删除 %s，文件夹里似乎还有东西！报错信息："%s"' %(i,e))
    else:
        print("%s 未找到，删除中止！" % dir_name)

# 遍历目录下所有文件和文件夹
# def Traversing(ftp,path = "/233"):
    # pwdinfo(ftp, path)
    # files = ftp.nlst()[2:]  # 得到path目录下的所有文件名称
    # print(files)
    # files_temp = []
    # for file in files:  # 遍历文件夹
    #     print(file)
    #     if os.path.isdir(path):
    #         print("it's a directory")
    #     elif os.path.isfile(path):
    #         print("it's a normal file")
    #     else:
    #         print("it's a special file(socket,FIFO,device file)")

        # if os.path.isfile(file):  # 判断是否是文件夹，不是文件夹才打开
        #     print(file)
        #     file_cwd = ftp.cwd(file)     # 打开文件
        #     # f = open(path + "/" + file)     # 打开文件
        #     iter_f = iter(file_cwd)    # 创建迭代器
        #     str_temp = ""
        #     for line in iter_f:  # 遍历文件，一行行遍历，读取文本
        #         str_temp = str_temp + line
        #     files_temp.append(str_temp)  # 每个文件的文本存到list中
    # print(files_temp)  # 打印结果


# 搜索（遍历）删除文件夹或文件
def DeleteDirFiles(ftp,dirpath = "/",DirFiles_name = None):
    """
    搜索（遍历）删除文件夹或文件
    :param ftp: 调用connect()方法的变量
    :param dirpath:限定搜索的路径范围，默认值为“/”根目录
    :param DirFiles_name:默认值为None,若为None,则递归删除参数dirpath目录下所有的文件和文件夹；若不为None,则递归寻找参数dirpath目录下名为DirFiles_name的文件或文件夹并删除！
    :return:
    """
    pwdinfo(ftp, dirpath)
    if DirFiles_name == None:
        DeleteFile(ftp, dirpath)    #删除该目录下所有文件


def main():
    ftp = connect()                  #连接登陆ftp
    # dirpath = "test"    #文件夹名
    # ftp.cwd(dirpath)
    # mkdir(ftp,"test2")
    # print("当前路径:%s" % ftp.pwd())  # 返回当前所在位置
    # ftp.cwd("/233/666/888/999")
    # print("当前路径:%s" % ftp.pwd())  # 返回当前所在位置
    # DeleteFile(ftp, "/233/")
    DeleteDir(ftp, "/233/")
    # Traversing(ftp)
    # upload(ftp,"D:\\workspace\\PythonSpace\\Spyder\\Spyder_aixinxi\\1.jpg")       #上传本地文件
    # filepath = "018465277C419D288C652804D6B73926"  #上传文件名
    # filepath = "1.jpg"  #上传文件名
    # filepath = "DhzSUkJU0AA3b0M.png"  #上传文件名
    # upload(ftp,filepath,fileNameMD5(filepath))
    disconnect(ftp)

    # filename="test1.txt"
    # ftp.rename("test.txt", filename) #文件改名
    # if os.path.exists(filename):   #判断本地文件是否存在
    #     os.unlink(filename)    #如果存在就删除
    # download(ftp,filename)        #下载ftp文件
    # listinfo(ftp)                   #打印目录下每个文件或文件夹的详细信息
    # files = ftp.nlst()              #获取路径下文件或文件夹列表
    # print(files)
    #
    #
    # ftp.delete(filename)              #删除远程文件
    # ftp.rmd("dir1")                  #删除远程目录
    # ftp.quit()  #退出

if __name__ == '__main__':
    main()