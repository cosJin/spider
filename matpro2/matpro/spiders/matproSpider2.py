# -*- coding:utf-8 -*-
'''by sudo rm -rf  http://imchenkun.com'''
import scrapy
from matpro.items import MatproItem
import urlparse

class MailSpider(scrapy.Spider):
    name = 'matpro2'
    start_urls = ['https://www.materialsproject.org/']
    def start_requests(self):
        url="https://www.materialsproject.org/materials/mp-1"
        cookies={
            'expected_tab':'facebook',
            'login_tab':'facebooke',
            'sessionid':'uxxgw49cvr9ow8awyzcr7a7ouf9qsmml',
            'welcome_info_name':'于学金'
                   }
        return [scrapy.Request(url,cookies=cookies,callback=self.parse)]
    
    def parse(self,response):
        filename = "matprol"
        with open(filename, 'wb') as f:
            f.write(response.body)
