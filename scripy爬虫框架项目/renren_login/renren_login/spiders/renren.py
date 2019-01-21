# -*- coding: utf-8 -*-
import scrapy


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']

    def start_requests(self):
        url="http://www.renren.com/SysHome.do"
        data={"num":"18720892174","password":"python123"}
        request=scrapy.FormRequest(url,formdata=data,callback=self.parse_page)
        yield request

    def parse_page(self, response):
        with open('renren.html','w',encoding='utf-8') as fp:
            fp.write(response.text)
