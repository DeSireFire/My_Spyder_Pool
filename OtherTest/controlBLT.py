# coding=utf8
# -*- coding: utf-8 -*-
# @Time    : 2019/9/29 14:53
# @Author  : RaXianch
# @project: Spyder.py
# @FileName: controlBLT.py
# @Software: PyCharm
# @github    ：https://github.com/DeSireFire


def cmdRuner(comm):
    '''
    命令执行函数
    :param comm:需要运行的命令
    :return: 执行命令后翻回的结果
    '''
    import os
    result = os.popen(comm)
    return result.read()

def getDockerID():
    # 获取docker ID
    res = cmdRuner(r"docker ps --format '{{.ID}}\t{{.Image}}\t{{.Names}}'")
    temp = {}
    if res:
        for line in res.splitlines():
            if 'zsnmwy/bilibili-live-tools' in line:
                temp[line.split()[0]] = line.split()[2]
    return temp



def runBTL(userName,userPW,Backstage=True):
    '''
    BTL启动器
    :param userName: B站登陆名
    :param userPW: B站用户密码
    :param Backstage: 是否后台运行，默认后台运行
    :return: 返回整理的docker命令
    '''

    # 去除特殊字符，只保留汉字，字母、数字
    import re
    sub_str = re.sub(u"([^\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", userName)

    if Backstage:   # 是否后台运行
        comm = "docker run --name='{dockerName}' -itd --rm -e USER_NAME={userName} -e USER_PASSWORD={userPW} zsnmwy/bilibili-live-tools".format(dockerName=sub_str,userName=userName,userPW=userPW)
    else:
        comm = "docker run --name='{dockerName}' -it --rm -e USER_NAME={userName} -e USER_PASSWORD={userPW} zsnmwy/bilibili-live-tools".format(dockerName=sub_str,userName=userName,userPW=userPW)

    return comm

def crontabADD(crMins='*',crHours='*',crDays='*',crMouDays='*',crWeeks='*',yourComm='pwd'):
    '''
    crontab命令构造
    https://linuxtools-rst.readthedocs.io/zh_CN/latest/tool/crontab.html
    :param crMins: 字符串，例：每小时的第3和第15分钟执行 3，15
    :param crHours: 字符串，例：每天的第3和第15小时执行 3，15。每天3到15小时 3-15
    :param crDays: 字符串，例子：每天执行 *。每隔两天执行 */2
    :param crMouDays: 字符串，例子：每月1、10、22日执行 1,10,22。
    :param crWeeks: 字符串，例子：每周日执行 0，其他以此类推到0~6，周日为一周第一天。
    :param yourComm: 字符串，要crontab控制执行的命令
    :return:
    '''
    comm = "{crMins} {crHours} {crDays} {crMouDays} {crWeeks} {yourComm}".format(
        crMins=crMins, crHours=crHours, crDays=crDays, crMouDays=crMouDays, crWeeks=crWeeks, yourComm=yourComm
    )
    return comm

def crontabFile(commList,startFile=False):
    pass


def choiceHandler(c):
    if c == 1:
        for user in info:   # 遍历多个用户
            for psN in range(0,user['psNum']):  # 用户多开次数
                dockerComm = runBTL(user['name']+'Num%s'%psN, user['pw'])  # 构造启动docker命令
                dockerID = cmdRuner(dockerComm)[:12]
    elif c == 2:
        idList = getDockerID()  # 获取所有有关DD抢辣条的docker进程ID
        for idKey in idList: # 遍历id 逐一关闭。时间较长
            comm = 'docker stop {CONTAINER_ID}'.format(CONTAINER_ID=idKey)
            print('正在关闭 %s ...'%(idList[idKey]))
            print('总进度: {:.2%}'.format(list(idList.keys()).index(idKey)/len(idList.keys())))
            cmdRuner(comm)
    elif c == 3:
        # 格式化打印docker ps
        print(cmdRuner(r"docker ps --format 'table {{.ID}}\t{{.Image}}\t{{.Names}}'"))
    elif c == 4:
        pass
    elif c == 5:
        pass


def menu():
    menuDict = {
        1:'一键启动所有DD抢辣条',
        2:'一键退出所有DD抢辣条',
        3:'显示所有在运行DD抢辣条进程',
        4:'一键设置所有DD抢辣条定时启动',
        5:'一键设置所有DD抢辣条定时关闭',
        0:'退出工具',
    }
    while True:
        print('*'*50)
        for i in menuDict:
            print("%s:%s"%(i,menuDict[i]))
        print('输入 对应选项前的数字 回车即可执行操作')
        print('*'*50)
        c = input('那么，What can i do for you? Tell me:')
        try:
            c = int(c)
            if c not in menuDict.keys():
                raise RuntimeError
            break
        except:
            print('输入有误！')

    if c in [1,2,3,4,5]:    # 是否退出
        print('%s %s Start!' % (c, menuDict[c]))
        choiceHandler(c)
    else:
        pass


if __name__ == '__main__':
    info=[{
        'name':'',
        'pw':'',
        'psNum':2,
    },]
    menu()

# crontabCommStart = crontabADD(crMins='30', crHours='9', crDays='*', crMouDays='*', crWeeks='*',
#                               yourComm=dockerComm)  # 构造定时启动任务命令
# ccsList.append(crontabCommStart)
#
# crontabCommStart = crontabADD(crMins='30', crHours='9', crDays='*', crMouDays='*', crWeeks='*',
#                               yourComm=dockerComm)  # 构造定时关闭任务命令
# ccsList.append(crontabCommStart)
#
# print(ccsList)
# # 生成定时启动任务文件
# crontabFile()
# # 生成定时关闭任务文件
