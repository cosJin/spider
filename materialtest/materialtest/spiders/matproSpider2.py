# -*- coding:utf-8 -*-
'''by sudo rm -rf  http://imchenkun.com'''
import scrapy
from materialtest.items import MaterialstructureItem
import urlparse

class MailSpider(scrapy.Spider):
    name = 'test_structure'
    start_urls = ['https://www.materialsproject.org/']
    def start_requests(self):
        for i in range(1,40):
            url="https://www.materialsproject.org/materials/mp-"+str(i)+"/"
            cookies={
                'expected_tab':'facebook',
                'login_tab':'facebooke',
                'sessionid':'jpu4vuhia8wb8tot7g8o1afjnsp1x90v',
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
        #filename = "test.txt"
        #with open(filename, 'wb') as f:
            #f.write(response.body)
        item = MaterialstructureItem()
        spaceGroup = response.xpath('//table[@id="spacegroup"]/tbody/tr/td/span[@class="value"]')
        item['HermannMauguin'] = spaceGroup[0].xpath('string(.)').extract()[0]
        item['Hall'] = spaceGroup[1].xpath('text()').extract()
        item['PointGroup'] = spaceGroup[2].xpath('string(.)').extract()[0]
        item['CrystalSystem'] = spaceGroup[3].xpath('text()').extract()
        item['strOp_RunType'] = response.css('.calc-summary-table > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > span:nth-child(2)::text').extract() 
        item['strOp_EnergyCutoff'] = response.css('.calc-summary-table > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > span:nth-child(2)::text').extract()
        item['strOp_Kpoints'] = response.css('.calc-summary-table > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > span:nth-child(2)::text').extract()
        item['strOp_UValues'] = response.css('.calc-summary-table > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > span:nth-child(2)::text').extract()
        item['strOp_Pseudopotentials'] = response.css('.calc-summary-table > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(1) > span:nth-child(2)::text,.calc-summary-table > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(1) > span:nth-child(3)::text').extract()
        item['strOp_FinalEnergy'] = response.css('.calc-summary-table > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2) > span:nth-child(2)::text').extract()
        item['strOp_CorrectedEnergy'] = response.css('.calc-summary-table > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(1) > span:nth-child(2)::text').extract()
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
        ####item['a'] = response.css('.table-hover > tbody:nth-child(2) > tr > td:nth-child(1)::text,.table-hover > tbody:nth-child(2) > tr > td:nth-child(1) > span::text').extract()
        ####item['b'] = response.css('#comp-lattice ul:nth-child(1) li:nth-child(2)  div:nth-child(2)  div:nth-child(1)::text').extract()有了但还没写
        ####item['c'] = response.css('#comp-lattice ul:nth-child(1) li:nth-child(3)  div:nth-child(2)  div:nth-child(1)::text').extract()有了但还没写
        ####item['alpha'] = response.css('#comp-lattice ul:nth-child(2)  li:nth-child(1)  div:nth-child(2)  div:nth-child(1)::text').extract()有了但还没写
        ####item['beta'] = response.css('#comp-lattice ul:nth-child(2)  li:nth-child(2) div:nth-child(2) div:nth-child(1)::text').extract()有了但还没写
        ####item['gamma'] = response.css('#comp-lattice ul:nth-child(2)  li:nth-child(2) div:nth-child(2) div:nth-child(1)::text').extract()有了但还没写
        item['Miller_Indices'] = response.css('.table-hover > tbody:nth-child(2) > tr > td:nth-child(1)::text,.table-hover > tbody:nth-child(2) > tr > td:nth-child(1) > span::text').extract()#有的数字上面有一个横线，注意观察。
        item['Surface_Energy'] = response.css('.table-hover > tbody:nth-child(2) > tr > td:nth-child(2)::text').extract()#按顺序来，两两一组，依次对应。
        item['Area_Fractio'] = response.css('.table-hover > tbody:nth-child(2) > tr > td:nth-child(3)::text').extract()#一个一个依次对应。
        item['Average_surface_energy'] = response.css('.surfaces-table > p:nth-child(2)::text').extract()#应该只有两个数，但爬出来的数据不干净
        item['Stiffness_Tensor'] = response.css('.front > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(2) > tr > td::text').extract()#目测为六乘六矩阵，所以前六个为第一行，下面6个是第二行，以此类推。
        item['ShearModulusAndSoOn'] = response.css('.elastic-table > tbody:nth-child(1) > tr> td> span:nth-child(2)::text').extract()#目测矩阵固定，所以前两个为第一行，以此类推。
        item['DOI'] = response.css('span.detail-section:nth-child(5) > h4:nth-child(2)::text').extract()
        item['ICSD'] = response.css('.icsd > ul:nth-child(1) > li::text').extract()
        yield item
