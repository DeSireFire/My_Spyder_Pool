import requests,json,time
# from Spyder_Tool import GetIP,ProxiesDataBase,Config,Util
'''
    resp.text返回的是Unicode型的数据。
    resp.content返回的是bytes型的数据。
'''
# Util.Refresh()
# myDirct = Util.Get()
# print(myDirct)
def Company_Spyder(companyID):
    Lg_Session = requests.session()
    # Lg_Session.verify = True
    # Lg_Session.proxies = Util.Get()
    Lg_Session.headers  = {
        'Referer':'https://www.lagou.com/gongsi/j%s.html'%companyID,
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    }
    Lagou_url = 'https://www.lagou.com/gongsi/searchPosition.json'
    str_list = []
    for i in range(1,4):
        time.sleep(5)
        Lg_Session_data = {
            'companyId':companyID,
            'pageNo':i,
            'pageSize':10,
        }
        Lg_requests=Lg_Session.post(url=Lagou_url,data=Lg_Session_data)
        try:
            rec = json.loads(str(Lg_requests.content, encoding = "utf-8"))['content']
                    # json.dumps(Lg_requests.content,ensure_ascii=False)
            for c in range(0,10):
                time.sleep(5)
                rec_content = rec['data']['page']['result'][c]
                rec_str = r"""


                    职位名字：%s
                    工作经验：%s
                    公司全名：%s
                    公司规模：%s
                    职业诱惑：%s %s
                    岗位学历要求：%s
                    公司简介：%s %s %s %s


                 """%(
                    rec_content['positionName'],
                    rec_content['workYear'],
                    rec_content['companyFullName'],
                    rec_content['companySize'],
                    rec_content['positionAdvantage'],
                    str(rec_content['companyLabelList']),
                    rec_content['education'],
                    rec_content['industryField'],
                    rec_content['financeStage'],
                    rec_content['city'],
                    rec_content['district'],
                )
                # time.sleep(5)
                with open(r'%s.txt'%rec_content['companyFullName'],'a') as f:
                    # f.write('\n'.join(rec_content))
                    # f.write(str(rec_content))
                    f.write(rec_str)
                    # f.write(str(str_list))
        except KeyError as KE:
            print('您的操作过于频繁！')
        finally:
            Lg_Session.close()
if __name__ == '__main__':
    company = {'百度':1575,'京东':35422,'阿里巴巴':52840,
               '网易':329,'腾讯':451,'搜狗':1537,
               '360':436,'小米':520,'美团':50702,
               '暴风':1101,'优酷':1914,'金山':7835,
               }
    for i in company:
        company_id = company[i]
        Company_Spyder(companyID=company_id)