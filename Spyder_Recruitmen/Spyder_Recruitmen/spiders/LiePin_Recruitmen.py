# -*- coding: utf-8 -*-
from scrapy import Request
from scrapy_redis.spiders import RedisSpider
from Spyder_Recruitmen.items import SpyderRecruitmenItem
# from scrapy.selector import Selector
from scrapy.conf import settings
from . import Value
import re,os,time

class LiepinRecruitmenSpider(RedisSpider):
    name = 'LiePin_Recruitmen'
    allowed_domains = ['liepin.com']
    start_urls = []
    temp_urls = []
    # start_urls = ['http://liepin.com/']
    host = 'www.liepin.com'
    redis_key = "LiePin_Recruitmen:start_urls"
    #redis 要记得提前注册
    #redis-cli lpush LiePin_Recruitmen:start_urls https://www.liepin.com/
    if Value.Job_Keyword:
        for Job_Kw in Value.Job_Keyword:
            # URL拼接处理
            url_information = "https://www.liepin.com/zhaopin/?key=%s"%Job_Kw
            start_urls.append(url_information)
    else:
        print('未发发现Job_Keyword有需要搜索的职位关键词！执行下一步操作。')
    if Value.Address_Keyword:
        for Address_Kw in Value.Address_Keyword:
            # URL拼接处理,dqs=城市编号
            dps = {
                '北京':"010",
                '上海':"020",
                '广州':"050020",
                '深圳':"050090",
                '天津':"030",
                '苏州':"060080",
                '重庆':"040",
                '成都':"280020",
                '杭州':"070020",
                '武汉':"170020",
                '南宁':"110020",
            }
            for i in range(0,len(start_urls)):
                # url_information = "https://www.liepin.com/zhaopin/?key=%s" % Company_Kw
                temp_urls.append( r'%s&dps=%s'%(start_urls[i],dps[Address_Kw]))
        start_urls = []
        start_urls = temp_urls
        temp_urls = []
    else:
        print('未发发现Address_Keyword有需要搜索的职位关键词！执行下一步操作。')
    if Value.Company_Keyword:
        for Company_Kw in Value.Company_Keyword:
            # URL拼接处理
            for i in range(len(start_urls)):
                temp_urls.append(r'%s&key=%s' % (start_urls[i], Company_Kw))
        start_urls = []
        start_urls = temp_urls
        temp_urls = []
    else:
        print('未发发现Company_Keyword有需要搜索的职位关键词！执行下一步操作。')
    for url_redis in start_urls:
        os.system('redis-cli lpush LiePin_Recruitmen:start_urls %s'%url_redis)
        # time.sleep(3)
    print('URL池 start_urls 装填完毕！')



    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse,headers={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"})

    def rep_handler(self, var):
        return var.replace('\n', '').replace('\t', '').replace('\r', '')

    def parse(self, response):
        body = self.rep_handler(response.body.decode('utf8'))
        info = re.findall(
            'class="job-info">(.*?)href="(.*?)"(.*?)_9\'\)">(.*?)</a>(.*?)warning">(.*?)</span>(.*?)"area">(.*?)</a>(.*?)edu">(.*?)</span>(.*?)</span>(.*?)title="(.*?)"',
            body)

        for item in info:
            items = SpyderRecruitmenItem()
            items['jobName'] = item[3]
            items["salary"] = item[5]
            items["address"] = item[7]
            items["pushDate"] = item[12]
            items["url"] = item[1]
            items['RecruitmenWeb'] = '%s_table'%self.name

            yield Request(url=items["url"], callback=self.detail, meta={"item": items})

    def detail(self, response):
        items = response.meta["item"]
        body = self.rep_handler(response.body.decode('utf8'))
        jobinfo = re.findall('class="content content-word">(.*?)</div>', body)
        if len(jobinfo) > 0:
            items["jobinfo"] = jobinfo[0]
        companyInfo = re.findall('class="info-word">(.*?)</div>', body)
        if len(companyInfo) > 0:
            items["companyInfo"] = companyInfo[0]
        companyName = re.findall('<h1(.*?)<h3>(.*?)title="(.*?)"', body)
        if len(companyName) > 0:
            items["companyName"] = companyName[0][2]
        yield items