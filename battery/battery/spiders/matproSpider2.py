# -*- coding:utf-8 -*-
'''by sudo rm -rf  http://imchenkun.com'''
import scrapy
import json
from  battery.items import BatteryItem
import urlparse

class NmdkSpider(scrapy.Spider):
    name = 'battery'

    start_urls = ['https://www.materialsproject.org/']
    def start_requests(self):
        for i in range(300769791,300769792):
            url="https://www.materialsproject.org/batteries/mp-"+str(i)
            cookies={
                'expected_tab':'facebook',
                'login_tab':'facebooke',
                'sessionid':'yqokg1f1zxsqgqcysnk6sp27h42i1mvk',
                'welcome_info_name':'于学金'}
            headers={
                'Host':'www.materialsproject.org',
                'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
                'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                'Accept-Encoding':'gzip, deflate, br',
                'Cookie':'login_tab=facebook; expected_tab=facebook; welcome_info_name=%u4E8E%u5B66%u91D1; sessionid=uxxgw49cvr9ow8awyzcr7a7ouf9qsmml',
                'Connection':'keep-alive'}

            yield scrapy.Request(url,headers = headers,cookies=cookies,callback=self.parse)
    
    def parse(self,response): 

       #filename = "test2.html"
        #with open(filename, 'wb') as f:
            #f.write(response.body)

        item = BatteryItem()
        # data = json.loads(response.body)      
        item['TotalGravimetricCapacity']=str(response.css('table.table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > span:nth-child(2)::text').extract()[0])+str(response.css('table.table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > span:nth-child(3)').xpath('string(.)').extract()[0])
        item['TotalVolumetricCapacity']=str(response.css('table.table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > span:nth-child(2)::text').extract()[0])+str(response.css('table.table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > span:nth-child(3)').xpath('string(.)').extract()[0])
        item['VolumeChange']=response.css('table.table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(1) > span:nth-child(2)::text').extract()
        item['EnergyDensity']=str(response.css('table.table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(1) > span:nth-child(2)::text').extract()[0])+str(response.css('table.table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(1) > span:nth-child(3)').xpath('string(.)').extract()[0])
        item['SpecificEnergy']=str(response.css('table.table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(1) > span:nth-child(2)::text').extract()[0])+str(response.css('table.table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(1) > span:nth-child(3)').xpath('string(.)').extract()[0])
        item['VoltagePairProperties']='charged:'+response.css('table.table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > a:nth-child(2)').xpath('string(.)').extract()[0]+'        discharge:'+response.css('table.table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > a:nth-child(2)').xpath('string(.)').extract()[0]
        item['EnergyAboveHull_charged']=response.css('table.table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > div:nth-child(1)::text').extract()
        item['EnergyAboveHull_discharged']=response.css('table.table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > div:nth-child(1)::text').extract()
        item['voltage']=response.css('table.table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(5) > div:nth-child(2)::text').extract()
        item['ID']=response.css('span.detail-section:nth-child(3) > h4:nth-child(2)::text').extract()
        #item['working_ion']=response.css('span.detail-section:nth-child(1)').xpath('string(.)').extract()
        #item['working_ion_discharge']=response.xpath('/span[@id="working-ion"]/text()').extract()
        item['IntercalationBatteryFramework']=response.css('span.detail-section:nth-child(1) > h4:nth-child(2)').xpath('string(.)').extract()
        yield item
