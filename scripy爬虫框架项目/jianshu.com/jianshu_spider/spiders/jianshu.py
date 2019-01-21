# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from jianshu_spider.items import JianshuSpiderItem


class JianshuSpider(CrawlSpider):
    name = 'jianshu'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'.*/p/[0-9a-z]{12}.*'), callback='parse_page', follow=True),
    )

    def parse_page(self, response):
        name=response.xpath("//h1[@class='title']/text()").get()
        date_time=response.xpath("//span[@class='publish-time']/text()").get().replace("*","")
        avater=response.xpath("//a[@class='avatar']/img/@src").get()
        avater=response.urljoin(avater)
        author=response.xpath("//span[@class='name']/a/text()").get()
        orain_url=response.url
        url1=orain_url.split("?")[0]
        artice_id=url1.split("/")[-1]
        content=response.xpath("//div[@class='show-content-free']").get()
        read_count=response.xpath("//span[@class='views-count']/text()").get()
        like_count=response.xpath("//span[@class='likes-count']/text()").get()
        word_count=response.xpath("//span[@class='comments-count']/text()").get()
        subjects=",".join(response.xpath("//div[@class='include-collection']/a/div/text()").getall())

        item=JianshuSpiderItem(
            name=name,
            date_time=date_time,
            avater=avater,
            author=author,
            orgin_url=orain_url,
            artice_id=artice_id,
            content=content,
            read_count=read_count,
            like_count=like_count,
            word_count=word_count,
            subjects=subjects
        )
        yield item
