# -*- coding: utf-8 -*-
import scrapy


class JandanMeizhiSpider(scrapy.Spider):
    name = 'jandan_meizhi'
    allowed_domains = ['jandan.net/']
    start_urls = ['http://jandan.net/ooxx/page-1#comments']

    def parse(self, response):
        meizhi_urls=response.xpath("//div[@class='text']")

        for meizhi_url in meizhi_urls:
            img_urls=meizhi_url.xpath(".//img/@src").getall()
            for img_url in img_urls:
                print(img_url)
