# -*- coding:utf-8 -*-
'''by sudo rm -rf  http://imchenkun.com'''
import scrapy
from matpro.items import MatproItem
import urlparse
from scrapy.crawler import CrawlerProcess



class MailSpider(scrapy.Spider):
    name = 'matpro'
    #allowed_domains = ["apps.webofknowledge.com"]
    start_urls = ["https://www.materialsproject.org"]#为什么该成这样就不行，　用下面的网址就可以

   # def openpage(self):
    #    url = "https://www.materialsproject.org/janrain/loginpage/?next=/"
  #      yield scrapy.Request(url,callback=self.parse)

    def parse(self, response):
        filename = "matprol"
        with open(filename, 'wb') as f:
            f.write(response.body)
