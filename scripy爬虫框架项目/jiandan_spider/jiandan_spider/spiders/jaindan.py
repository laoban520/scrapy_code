# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from bs4 import BeautifulSoup
import re


class JaindanSpider(CrawlSpider):
    name = 'jaindan'
    allowed_domains = ['jiandan.net']
    start_urls = ['http://jandan.net/ooxx/page-1#comments']

    rules = (
        Rule(LinkExtractor(allow=r'.+/page-[0-9]+#.*'), callback='parse_page', follow=True),
    )

    def parse_page(self, response):
        soup=BeautifulSoup(response,'lxml')
        imgs=soup.select('img')
        for img in imgs:
            img_url=re.findall('src="(.*?)"',str(img))
            print(img_url)

