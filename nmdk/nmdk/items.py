# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NmdkItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    porous_material = scrapy.Field()
    Pore_Limiting_Diameter = scrapy.Field()
    Largest_Cavity_Diameter = scrapy.Field() 
    Accessible_Surface_Area = scrapy.Field() 
    Void_Fraction = scrapy.Field()
    Crystal_Density = scrapy.Field()
    Lattice_Parameters_abc = scrapy.Field() 
    Lattice_Parameters_abr = scrapy.Field() 
    Lattice_Parameters_volume = scrapy.Field() 
    Final_Structure = scrapy.Field()
    hoa_x = scrapy.Field()
    hoa_y = scrapy.Field()
    isotherm_x = scrapy.Field()
    isotherm_y = scrapy.Field()
    MPID= scrapy.Field()