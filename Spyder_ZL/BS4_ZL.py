import requests
from bs4 import *
import re
'''
0.url地址
1.使用最简单的怕取方式测试，
2.如果1获取失败，创建session对象，
3.写入headers
4.get:params=None, cookie=None, header=None, timeout=20
5.或者post:data, header=None, cookie=None, params=None, verify=False, proxie=None
6.用content或者text获取已经爬到的数据
7.创建一个bs对象
8.find_all筛选标签，返回列表
'''


def ZL_Session_Fun(ZL_URL,jl='北京+上海+广州+深圳+南京',kw='京东商城',pagenumber='3'):
    ZL_Session = requests.session()
    ZL_Session.headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
    }
    for p in range(1,int(pagenumber)+1):
        ZL_Session.params = {
            'jl':jl,
            'kw':kw,
            'p':p,
            'kt':2,
            'isadv':0,
        }

        ZL_Session_Requests = ZL_Session.get(url=ZL_URL)
        return ZL_BS4_hander(ZL_Session_Requests,ZL_Session)

def ZL_BS4_hander(ZL_Session_Requests,ZL_Session):
    ZL_soup = BeautifulSoup(ZL_Session_Requests.content,'lxml')
    ZL_listsoup = ZL_soup.find_all('table',{'class':"newlist"})
    searchresult_list = []
    for href in ZL_listsoup[1:]:
        ZL_RE_ZWMC = re.findall(r'bold" target="_blank">(.*)</a',str(href))
        print(ZL_RE_ZWMC)
        ZL_BS4_gsmc = ((href.find('td', {"class": "gsmc"})).find('a')).text
        ZL_RE_zwyx = re.findall(r'class="zwyx">(.*)</td>',str(href))
        ZL_RE_gzdd = re.findall(r'<td class="gzdd">(.*)</td>',str(href))
        ZL_RE_GShref = re.findall(r'<a href="(.*)" par',str(href))
        ZL_RE_gxsj = re.findall(r'<td class="gxsj"><span>(.*)</span>',str(href))
        ZL_RE_GZJY = re.findall('<span>经验：(.*)</span><span>',str(href.find('li',{'class':'newlist_deatil_two'})))

        GS_info_dirct = {
            '职位名称':ZL_RE_ZWMC,
            '公司名称':ZL_BS4_gsmc,
            '职位月薪':ZL_RE_zwyx,
            '工作地点':ZL_RE_gzdd,
            '公司详情':ZL_RE_GShref,
            '发布日期':ZL_RE_gxsj,
            '工作经验':ZL_RE_GZJY,
        }
        ZL_Result_str, TURN_ZL_Session =ZL_company_info(GS_info_dirct,ZL_Session)
        #保存至文件和数据库
        ZL_Result_Save_File(ZL_Result_str, TURN_ZL_Session)


def ZL_company_info(GS_info_dirct,ZL_Session):
    ZL_URL = GS_info_dirct['公司详情'][0]
    ZL_company_info_Session = requests.session()
    ZL_company_info_Session.headers = {
        'Host': 'jobs.zhaopin.com',
        'Referer': 'http: // sou.zhaopin.com / jobs / searchresult.ashx',
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
    }

    ZL_Session_Requests = ZL_company_info_Session.get(url=ZL_URL)
    return ZL_company_info_hander(ZL_Session_Requests,GS_info_dirct,ZL_Session)

def ZL_company_info_hander(ZL_Session_info_Requests,GS_info_dirct,ZL_Session):
    '''
    工作经验
    招聘人数
    职位类别
    职位描述
    公司介绍
    :param ZL_Session_RZL_Session_info_Requestsequests:
    :return:
    '''
    ZL_company_info_hander_soup = BeautifulSoup(ZL_Session_info_Requests.content,'lxml')
    ZL_company_info_hander_listsoup = ZL_company_info_hander_soup.find_all('div',{'class':"terminalpage-left"})
    for href in ZL_company_info_hander_listsoup:
        ZL_BS4_GZJY = re.findall(r'<li><span>工作经验：</span><strong>(.*)</strong></li>',str(href))
        ZL_BS4_ZPRS = re.findall(r'<li><span>招聘人数：</span><strong>(.*) </strong></li>',str(href))
        ZL_BS4_ZWLB = re.findall(r'<li><span>职位类别：</span><strong><a href="(.*)" target="_blank">(.*)</a></strong></li>',str(href))[0][1]
        ZL_BS4_ZWMS = (href.find('div',{'class':"tab-inner-cont"})).text
        ZL_BS4_GSJS = ((href.find_all('div',{'class':"tab-inner-cont"}))[1]).text
        GS_Dinfo_dirct = {
            '工作经验':ZL_BS4_GZJY,
            '招聘人数':ZL_BS4_ZPRS,
            '职位类别':ZL_BS4_ZWLB,
            '职位描述':ZL_BS4_ZWMS,
            '公司介绍':ZL_BS4_GSJS,
        }
        return ZL_company_Str_handler(GS_info_dirct,GS_Dinfo_dirct,ZL_Session)

def ZL_company_Str_handler(GS_info_dirct,GS_Dinfo_dirct,ZL_Session):
    ZL_Result_str = '''
    基本信息：
            '职位名称':%s,
            '公司名称':%s,
            '职位月薪':%s,
            '工作地点':%s,
            '公司详情':%s,
            '发布日期':%s,
            '工作经验':%s,
            
    详细信息：
            '工作经验':%s,
            '招聘人数':%s,
            '职位类别':%s,
            '职位描述':%s,
            '公司介绍':%s,
    '''%(
        GS_info_dirct['职位名称'],
        GS_info_dirct['公司名称'],
        GS_info_dirct['职位月薪'],
        GS_info_dirct['工作地点'],
        GS_info_dirct['公司详情'],
        GS_info_dirct['发布日期'],
        GS_info_dirct['工作经验'],
        GS_Dinfo_dirct['工作经验'],
        GS_Dinfo_dirct['招聘人数'],
        GS_Dinfo_dirct['职位类别'],
        GS_Dinfo_dirct['职位描述'],
        GS_Dinfo_dirct['公司介绍'],
    )

    # return ZL_Result_Save_File(ZL_Result_str,ZL_Session)
    return ZL_Result_str,ZL_Session

def ZL_Result_Save_File(ZL_Result_str,Filrname):
    with open('%s(%s地区).txt'%(Filrname.params['kw'],Filrname.params['jl']),'a') as f:
        f.write(ZL_Result_str)

if __name__ == '__main__':

    ZL_URL = 'http://sou.zhaopin.com/jobs/searchresult.ashx'
    jl = input('请输入要搜索的职位地区(如：北京+上海+广州+深圳+南京)：')
    kw = input('请输入要搜索的公司(如：京东商城)：')
    pagenumber = input('请输入要搜索的页数(如：3)：')
    ZL_Session_Fun(ZL_URL,jl,kw,pagenumber)