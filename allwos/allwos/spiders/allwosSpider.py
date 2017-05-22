#coding:utf-8
# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy
from allwos.items import AllwosItem
import time
from scrapy.crawler import CrawlerProcess

class allwosSpider(scrapy.Spider):
    name ='allwos'
    allowed_domains = [] 
    start_urls = ["http://apps.webofknowledge.com/Search.do?product=UA&SID=Z2aKgYhMT2DBISoN5j8&search_mode=GeneralSearch&prID=b08b2c49-3891-4a6d-943d-570973a4fa50"]

    def parse(self, response):
        ####page[0]=response.xpath('//td[@class="goto"]/span[@id="pageCount.bottom"]/text()').extract()
        for link in response.xpath('//div/a[@class="smallV110"]/@href').extract():
            link = 'http://apps.webofknowledge.com'+link
            yield scrapy.Request(link, callback=self.parse_next)#这里不好理解的朋友，先去看看yield的用法。我是按协程（就是中断执行）理解的，感觉容易理解。

        page=response.xpath('//td[@class="goto"]/span[@id="pageCount.bottom"]/text()').extract()
        pg = page[0].split(',')
        pagecount=pg[0]+pg[1]     
        pageCount=int(pagecount)       #得到总页数pageCount
        for pageNow in range(2,pageCount+1):
            next_url = "http://apps.webofknowledge.com/summary.do?product=UA&parentProduct=UA&search_mode=GeneralSearch&parentQid=&qid=1&SID=Z2aKgYhMT2DBISoN5j8&&update_back2search_link_param=yes&page="+str(pageNow)
            yield scrapy.Request(next_url,callback=self.parse)


###############################################################
    def parse_next(self,response):
        item = AllwosItem()
        item['source'] = response.xpath('//div[@class="block-record-info block-record-info-source"]/p[@class="sourceTitle"]/value/text()').extract()#源杂志
        item['num'] = response.xpath('//div[@class="block-record-info block-record-info-source"]/p[@class="FR_field"]/value/text()').extract()	#文献号
        item['title'] = response.xpath('//div[@class="title"]/value/text()').extract()						#题目

        yield item
