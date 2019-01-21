# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JianshuSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name=scrapy.Field()
    date_time=scrapy.Field()
    content=scrapy.Field()
    orgin_url=scrapy.Field()
    author=scrapy.Field()
    avater=scrapy.Field()
    artice_id=scrapy.Field()
    like_count=scrapy.Field()
    read_count=scrapy.Field()
    word_count=scrapy.Field()
    subjects=scrapy.Field()

