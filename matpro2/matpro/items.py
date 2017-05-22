# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MatproItem(scrapy.Item):
    # define the fields for your item here like:
    
    Material = scrapy.Field()
    ID = scrapy.Field()
    Final_Magnetic_Moment = scrapy.Field()
    Magnetic_Ordering = scrapy.Field()
    Formation_Energy_Atom = scrapy.Field()
    Energy_Above_Hull_Atom = scrapy.Field()
    Density = scrapy.Field()
    Decomposes_To = scrapy.Field()
    Band_Gap = scrapy.Field()
 
