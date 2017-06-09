# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BatteryItem(scrapy.Item):
    # define the fields for your item here like:
    TotalGravimetricCapacity = scrapy.Field()
    TotalVolumetricCapacity = scrapy.Field()
    VolumeChange = scrapy.Field()
    EnergyDensity = scrapy.Field()
    SpecificEnergy = scrapy.Field()
    VoltagePairProperties = scrapy.Field()
    EnergyAboveHull_charged = scrapy.Field()
    EnergyAboveHull_discharged = scrapy.Field()
    voltage = scrapy.Field()
    ID = scrapy.Field()
    working_ion=scrapy.Field() 
    working_ion_discharge=scrapy.Field()
    IntercalationBatteryFramework = scrapy.Field()