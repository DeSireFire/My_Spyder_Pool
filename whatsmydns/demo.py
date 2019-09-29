# coding=utf8
import requests,re
import json,os,chardet
import sys


def test():
    '''
    获取DNS名的token
    :return:
    '''
    for i in range(0,10):
        URL = "https://www.whatsmydns.net/"
        # headers={"accept-encoding":'gzip'}
        req = requests.get(URL)
        # req = requests.get(URL, headers=headers)
        req.encoding = chardet.detect(req.content)['encoding']
        if req.encoding == "GB2312":
            req.encoding = "GBK"
        print(req.encoding)
        pattern = re.compile('<input type="hidden" name="_token" id="_token" value="(.*?)" />',re.S)
        titles = re.findall(pattern,req.text)
        print("%s:%s"%(i,titles))

def confir(str):

    for i in range(0,32):
        str = str.replace(chr(i),'')
    return  str


if __name__ == '__main__':
    print(sys.getdefaultencoding())
    # test()

    # temp = "[{'债券名称': '佛山市国星光电股份有限公司2011年公司债券', '债券简称': '11国星债', '债券代码': '112083', '债券类型': '普通企业债', '债券面值（元）': '100', '债券年限（年）': '5', '票面利率': '6.8', '到期日': '2017-05-03', '兑付日': '2017-05-03', '摘牌日': '1970-01-01', '利率说明': '本期公司债券的期限为5年期，附第3年末投资者回售选择权。本期债券的询价区间为6.80%-7.30%，本期公司债券的票面利率为固定利率，在债券存续期内固定不变，票面利率由公司和保荐人（主承销商）通过市场询价协商确定。', '计息方式': '固定利率', '付息方式': '周期性付息', '起息日期': '2012-05-03', '止息日期': '2017-05-02', '年付息次数': '1', '付息日期': '05-03', '发行价格（元）': '100', '发行规模（亿元）': '5', '发行日期': '2012-05-03', '上市日期': '2012-06-21', '上市场所': '深圳交易所', '信用等级': 'AA', '内部信用增级方式': '', '外部信用增级方式': '', '债券公告': []}]"

    # print(temp)
    # print(type(temp))
    # print(temp[1:-1])
    # # print(dict(temp[1:-1]))
    # print(type(eval(temp)))

#     temp = r"""
# [{'债券名称': '佛山市国星光电股份有限公司2011年公司债券', '债券简称': '11国星债', '债券代码': '112083', '债券类型': '普通企业债', '债券面值（元）': '100', '债券年限（年）': '5', '票面利率': '6.8', '到期日': '2017-05-03', '兑付日': '2017-05-03', '摘牌日': '1970-01-01', '利率说明': '本期公司债券的期限为5年期，附第3年末投资者回售选择权。本期债券的询价区间为6.80%-7.30%，本期公司债券的票面利率为固定利率，在债券存续期内固定不变，票面利率由公司和保荐人（主承销商）通过市场询价协商确定。', '计息方式': '固定利率', '付息方式': '周期性付息', '起息日期': '2012-05-03', '止息日期': '2017-05-02', '年付息次数': '1', '付息日期': '05-03', '发行价格（元）': '100', '发行规模（亿元）': '5', '发行日期': '2012-05-03', '上市日期': '2012-06-21', '上市场所': '深圳交易所', '信用等级': 'AA', '内部信用增级方式': '', '外部信用增级方式': '', '债券公告': []}]
#     """
#     print(temp.replace('\r\n',''))
#     print(type(eval(temp.replace(' ',''))))
