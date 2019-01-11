# -*- coding: utf-8 -*-
import re

import scrapy
from urllib.parse import urljoin

from AmericanRealEstate.items import StateNameCountyNameItem,CountyNameZipCodeItem


class TruliaStateCountyZipSpider(scrapy.Spider):
    name = 'trulia_state_county_zip'
    allowed_domains = ['trulia.com']
    # 这里的custom_settings可能没有起作用，
    start_urls = ['https://www.trulia.com/sitemap/']
    custom_settings = {
        "DEFAULT_REQUEST_HEADERS": {
        'authority': 'www.trulia.com',
        'method': 'GET',
        # 'path':'/sitemap/Alabama-real-estate/',
        'scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,ja;q=0.8',
        'cache-control': 'no-cache',
        # 'cookie': '_pxvid=05b33ba0-1304-11e9-be80-9143a92e94bf; s_fid=091772EA4252BCF3-30BDFCA435C410CC; PHPSESSID=vj6b7af38oqrrr0aehfqmqkho4; tlftmusr=190108pl07q98uuuefvs6nqxgg00w200; fvstts=20190108; csrft=60gaQOvgw%2Fp7eh0FCcWF5LVfL3UBaHguiFbnBzfL56E%3D; _ga=GA1.2.1739258178.1546936361; _gid=GA1.2.233419384.1546936361; s_cc=true; G_ENABLED_IDPS=google; s_vi=[CS]v1|2E1A303E05316460-40000114000000CC[CE]; QSI_S_ZN_aVrRbuAaSuA7FBz=v:0:0; fontsLoaded=1; __gads=ID=8c7c897faf592e2c:T=1546936722:S=ALNI_MY0hzlDQvXNNDEo2j_KzgUapqeVkQ; previousSearchOptions=optQuery0%3Dprice_reductions%253D0%2526type%253Daddress%2526open_homes%253D0%2526subtype%253Dcity%2526city%253DNassau%2526state%253DNY%2526st%253Dh%3BoptQuery1%3Dprice_reductions%253D0%2526type%253Daddress%2526open_homes%253D0%2526subtype%253Dcity%2526city%253DMontgomery%2526state%253DAL%2526st%253Dh%3BoptQuery2%3Dprice_reductions%253D0%2526type%253Daddress%2526open_homes%253D0%2526subtype%253Dcity%2526city%253DJuneau%2526state%253DAK%2526st%253Dh%3BoptQuery3%3Dprice_reductions%253D0%2526type%253Daddress%2526open_homes%253D0%2526subtype%253Dcity%2526city%253DNew%2BYork%2526state%253DNY%2526st%253Dh%3BoptQuery4%3Dprice_reductions%253D0%2526type%253Daddress%2526open_homes%253D0%2526subtype%253Dcity%2526city%253DAmerican%2BCanyon%2526state%253DCA%2526st%253Dh; previousSearches=locQuery0%3DNassau%2C%2BNY%3BlocQuery1%3DMontgomery%2C%2BAL%3BlocQuery2%3DJuneau%2C%2BAK%3BlocQuery3%3DNew%2BYork%2C%2BNY%3BlocQuery4%3DAmerican%2BCanyon%2C%2BCA; search_parameter_set=%7B%22searchType%22%3A%22for_sale%22%2C%22location%22%3A%7B%22cities%22%3A%5B%7B%22city%22%3A%22New+York%22%2C%22state%22%3A%22NY%22%7D%5D%7D%2C%22filters%22%3A%7B%22page%22%3A1%2C%22view%22%3A%22map%22%2C%22limit%22%3A30%2C%22sort%22%3A%7B%22type%22%3A%22best%22%2C%22ascending%22%3Atrue%7D%7D%7D; promptdata=%7B%22c%22%3A%7B%22pg-srp%22%3A23%2C%22pg-pdp%22%3A12%7D%2C%22pd%22%3A%5B%5D%2C%22pts%22%3Anull%7D; s_sq=%5B%5BB%5D%5D; trul_visitTimer=1547022942454_1547023923594; SERVERID=webfe902|XDW2N; _px3=16c280b25b22146133e6300c3849888074cac604fad9832b741ecc7c16eedcb0:/h9aVy8h1snaWH6FxYxD3dM7Nve9PDofXUU5AL0/0mv1tiVblPOdQRkMXZr1NHTUyWG/apF2DNESBJGj6eohFA==:1000:4fE9ljEmSuHOK8RfsW+J8LWPUSGfsqHjZS0cMk3dv06YLvRyp8KhLDc5s6nszaq0X1PiF1XTrI2Ov75ChnX2RMfuq+zAj9RMIwQ55CWHW+34YqPjoA2FDcHnRbE5uSeM/vx2mAa0zsr9Ca+UpuUu5DN2dQBnCLAsRZiVFw69mxE=',
        # 'referer': 'https://www.trulia.com/sitemap/,',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'

    },
    "DOWNLOADER_MIDDLEWARES" : {
        # 'AmericanRealEstate.middlewares.AmericanrealestateDownloaderMiddleware': 543,
        'AmericanRealEstate.middlewares.HeadersMiddleware': 542,
    },
        "ITEM_PIPELINES" :{
        # 'AmericanRealEstate.pipelines.AmericanrealestatePipeline': 300,

        'AmericanRealEstate.pipelines.StateNameCountyNamePipeline': 301,
        # 'AmericanRealEstate.pipelines.CountyZipCodePipeline': 302,
    },

    }


    def parse(self, response):
        # states = response.text
        # with open('./test.html','w') as f:
        #     f.write(states)
        states = response.css('.real-estate-markets li a')
        # 获取详情页的连接

        for state in states:
            states_real_estate_urls = state.css('::attr(href)').extract_first()
            # print(states_real_estate_urls)
            # states_name = state.css('::text').extract_first()
            # print(states_name)
            next_url = urljoin(response.url,states_real_estate_urls)
            # print(next_url)
            # print(state.replace(' real estate',''))
            yield scrapy.Request(url=next_url,callback=self.parse_counties)

    def parse_counties(self, response):
        counties = response.css('.all-counties-sitemap-links li a')
        state_county_item = StateNameCountyNameItem()
        for county in counties:
            states_real_estate_urls = county.css('::attr(href)').extract_first()
            # print(states_real_estate_urls)
            county_name = county.css('::text').extract_first()
            state_county_item['county'] = county_name
            if len(re.findall(r'County',county_name)) != 0:
                true_county_name = county_name.replace(' County', '')
            if len(re.findall(r'Parish',county_name)) != 0:
                true_county_name = county_name.replace(' Parish', '')
            if len(re.findall(r'Borough',county_name)) != 0:
                true_county_name = county_name.replace(' Borough', '')

            # print(true_county_name)
            state_name = re.findall(r'sitemap/(.*)-real-estate',response.url)[0].replace('-',' ')
            state_county_item['stateName'] = state_name
            state_county_item['countyName'] = true_county_name
            yield state_county_item

            next_url = urljoin(response.url, states_real_estate_urls)
            # print(next_url)
            # print(state.replace(' real estate',''))
            yield scrapy.Request(url=next_url, callback=self.parse_zipcode)

    def parse_zipcode(self,response):
        zip_codes = response.css('.all-zip-codes-sitemap-links li a')
        county_zip_item = CountyNameZipCodeItem()
        for zip_code in zip_codes:
            zip_number = zip_code.css('::text').extract_first()
            if len(re.findall(r'County',response.url)) != 0:
                county_name = re.findall(r'real-estate/(.*)-County',response.url)[0].replace('-',' ')
            if len(re.findall(r'Parish',response.url)) !=0:
                county_name = re.findall(r'real-estate/(.*)-Parish', response.url)[0].replace('-', ' ')
            if len(re.findall(r'Borough',response.url)) !=0:
                county_name = re.findall(r'real-estate/(.*)-Borough', response.url)[0].replace('-', ' ')
            county_zip_item['countyName'] = county_name
            county_zip_item['zipCode'] = zip_number
            yield county_zip_item
