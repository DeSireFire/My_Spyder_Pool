import requests,json
import execjs
# URL = "https://www.jd.com/brand/1713d78182f3e112c2fe.html"
URL = "https://item.jd.com/39969536201.html"
# URL = "https://c0.3.cn/stock?skuId=39969536201&cat=1713,3259,3333&venderId=791615&area=1_72_4137_0&buyNum=1&choseSuitSkuIds=&extraParam={%22originid%22:%221%22}&ch=1&fqsp=0&pduid=15385627490782077221312&pdpin=&coord=&detailedAdd=&callback=jQuery4312773"
headers = {
# 'Origin':'https://item.jd.com',
# 'Referer':'https://item.jd.com/39969536201.html',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
}
jsFunc = '''
    function add(x,y){
    return x+y*y;
    }
'''
jscontext = execjs.compile(jsFunc)
a = jscontext.call('add',3,5)
print(a)
# 可识别字符串，元组，字典，列表等
# r = requests.get(URL, headers=headers)
# print(r.text)