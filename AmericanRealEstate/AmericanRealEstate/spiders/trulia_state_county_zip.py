# -*- coding: utf-8 -*-
import re

import scrapy
from urllib.parse import urljoin

from AmericanRealEstate.items import StateNameCountyNameItem,CountyNameZipCodeItem, SearchCriteriaItem


class TruliaStateCountyZipSpider(scrapy.Spider):
    name = 'trulia_state_county_zip'
    allowed_domains = ['trulia.com']
    # 这里的custom_settings可能没有起作用，
    start_urls = ['https://www.trulia.com/sitemap/']
    custom_settings = {
        "DEFAULT_REQUEST_HEADERS": {
            # "referer": "https://www.trulia.com/",
            'authority': 'www.trulia.com',
            'method': 'GET',
            # 'path':'/sitemap/Alabama-real-estate/',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9,ja;q=0.8',
            'cache-control': 'max-age=0',
            'cookie': 's_fid=433AA466E2E74246-15C3C4922E6D4B9F; tlftmusr=190111pl5oxe6dz6h9ql8f26dy4gw379; fvstts=20190110; _ga=GA1.2.1370343627.1547191941; s_vi=[CS]v1|2E1C236905033FEB-40001188A0008984[CE]; _pxvid=3becfc80-1573-11e9-8c5b-a9eccfd531c4; PHPSESSID=jeggrdnphgs8cccvlpbs45i1j0; csrft=jA0ya2SbWv3cOtEpj66HYO%2BeAi5DCp0GGeJWxahT8pk%3D; _gid=GA1.2.1042690951.1548056115; QSI_S_ZN_aVrRbuAaSuA7FBz=v:0:0; s_cc=true; fontsLoaded=1; __gads=ID=e54b8c8a9d0a3af6:T=1548144822:S=ALNI_MbTTP258XwNoU2W760CAOClFmDtSg; previousSearchOptions=optQuery0%3Dprice_reductions%253D0%2526type%253Daddress%2526open_homes%253D0%2526subtype%253Dcity%2526city%253DNew%2BYork%2526state%253DNY%2526st%253Dh%3BoptQuery1%3Dprice_reductions%253D0%2526type%253Daddress%2526open_homes%253D0%2526subtype%253Dcity%2526city%253DClayton%2526state%253DAL%2526zip_code%253D36016%2526st%253Dh%3BoptQuery2%3Dprice_reductions%253D0%2526type%253Daddress%2526open_homes%253D0%2526subtype%253Dcity%2526state%253DNY%2526zip_code%253D10001%2526st%253Dh; previousSearches=locQuery0%3DNew%2BYork%2C%2BNY%3BlocQuery1%3DClayton%2C%2BAL%3BlocQuery2%3D%2C%2BNY; search_parameter_set=%7B%22searchType%22%3A%22for_sale%22%2C%22location%22%3A%7B%22zips%22%3A%5B%2210001%22%5D%7D%2C%22filters%22%3A%7B%22page%22%3A1%2C%22view%22%3A%22map%22%2C%22limit%22%3A30%2C%22sort%22%3A%7B%22type%22%3A%22best%22%2C%22ascending%22%3Atrue%7D%7D%7D; promptdata=%7B%22c%22%3A%7B%22pg-srp%22%3A21%2C%22pg-pdp%22%3A4%7D%2C%22pd%22%3A%5B%5D%2C%22pts%22%3Anull%7D; s_sq=%5B%5BB%5D%5D; trul_visitTimer=1548152351080_1548154535289; SERVERID=webfe207|XEb2q; _px3=3103951464d2ee5a547b883715ce5dc2c2fadb6029d589cfb527d2ad30e8f124:XM76iBK2oR/XExiYGfkCMHAHDlp4k6gwQxWuTE9PTWDj7t6eZ3h7WnntSZcO4Qf7AqZNUOecBjMMin47YIocXg==:1000:D1mIU7wAkIJLyzqQ4dG2iRwr6/L6pWBiiGuHeFD5SwvlELKYxRmr0OdEwkkvNWWi3jWyc41DwaHWRvT+vRiQ0qz0blA85SUGpDVMBwaFJC1XCvC9rhSEx39voJqeBbluRH78AHbgQEtp6WKfaoyjGiyoeIGUrHQ2lgFMxgz07xY=',
            'referer': 'https://www.trulia.com',
            'upgrade-insecure-requests': '1',
            # 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',

    },
    "DOWNLOADER_MIDDLEWARES" : {
        # 'AmericanRealEstate.middlewares.AmericanrealestateDownloaderMiddleware': 543,
        # 'AmericanRealEstate.middlewares.HeadersMiddleware': 542,
         'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
         'AmericanRealEstate.middlewares.RandomUserAgentMiddleware': 543,
    },
        "ITEM_PIPELINES" :{
        # 'AmericanRealEstate.pipelines.AmericanrealestatePipeline': 300,

        # 'AmericanRealEstate.pipelines.StateNameCountyNamePipeline': 301,
        # 'AmericanRealEstate.pipelines.CountyZipCodePipeline': 302,
            'AmericanRealEstate.pipelines.SearchCriteriaPipeline': 302,

    },
        "COOKIES_ENABLED": False,
        "COOKIES_DEBUG": True,

        # # 自动限速设置：
        # "AUTOTHROTTLE_ENABLED": True,
        # "DOWNLOAD_DELAY": 1

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
        # state_county_item = StateNameCountyNameItem()
        for county in counties:
            states_real_estate_urls = county.css('::attr(href)').extract_first()
            # print(states_real_estate_urls)
            # url ='https://www.trulia.com/sitemap/Alabama-real-estate/'
            full_county_name = county.css('::text').extract_first()
            # state_county_item['county'] = county_name
            # if len(re.findall(r'County',county_name)) != 0:
            #     true_county_name = county_name.replace(' County', '')
            # if len(re.findall(r'Parish',county_name)) != 0:
            #     true_county_name = county_name.replace(' Parish', '')
            # if len(re.findall(r'Borough',county_name)) != 0:
            #     true_county_name = county_name.replace(' Borough', '')

            # print(true_county_name)
            state_name = re.findall(r'sitemap/(.*)-real-estate',response.url)[0].replace('-',' ')
            # state_county_item['stateName'] = state_name
            # state_county_item['countyName'] = true_county_name
            meta_data = {'stateName': state_name,'full_county_name':full_county_name}
            # yield state_county_item

            next_url = urljoin(response.url, states_real_estate_urls)
            # print(next_url)
            # print(state.replace(' real estate',''))
            yield scrapy.Request(url=next_url, meta=meta_data,callback=self.parse_zipcode)

    def parse_zipcode(self,response):
        zip_codes = response.css('.all-zip-codes-sitemap-links li a')
        state_name = response.meta['stateName']
        full_county_name = response.meta['full_county_name']
        search_criteria_item = SearchCriteriaItem()
        # county_zip_item = CountyNameZipCodeItem()
        for zip_code in zip_codes:
            zip_number = zip_code.css('::text').extract_first()

            if len(re.findall(r'County',response.url)) != 0:
                county_name = re.findall(r'real-estate/(.*)-County',response.url)[0].replace('-',' ')
            if len(re.findall(r'Parish',response.url)) !=0:
                county_name = re.findall(r'real-estate/(.*)-Parish', response.url)[0].replace('-', ' ')
            if len(re.findall(r'Borough',response.url)) !=0:
                county_name = re.findall(r'real-estate/(.*)-Borough', response.url)[0].replace('-', ' ')

            search_criteria_item['stateName'] = state_name
            search_criteria_item['countyName'] = county_name
            search_criteria_item['fullCountyName'] = full_county_name
            search_criteria_item['zipCode'] = zip_number
            yield search_criteria_item

            # county_zip_item['countyName'] = county_name
            # county_zip_item['zipCode'] = zip_number
            # yield county_zip_item

