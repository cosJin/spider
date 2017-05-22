#coding:utf-8
import scrapy
from freebuf2.items import Freebuf2Item
import time
from scrapy.crawler import CrawlerProcess

class freebuf2Spider(scrapy.Spider):
    name ='freebuf2'
    allowed_domains = []

    start_urls = ["http://www.freebuf.com/"]

    def parse(self, response):

        for link in response.xpath("//div[contains(@class, 'news_inner news-list')]/div/a/@href").extract():
            yield scrapy.Request(link, callback=self.parse_next)   #这里不好理解的朋友，先去看看yield的用法。我是按协程（就是中断执行）理解的，感觉容易理解。

        next_url = response.xpath("//div[@class='news-more']/a/@href").extract()#找到下一个链接，也就是翻页。
        if next_url:

            yield scrapy.Request(next_url[0],callback=self.parse)

    def parse_next(self,response):
        item = Freebuf2Item()
        item['title'] = response.xpath("//h2/text()").extract()
        item['url'] = response.url
        item['date'] = response.xpath("//div[@class='property']/span[@class='time']/text()").extract()
        item['tags'] = response.xpath("//span[@class='tags']/a/text()").extract()

        yield item
