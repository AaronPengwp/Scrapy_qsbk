# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class QsbkPipeline(object):
    def __init__(self):
        self.fp = open('duauzi.json','w',encoding='utf-8')
    def open_spider(self,spider):
        print("爬虫开始了。。。")


    def process_item(self, item, spider):#items一有数据就会传过来
        # 方法一：
        # item_json = json.dumps(item,ensure_ascii=False)
        # 方法二：items不是字典不能直接dumps了
        item_json = json.dumps(dict(item), ensure_ascii=False)
        self.fp.write(item_json+'\n')

        return item

    def close_spider(self,spider):
        self.fp.close()
        print("爬虫结束了。。。")

