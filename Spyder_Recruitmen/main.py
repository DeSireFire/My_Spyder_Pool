from scrapy import cmdline
from os import system
#Scrapy默认是不能在IDE中调试的，需要以下操作
cmdline.execute(['scrapy','crawl','LiePin_Recruitmen'])
#前两个参数是不变的，第三个参数请使用自己的spider的名字
# system('redis-cli lpush LiePin_Recruitmen:start_urls https://www.liepin.com/')
# redis-cli lpush LiePin_Recruitmen:start_urls https://www.liepin.com/
# redis-cli lpush LiePin_Recruitmen:start_urls https://www.liepin.com/zhaopin/?key=python
