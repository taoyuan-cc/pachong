# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#import json
import pymysql


class TencentPipeline(object):
    def __init__(self):
        self.connect = pymysql.Connect(host="localhost", user="root", password="123456", db="test", charset="utf8")
        self.cur = self.connect.cursor()
        self.cur.execute("create database pc_db character set utf8")
        self.cur.execute("use pc_db")
        self.cur.execute("create table pc_tab(id int unsigned primary key auto_increment not null,title varchar(200),place varchar(200),state varchar(200),name varchar(200),time varchar(200),link varchar(200))")

    def process_item(self, item, spider):
        self.cur.execute("insert into pc_tab(title,place,state,name,time,link)values('%s','%s','%s','%s','%s','%s')" % (item["title"], item["place"], item["state"], item["name"], item["time"], item["link"]))
        self.connect.commit()
        return item

    def close_spider(self, spider):
        self.cur.close()
        self.connect.close()
