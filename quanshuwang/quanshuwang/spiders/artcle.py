# -*- coding: utf-8 -*-
import scrapy
import os
import sys
import json
from quanshuwang.items import ArtcleItem
reload(sys)
sys.setdefaultencoding('utf8')

item=ArtcleItem()
class ArtcleSpider(scrapy.Spider):
    name = 'artcle'
    allowed_domains = ['quanshuwang.com']
    start_urls = []
    ListAll = os.listdir(os.getcwd())
    item['content']=[]
    def is_json(self):
        return self[-5:] == '.json'
    List = filter(is_json, ListAll)
    for l in List[:2]:#删掉[:2]即获取所有主题
        file=open(l)
        start_urls.append('http://www.quanshuwang.com' + json.load(file)['src'][0])
        #下面为获取主题内所有文章
        #start_urls.append('http://www.quanshuwang.com' + l  for l in json.load(file)['src'])

    def parse(self, response):
        item['name']=response.xpath('//*[@id="chapter"]/div[2]/div[*]/strong/text()').extract()[0]
        item['chapter']=response.xpath('//*[@id="chapter"]/div[2]/div[2]/ul/div[2]/li[*]/a/text()').extract()
        item['chapterurl'] = response.xpath('//*[@id="chapter"]/div[2]/div[2]/ul/div[2]/li[*]/a/@href').extract()

        for i in item['chapterurl'][:10]:#删掉[:10]即获取所有章节
            next_url = response.url[:-10] + str(i)
            yield scrapy.Request(url=next_url, callback=self.contentPage)

    def contentPage(self,response):
        content=''
        for l in response.xpath('//*[@id="content"]/text()').extract():
            content=content+l.encode('utf8')
        item['content'].append(content)
        yield item