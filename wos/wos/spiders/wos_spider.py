import scrapy
from wos.items import WosItem

class DmozSpider(scrapy.Spider):
    name = "wos"
    allowed_domains = ["apps.webofknowledge.com"]
    start_urls = [
        "http://apps.webofknowledge.com/Search.do?product=UA&SID=X17BaPA4nTiF1eu2YUa&search_mode=GeneralSearch&prID=2aa25143-061e-4b86-b782-e48a6e13d573"
    ]
 
    def parse(self, response):
        for sel in response.xpath('//div/a[@class="smallV110"]'):
            item = WosItem()
            item['title'] = sel.xpath('value/text()').extract()
            item['site']=sel.xpath('@href').extract()
            yield item 
