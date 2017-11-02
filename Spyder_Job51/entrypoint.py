from scrapy import cmdline
#Scrapy默认是不能在IDE中调试的，需要以下操作
cmdline.execute(['scrapy','crawl','Job51'])
#前两个参数是不变的，第三个参数请使用自己的spider的名字

