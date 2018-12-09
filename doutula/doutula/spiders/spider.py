import scrapy
from scrapy import Request
import requests
import os
from .. import items

class Doutu(scrapy.Spider):
    name = 'doutu'

    def start_requests(self):
        url = 'http://www.doutula.com/photo/list/?page={0}'
        for i in range(1, 100):
            yield Request(url=url.format(i),callback=self.parse)

    def parse(self, response):
        root = response.xpath('//*[@id="pic-detail"]/div/div[3]/div[2]/ul/li/div/div/a')
        x = 0
        for q in root:
            x= x+1
            item = items.DoutulaItem()
            item['name'] = q.xpath('//p/text()').extract()[x]
            item['img_url'] = q.xpath('//@data-original').extract()[x]

            fitst_suffox = os.path.splitext(str(item['img_url']))[1]
            a = fitst_suffox[0:4]

            a_filename = item['name'] + a
            print('准备下载图片，链接为' + str(item['img_url']))
            r = requests.get(item['img_url'])
            try:
                with open('image\\' + a_filename, mode='wb') as url:
                    url.write(r.content)
                print('下载第' + a_filename + '张图片成功')

            except Exception:
                print('error')
            yield item


