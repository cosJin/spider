# -*- coding:utf-8 -*-
'''by sudo rm -rf  http://imchenkun.com'''
import scrapy
from matpro.items import MatproItem
import urlparse

class MailSpider(scrapy.Spider):
    name = 'matpro3'
    start_urls = ['https://www.materialsproject.org/']
    def start_requests(self):
        for i in range(1,70000):
            url="https://www.materialsproject.org/materials/mp-"+str(i)+"/"
            cookies={
                'expected_tab':'facebook',
                'login_tab':'facebooke',
                'sessionid':'uxxgw49cvr9ow8awyzcr7a7ouf9qsmml',
                'welcome_info_name':'于学金'}
            headers={
                'Host':'www.materialsproject.org',
                'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
                'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                'Accept-Encoding':'gzip, deflate, br',
                'Cookie':'login_tab=facebook; expected_tab=facebook; welcome_info_name=%u4E8E%u5B66%u91D1; sessionid=uxxgw49cvr9ow8awyzcr7a7ouf9qsmml',
                'Connection':'keep-alive'}

            yield scrapy.Request(url,headers = headers,cookies=cookies)
    
    def parse(self,response):
        item = MatproItem()
        doc = response.xpath('//div[@class="row detail-header"]/span[@class="detail-section"]/h4')
        item['Material'] = doc[0].xpath('string(.)').extract()[0]
        item['ID'] = doc[1].xpath('string(.)').extract()[0]
        item['Final_Magnetic_Moment'] = response.xpath('//table[@class="table data table-bordered"]/tbody/tr/td/span[@class="value"]/text()').extract()[0]
        item['Magnetic_Ordering'] = response.xpath('//table[@class="table data table-bordered"]/tbody/tr/td/span[@class="value"]/text()').extract()[2]
        item['Formation_Energy_Atom'] = response.xpath('//table[@class="table data table-bordered"]/tbody/tr/td/span[@class="value"]/text()').extract()[3]
        item['Energy_Above_Hull_Atom'] = response.xpath('//table[@class="table data table-bordered"]/tbody/tr/td/span[@class="value"]/text()').extract()[4]
        item['Density'] = response.xpath('//table[@class="table data table-bordered"]/tbody/tr/td/span[@class="value"]/text()').extract()[5]
        Decomposes = response.xpath('//table[@class="table data table-bordered"]/tbody/tr/td/span[@class="value"]')
        item['Decomposes_To'] = Decomposes[5].xpath('string(.)').extract()[0]
        item['Band_Gap'] = response.xpath('//table[@class="table data table-bordered"]/tbody/tr/td/span[@class="value"]/text()').extract()[4]
        yield item
