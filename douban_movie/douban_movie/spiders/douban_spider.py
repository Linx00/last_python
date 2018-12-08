import scrapy
from scrapy import Request
from lxml import etree
import time
import json
from .. import items

class Douban_movie(scrapy.Spider):
    name = 'douban_movie'

    def start_requests(self):
        for a in range(10):
            url ='https://book.douban.com/top250?start={0}'
            yield Request(url = url.format(a*25),callback=self.parse)

    def parse(self, response):
        data = response.text
        s = etree.HTML(data)
        file = s.xpath('//*[@id="content"]/div/div[1]/div/table')
        time.sleep(2)
        for q in file:
            title = q.xpath("./tr/td[2]/div[1]/a/@title")[0]
            href = q.xpath('./tr/td[2]/div[1]/a/@href')[0]
            num = q.xpath('./tr/td[2]/div[2]/span[3]/text()')[0].strip("(").strip(" ").strip(")")
            point = q.xpath('./tr/td[2]/div[2]/span[2]/text()')[0]
            item = items.DoubanMovieItem()
            item['title'] = title
            item['href'] = href
            item['num'] = num
            item['point'] = point
            yield item

