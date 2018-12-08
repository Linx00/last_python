# -*- coding: utf-8 -*-
import json
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanMoviePipeline(object):
    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file = open(f'douban_data.json', 'a', encoding="utf-8")
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()

