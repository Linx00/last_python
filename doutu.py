from lxml import etree
import requests
import os
import time
from urllib3 import request
import math

def parse_page(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        # 'Cookie': '__cfduid=d4210dc3ed8de1204c343da44f31fd42a1540104618; UM_distinctid=166956388842c2-0ab753f7ea6edf-9393265-1fa400-16695638887d0; CNZZDATA1256911977=1735521639-1540103958-null%7C1540103958; _ga=GA1.2.1210168187.1540104620; _gid=GA1.2.1626829238.1540104620; yjs_id=450be6eb241191471abcbbc2824660c9; ctrl_time=1; XSRF-TOKEN=eyJpdiI6InpudDAxKzlyelAwYXNGaFdKQVh1QWc9PSIsInZhbHVlIjoicWM4SjBRR2p4Z0w5bWh4cU9qN0twc1krUFlZQUpndUlBcTZ3VlJVaXd2dDNsMkJqaWZXU1JXajRja1RuRUNtd1F5XC9zRDB3UERoWU96d2N0Y0RxMVRnPT0iLCJtYWMiOiIwYTJlN2QzZjVlZjQ1ZmI0MWFiNjQ2MGE1NzQyY2Y0NDIxODM4YjMwYTVjMDBjZWRhYWUzNTE3MzU2MGQyMWIxIn0%3D; doutula_session=eyJpdiI6ImZmcTkrZFBTTW5KZmtzYjFTVlZDMGc9PSIsInZhbHVlIjoiaU5xSUxtNHN3M29HbTMxRnpjZWdCNENkdlBZWWRUcjV6NFE2YktUQ2tGOVFJenAzbFdtSHdxVDhEZjNcL3JhRHg1ZkpPSk00MmtkeWErUlgzT1lQSEJRPT0iLCJtYWMiOiJlMGRmZTNkMTMzZTE4MDEwNDUwMzUzNDM3M2EwNTZmY2MxOGUzOTBlNWEzNDM5YTliOThjOWZlZjMyN2FiYzdhIn0%3D'
    }
    respose = requests.get(url=url, headers=header).text
    data = etree.HTML(respose)
    root = data.xpath('//*[@id="pic-detail"]/div/div[3]/div[2]/ul/li/div/div/a')
    x = 0
    for q in root :

        name = q.xpath('.//p/text()')

        img_url = q.xpath('.//@data-original')
        fitst_suffox = os.path.splitext(str(img_url))[1]
        a = fitst_suffox[0:4]

        a_filename = name[0]+a
        print('准备下载第' + str(x) + '张图片，链接为' + str(img_url))
        r = requests.get(img_url[0])
        try:
            with open('image/'+a_filename, mode='wb') as fo:
                fo.write(r.content)
            print('下载第' + str(x) + '张图片成功')
            x = x + 1
        except Exception:
            print('error')






def down():
    for i in range(4, 8):
        url = 'http://www.doutula.com/photo/list/?page={}'.format(i)
        parse_page(url)


if __name__ == '__main__':
    # url = 'http://www.doutula.com/photo/list/?page=1'
    # parse_page(url)
    down()
    # num()


