# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class  MaterialtestItem(scrapy.Item):
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
class  MaterialstructureItem(scrapy.Item):
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
    a = scrapy.Field()
    b = scrapy.Field()
    c = scrapy.Field()
    alpha = scrapy.Field()
    beta = scrapy.Field()
    gamma = scrapy.Field()
    Miller_Indices = scrapy.Field()
    Surface_Energy = scrapy.Field()
    Area_Fractio = scrapy.Field()
    Average_surface_energy = scrapy.Field()
    Stiffness_Tensor = scrapy.Field()
    ShearModulusAndSoOn = scrapy.Field()
    ICSD = scrapy.Field()
    DOI = scrapy.Field()
    strOp_RunType = scrapy.Field()   
    strOp_EnergyCutoff = scrapy.Field() 
    strOp_Kpoints = scrapy.Field()
    strOp_UValues = scrapy.Field()
    strOp_Pseudopotentials = scrapy.Field()
    strOp_FinalEnergy = scrapy.Field()
    strOp_CorrectedEnergy = scrapy.Field()

    HermannMauguin = scrapy.Field()
    Hall = scrapy.Field()
    PointGroup = scrapy.Field()
    CrystalSystem = scrapy.Field()
