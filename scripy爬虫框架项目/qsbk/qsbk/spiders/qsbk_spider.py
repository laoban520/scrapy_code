# -*- coding: utf-8 -*-
import scrapy
from qsbk.items import QsbkItem

class QsbkSpiderSpider(scrapy.Spider):
    name = 'qsbk_spider'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['http://qiushibaike.com/page/1/']
    hearder="http://qiushibaike.com"

    def parse(self, response):
        duanzhidivs=response.xpath("//div[@id='content-left']/div")
        for duanzhidiv in duanzhidivs:
            author=duanzhidiv.xpath(".//h2/text()").get().strip()
            content=duanzhidiv.xpath(".//div[@class='content']//text()").getall()
            content="".join(content).strip()
            item=QsbkItem(author=author,content=content)
            yield item
        next_url=response.xpath("//ul[@class='pagination']/li[last()]/a/@href").get()
        if not next_url:
            return
        else:
            yield scrapy.Request(self.hearder+next_url,callback=self.parse)


