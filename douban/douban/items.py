# -*- coding: utf-8 -*-
import scrapy
'''by sudo rm -rf  http://imchenkun.com'''


class DoubanMailItem(scrapy.Item):
    sender_time = scrapy.Field()     # 发送时间
    sender_from = scrapy.Field()     # 发送人
    url = scrapy.Field()             # 豆邮详细地址
    title = scrapy.Field()           # 豆邮标题
