# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanMovieItem(scrapy.Item):
    title = scrapy.Field()
    href = scrapy.Field()
    num = scrapy.Field()
    point = scrapy.Field()
