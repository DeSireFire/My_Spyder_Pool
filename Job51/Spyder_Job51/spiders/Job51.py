import scrapy
from scrapy import Request
import re
from Spyder_Job51.items import Spyder_Job51Item


class DmozSpider(scrapy.Spider):
    name = 'Job51'#entrypoint中的spider名字就在这里
    #51job前程无忧爬虫
    def info_input(self):
        pass

    def start_requests(self):
        #城市：郑州;关键词python
        #TODO 改为自定义城市和自定义搜索词
        urls = [
            'http://search.51job.com/list/170200,000000,0000,00,9,99,python,2,1.html',
            'http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=170200%2C020000&keyword=python&keywordtype=2&lang=c&stype=2&postchannel=0000&fromType=1&confirmdate=9'
        ]
        for url in urls:#urls列表里可放多个地址
            yield Request(url=url,callback=self.parse)

    def rep_handler(self, var):
        return var.replace('\n', '').replace('\t', '').replace('\r', '')

    def parse(self, response):
        # response.body约等于request.content
        body = self.rep_handler(response.body.decode('gbk'))
        #去除影响正则的符号
        info = re.findall(
            '<div class="el">(.*?)title="(.*?)" href="(.*?)"(.*?)title="(.*?)" (.*?)"t3">(.*?)</span>(.*?)"t4">(.*?)</span>(.*?)t5">(.*?)</span>',
            body
        )
        #正则匹配

        if len(info)>0:
            #如果info存在值，提起数据并格式化
            for item in info:
                item_sub = Spyder_Job51Item()
                item_sub['JobName'] = item[1]
                item_sub['companyName'] = item[4]
                item_sub['salary'] = item[8]
                item_sub['address'] = item[6]
                item_sub['pushDate'] = item[10]
                item_sub['url'] = item[2]
                yield Request(url=item[2],callback=self.detail,meta={'item':item_sub})


    def detail(self,response):
        item_detail = response.meta['item']
        body = self.rep_handler(response.body.decode('gbk'))
        jobinfo = re.findall('class="bmsg job_msg inbox">(.*?)<div class="mt10">', body)
        if len(jobinfo)>0:
            item_detail['jobinfo'] = jobinfo[0]
        companyinfo = re.findall('class="tmsg inbox">(.*?)</div>', body)
        if len(companyinfo)>0:
            item_detail['companyInfo'] = companyinfo[0]
        yield item_detail