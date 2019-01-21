# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from twisted.enterprise import adbapi
from pymysql import cursors

class JianshuSpiderPipeline(object):
    def __init__(self):
        data_py={
            'host':'127.0.0.1',
            'port':3306,
            'user':'root',
            'password':'qaz1234',
            'database':'text',
            'charset':'utf8'
        }
        self.conn=pymysql.connect(**data_py)
        self.curson=self.conn.cursor()
        self._sql=None
    def process_item(self, item, spider):
        self.curson.execute(self.sql,(item['name'],item['date_time'],item['author'],
                                      item['avater'],item['artice_id'],item['orgin_url'],
                                      item['content']))
        self.conn.commit()
        return item
    @property
    def sql(self):
        if not self._sql:
            self._sql="""
            insert into jianshu_spider(id,name,data_time,aythor,avater,artice_id,
            orgin_url,content) values(null,%s,%s,%s,%s,%s,%s,%s)
            """
            return self._sql
        return self._sql

class jianshuspiderpipline(object):
    def __init__(self):
        db_data={
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'root',
            'password': 'qaz1234',
            'database': 'text',
            'charset': 'utf8',
            'cursorclass':cursors.DictCursor
        }
        self.dbpool=adbapi.ConnectionPool('pymysql',**db_data)
        self._sql=None
    @property
    def sql(self):
        if not self._sql:
            self._sql = """
                            insert into jianshu_spider(id,name,data_time,aythor,avater,artice_id,
                            orgin_url,content,read_count,like_count,word_count,subjects) values(null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                            """
            return self._sql
        return self._sql
    def process_item(self,item,spider):
        defer=self.dbpool.runInteraction(self.insert_item,item)
        defer.addErrback(self.handle_error,item,spider)
    def insert_item(self,cursor,item):
        cursor.execute(self.sql,(item['name'],item['date_time'],item['author'],
                                      item['avater'],item['artice_id'],item['orgin_url'],
                                      item['content'],item['read_count'],item['like_count'],item['word_count'],item['subjects']))
    def handle_error(self,error,item,spider):
        print('='*10+'error'+'='*10)
        print(error)
        print('='*10+'error'+'='*10)

