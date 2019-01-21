from scrapy import signals
from selenium import webdriver
import time
from scrapy.http.response.html import HtmlResponse
class seleniumdownloadmiddeware(object):
    def __init__(self):
        self.driver=webdriver.Chrome(executable_path=r"D:\chromedrive\chromedriver.exe")
    def process_request(self,request,spider):
        try:
            self.driver.get(request.url)
            time.sleep(1)
            source=self.driver.page_source   #获取详情页
            responce=HtmlResponse(url=self.driver.current_url,body=source,request=request,encoding='utf-8')
        except:
            pass
        return responce