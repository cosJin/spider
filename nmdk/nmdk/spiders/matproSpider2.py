# -*- coding:utf-8 -*-
'''by sudo rm -rf  http://imchenkun.com'''
import scrapy
import json
from nmdk.items import NmdkItem
import urlparse

class NmdkSpider(scrapy.Spider):
    name = 'nmdk'

    start_urls = ['https://www.materialsproject.org/']
    def start_requests(self):
        for i in range(457988,457989):
            url="https://www.materialsproject.org/porous/NMGC-"+str(i)+"/data"
            cookies={
                'expected_tab':'facebook',
                'login_tab':'facebooke',
                'sessionid':'92zoiwf6tusa817ija7rfqr1yxhqp6uo',
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

        #filename = "test.json"
        #with open(filename, 'wb') as f:
            #f.write(response.body)

        item = NmdkItem()
        data = json.loads(response.body)      
        try:
            item['hoa_x'] = data['sorb_props'][0]['hoa'][0]['series_data']['pres']['value']
            item['hoa_y'] = data['sorb_props'][0]['hoa'][0]['series_data']['hoa']['value']
        except:
            pass
        try:
            item['isotherm_x'] = data['sorb_props'][0]['isotherm'][0]['series_data']['pres']['value']
            item['isotherm_y'] = data['sorb_props'][0]['isotherm'][0]['series_data']['load']['value']
        except:
            pass
        item['porous_material']=data['formula']
        item['Pore_Limiting_Diameter'] = str(data['props']['PLD']['value'])+data['props']['PLD']['units']
        item['Largest_Cavity_Diameter'] = str(data['props']['LCD']['value'])+data['props']['LCD']['units']
        item['Accessible_Surface_Area'] = str(data['props']['ASA']['value'])+data['props']['ASA']['units']
        item['Void_Fraction'] = str(data['props']['void_fraction']['value'])+data['props']['void_fraction']['units']
        item['Crystal_Density'] = str(data['props']['crystal_density']['value'])+data['props']['crystal_density']['units']
        item['Lattice_Parameters_abc'] = "a:"+str(data['lattice']['a'])+",b:"+str(data['lattice']['b'])+",c:"+str(data['lattice']['c'])
        item['Lattice_Parameters_abr'] = "alpha:"+str(data['lattice']['alpha'])+",beta:"+str(data['lattice']['beta'])+",gamma:"+str(data['lattice']['gamma'])
        item['Lattice_Parameters_volume'] = data['lattice']['volume']
        item['Final_Structure'] = data['cif'].split('_atom_site_fract_z')[1].split('#')[0]
        yield item
