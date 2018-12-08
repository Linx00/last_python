import requests
from lxml import etree
import time
def douban_movie():
    with open ('C:/Users\linx00\Desktop\df.csv','w',encoding='utf-8') as f:
        for a in range(10):
            url =' https://book.douban.com/top250?start={}'.format(a*25)
            data = requests.get(url).text

            s=etree.HTML(data)
            file = s.xpath('//*[@id="content"]/div/div[1]/div/table')
            time.sleep(2)
            for q in file:

                title = q.xpath("./tr/td[2]/div[1]/a/@title")[0]
                href=q.xpath('./tr/td[2]/div[1]/a/@href')[0]
                num=q.xpath('./tr/td[2]/div[2]/span[3]/text()')[0].strip("(").strip(" ").strip(")")
                point = q.xpath('./tr/td[2]/div[2]/span[2]/text()')[0]
                f.write("{}{}{}{}".format(title, href, num, point))

if __name__ == '__main__':
    douban_movie()


