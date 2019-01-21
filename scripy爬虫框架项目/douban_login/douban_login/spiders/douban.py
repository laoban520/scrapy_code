# -*- coding: utf-8 -*-
import scrapy
from urllib import request
from PIL import Image


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://accounts.douban.com/login']
    login_url='https://accounts.douban.com/login'

    def parse(self, response):
        fromdata={
            'source':'index_nav',
            'redir':'https://www.douban.com/',
            'from_email':'468673420@qq.com',
            'from_password':'qaz123456789',
            'remember':'on',
            'login':'登录'
        }
        caption_url=response.xpath("//img[@id='captcha_image']/@src").get()
        if caption_url:
            caption=self.region_img(caption_url)
            fromdata['captcha-solution']=caption
            captcha_id=response.xpath("//input[@name='captcha-id']/@value").get()
            fromdata['captcha-id']=captcha_id
            print(fromdata)
        yield scrapy.FormRequest(url=self.login_url,fromdata=fromdata,callback=self.parse_page)

    def parse_page(self,response):
        if response.url=='https://www.douban.com':
            print('登录成功')
        else:
            print('登录失败')

    def region_img(self,img_url):
        request.urlretrieve(img_url,'coption.png')
        image=Image.open('coption.png')
        image.show()
        caption=input("请输入验证码：")
        return caption


