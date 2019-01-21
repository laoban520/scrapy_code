# -*- coding: utf-8 -*-
import scrapy
from bwm.items import BwmItem
# 步骤：
# 1、设置setting.py文件的请求头等等数据
# 2、分析网页提取数据，在bwm5上写代码
# 3、设置items.py代码
# 4、保存图片，zaipipelines.py上操作


class Bwm5Spider(scrapy.Spider):
    name = 'bwm5'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/65.html']

    def parse(self, response):
        capcha_urls=response.xpath("//div[@class='uibox']")[1:]
        for capcha_url in capcha_urls:
            caption=capcha_url.xpath(".//div[@class='uibox-title']/a/text()").get()
            img_urls=capcha_url.xpath(".//ul/li/a/img/@src").getall()
            # for img_url in img_urls:
            #     img_url=response.urljoin(img_url)
            img_url=list(map(lambda img_url:response.urljoin(img_url),img_urls))
            item=BwmItem(caption=caption,img_urls=img_url)
            yield item


