# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
from urllib import request

class BwmPipeline(object):
    def __init__(self):
        self.path=os.path.join(os.path.dirname(os.path.dirname(__file__)),'image')
        if not os.path.exists(self.path):
            os.mkdir(self.path)
    def process_item(self, item, spider):
        caption=item['caption']
        img_url=item['img_url']

        caption_path=os.path.join(self.path,caption)
        if not os.path.exists(caption_path):
            os.mkdir(caption_path)
        for url in img_url:
            img_name=url.split('_')[-1]
            request.urlretrieve(url,os.path.join(caption_path,img_name))
        return item



