# -*- coding: utf-8 -*-
import re
import scrapy
from urllib.parse import urljoin


from AmericanRealEstate.settings import trulia_search_criteria, trulia_search_criteria
from AmericanRealEstate.items import TruliaHouseInfoItem


class TruliaSpider(scrapy.Spider):
    name = 'trulia'
    allowed_domains = ['trulia.com']
    # start_urls = [x for x in trulia_search_criteria][0:1]

    start_urls = ['https://www.trulia.com/County/AL/Baldwin_Real_Estate/']

    custom_settings = {
        "ITEM_PIPELINES": {
            # 'AmericanRealEstate.pipelines.RealtorHouseInfoPipeline': 301,
            'AmericanRealEstate.pipelines.TruliaDetailDomPipeline': 302,

            # 'AmericanRealEstate.pipelines.RealtorHouseInfoTestPipeline': 302,
            # 'scrapy_redis.pipelines.RedisPipeline': 300

        },

        "DOWNLOADER_MIDDLEWARES": {
            'AmericanRealEstate.pipelines.RandomUserAgentMiddleware': 545,
            'AmericanRealEstate.pipelines.ProcessTrulia403Middleware': 546,
    },
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
            # 'cookie': 's_fid=433AA466E2E74246-15C3C4922E6D4B9F; tlftmusr=190111pl5oxe6dz6h9ql8f26dy4gw379; fvstts=20190110; _ga=GA1.2.1370343627.1547191941; s_vi=[CS]v1|2E1C236905033FEB-40001188A0008984[CE]; _pxvid=3becfc80-1573-11e9-8c5b-a9eccfd531c4; G_ENABLED_IDPS=google; __gads=ID=b974a5b2be825d27:T=1547544408:S=ALNI_Mbj9mLodrBnjohkq2yUpkvsqvLaUg; previousSearchOptions=optQuery0%3Dprice_reductions%253D0%2526type%253Daddress%2526open_homes%253D0%2526subtype%253Dcity%2526city%253DGallup%2526state%253DNM%2526zip_code%253D87301%2526st%253Dh%3BoptQuery1%3Dprice_reductions%253D0%2526type%253Daddress%2526open_homes%253D0%2526subtype%253Dcity%2526city%253DAutaugaville%2526state%253DAL%2526st%253Dh%3BoptQuery2%3Dprice_reductions%253D0%2526type%253Daddress%2526open_homes%253D0%2526subtype%253Dcity%2526state%253DNM%2526zip_code%253D87008%2526st%253Dh; previousSearches=locQuery0%3DGallup%2C%2BNM%3BlocQuery1%3DAutaugaville%2C%2BAL%3BlocQuery2%3D%2C%2BNM; PHPSESSID=cc3cnk7h55ar5jbst3f2d5m5q7; csrft=ZmhLK%2FkFDIVtPl%2BqOKZlZ3QEj3iPzGY9EeGUQo8MZI8%3D; _gid=GA1.2.1473634457.1548029162; QSI_S_ZN_aVrRbuAaSuA7FBz=v:0:0; s_cc=true; search_parameter_set=%7B%22searchType%22%3A%22for_sale%22%2C%22location%22%3A%7B%22counties%22%3A%5B%2201001%22%5D%7D%2C%22filters%22%3A%7B%22page%22%3A1%2C%22view%22%3A%22map%22%2C%22limit%22%3A30%2C%22sort%22%3A%7B%22type%22%3A%22best%22%2C%22ascending%22%3Atrue%7D%7D%7D; fontsLoaded=1; promptdata=%7B%22c%22%3A%7B%22pg-srp%22%3A21%2C%22pg-pdp%22%3A11%2C%22pg-cdp%22%3A1%7D%2C%22pd%22%3A%5B%5D%2C%22pts%22%3Anull%7D; trul_visitTimer=1548053958174_1548054352053; SERVERID=webfe335|XEVvV; _px3=9aa8498d56f24129b0c71a7ad318d74577df73554441c358eb93a7afa4f4be18:I2pfK8bZHzNaGS1GmMrmiIsuSg82j98qWFtYjCHqKJtzuHjURYEb75oSE+HGc1ot1Zv6AD855YkJpo7F+DTh5w==:1000:wuQnyap82ccitihuP8XAWXjhBcCLoGJGutCqHjeDAi9tDWUED6qJ/bK1wbqqCiWJXLmcEXkt6LidmGZ+2CQ7rHe9InQbkds7opUbpnlSZ7PJgdHQ+zpNuAWtfSViyk2JH5bgAp1RC3MgrHTXGzDW2OcNwJdlVtWzZcGtD5qJfeo=',
            # 'referer': 'https://www.trulia.com',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',

    },
        "COOKIES_ENABLED": True,
        "COOKIES_DEBUG":True,
        # "AUTOTHROTTLE_ENABLED": True,
        # "DOWNLOAD_DELAY": 1,

    }

    def parse(self, response):
            houses = response.xpath("//div[@class='backgroundControls']//div[@class='containerFluid']/ul//li[contains(@class,'xsCol12Landscape')]")
            for house in houses:
                detail_url = house.xpath(".//a[@class='tileLink']/@href").extract_first()
                true_detail_url = urljoin(response.url,detail_url)
                print(true_detail_url)

                yield scrapy.Request(url=true_detail_url,callback=self.parse_content)

            next_page_url = response.xpath("//a[contains(@aria-label,'Next page')]/@href").extract_first()
            if next_page_url is not None:
                true_next_page_url = urljoin(response.url,next_page_url)
                yield scrapy.Request(url=true_next_page_url, callback=self.parse)

    def parse_content(self,response):
        trulia_house_info_item = TruliaHouseInfoItem()
        price = response.xpath("//span[contains(@data-role,'price')]").extract_first()
        trulia_house_info_item['price'] = price

        yield trulia_house_info_item
