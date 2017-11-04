# -*- coding: utf-8 -*-
from scrapy import Request
from scrapy_redis.spiders import RedisSpider
from Spyder_Recruitmen.items import SpyderRecruitmenItem
from scrapy.selector import Selector
from random import choice
from . import Value
import re,os,time,random


class ZhilianRecruitmenSpider(RedisSpider):
    name = 'ZhiLian_Recruitmen'
    allowed_domains = ['zhaopin.com']
    host = 'zhaopin.com'
    redis_key = "ZhiLian_Recruitmen:start_urls"
    start_urls = []
    def start_requests(self):
        for page in range(1,2):
            for Job_Kw in Value.Job_Keyword:
                for Address_Kw in Value.Address_Keyword:
                    for Company_Kw in Value.Company_Keyword:
                        start_url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%s&kw=%s%s%s&sm=0&p=%s'%(Address_Kw,Company_Kw,'%20',Job_Kw,page)
                        print(start_url)
                        self.start_urls.append(start_url)
                        os.system("redis-cli lpush ZhiLian_Recruitmen:start_urls %s" % start_url)
        for url in self.start_urls:
            Sleep_time = random.randint(0, 10)
            print('睡眠～%s秒' % Sleep_time)
            time.sleep(Sleep_time)
            yield Request(url=url, callback=self.parse)

    def rep_handler(self,var):
        try:
            var = str(var)
            for i in ['?', ":", "*", ' ', '<[^>]+>']:
                var.replace(r'%s' % i, '')
                dr = re.compile(r'<[^>]+>', re.S)
                var = dr.sub('', var)
        except Exception as ex:
            print(ex)
        return var

    def parse(self, response):
        body = self.rep_handler(response.body.decode('utf8'))
        infos = re.findall('<td class="zwmc" style="width: 250px;">(.*?)href="(.*?)" ', body)
        if len(infos) > 0:
            for info in infos:
                items = SpyderRecruitmenItem()
                items['url'] = info[1]
                yield Request(url=items['url'], callback=self.detail, meta={'item': items})
                # 详情页面


    def detail(self, response):
        '''
        jobName = scrapy.Field()
        companyName = scrapy.Field()
        salary = scrapy.Field()
        address = scrapy.Field()
        pushDate = scrapy.Field()
        url = scrapy.Field()
        jobinfo = scrapy.Field()
        companyInfo = scrapy.Field()
        RecruitmenWeb = scrapy.Field() #区分招聘信息的来源
        :param response:
        :return:
        '''
        items = response.meta['item']
        body = self.rep_handler(response.body.decode('utf8'))
        jobName = re.findall(' <h1>(.*?)</h1>', body)
        if len(jobName) > 0:
            items['jobName'] = jobName[0]
        companyName = re.findall(' <h2><a onclick="recordOutboundLink(.*?)target="_blank">(.*?)<img ', body)
        if len(companyName) > 0:
            items['companyName'] = companyName[0][1]
        salary = re.findall('<li><span>职位月薪：</span><strong>(.*?)<a', body)
        if len(salary) > 0:
            items['salary'] = str(salary[0])
        address = re.findall('<li><span>工作地点：</span><strong>(.*?)>(.*?)</a>', body)
        if len(address) > 0:
            items['address'] = address[0][1]
        pushDate = re.findall(' <li><span>发布日期：</span>(.*?)>(.*?)</span>', body)
        if len(pushDate) > 0:
            items['pushDate'] = pushDate[0][1]
        # jobinfo = re.findall('<div class="tab-inner-cont"><p>(.*?)</p><p>(.*?)</P> ', body)
        jobinfo =  Selector(text=body).xpath('//div[6]/div[1]/div[1]/div/div[1]/p').extract()
        if len(jobinfo) > 0:
            items['jobinfo'] = jobinfo
        items['RecruitmenWeb'] = '%s_table' % self.name
        yield items
