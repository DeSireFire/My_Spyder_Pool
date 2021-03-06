import json
import os

# 创建一个xstr类，用于处理从文件中读出的字符串
class xstr:
    def __init__(self, instr):
        self.instr = instr

    # 删除“//”标志后的注释
    def rmCmt(self):
        qtCnt = cmtPos = slashPos = 0
        rearLine = self.instr
        # rearline: 前一个“//”之后的字符串，
        # 双引号里的“//”不是注释标志，所以遇到这种情况，仍需继续查找后续的“//”
        while rearLine.find('//') >= 0: # 查找“//”
            slashPos = rearLine.find('//')
            cmtPos += slashPos
            # print 'slashPos: ' + str(slashPos)
            headLine = rearLine[:slashPos]
            while headLine.find('"') >= 0: # 查找“//”前的双引号
                qtPos = headLine.find('"')
                if not self.isEscapeOpr(headLine[:qtPos]): # 如果双引号没有被转义
                    qtCnt += 1 # 双引号的数量加1
                headLine = headLine[qtPos+1:]
                # print qtCnt
            if qtCnt % 2 == 0: # 如果双引号的数量为偶数，则说明“//”是注释标志
                # print self.instr[:cmtPos]
                return self.instr[:cmtPos]
            rearLine = rearLine[slashPos+2:]
            # print rearLine
            cmtPos += 2
        # print self.instr
        return self.instr

    # 判断是否为转义字符
    def isEscapeOpr(self, instr):
        if len(instr) <= 0:
            return False
        cnt = 0
        while instr[-1] == '\\':
            cnt += 1
            instr = instr[:-1]
        if cnt % 2 == 1:
            return True
        else:
            return False

def fileDel(filePath):
    if os.path.exists(filePath):
        # 删除文件，可使用以下两种方法。
        os.remove(filePath)
        # os.unlink(my_file)
    else:
        print('no such file:%s' % filePath)

def jsonHandler(filePath):
    fileDel(os.path.join(os.getcwd(), 'temp.json'))
    f = open(filePath,'r')
    fList = f.read()
    # fList = f.readlines()

    f.close()
    with open(os.path.join(os.getcwd(),'temp.json'),'a') as w:
        # for i in fList:
        #     xline = xstr(i)
        #     w.write(xline.rmCmt())
        xline = xstr(fList)
        w.write(xline.rmCmt())

    # f = open(os.path.join(os.getcwd(),'temp.json'),'r')
    # jsonFile = f.read()
    # f.close()
    # fileDel(os.path.join(os.getcwd(), 'temp.json'))
    # jsonV2 = json.loads(jsonFile)
    # # for i in jsonV2:
    # #     print(i,jsonV2[i])
    #
    # for i in jsonV2['inbounds']:
    #     print(i)
if __name__ == '__main__':
    jsonHandler('config.json')