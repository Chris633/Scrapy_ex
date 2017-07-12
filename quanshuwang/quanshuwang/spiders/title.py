# -*- coding: utf-8 -*-
import scrapy
from quanshuwang.items import TittleItem
import sys
reload(sys)
sys.setdefaultencoding('utf8')


class TitleSpider(scrapy.Spider):
    name = 'title'
    allowed_domains = ['quanshuwang.com']

    start_urls = ['http://www.quanshuwang.com/map/%s.html' % x for x in '12345']

    def parse(self, response):
        body = response.xpath('/html/body')
        item = TittleItem()
        item['title'] = body.xpath('a/text()').extract()
        item['src'] = body.xpath('a/@href').extract()
        item['page'] = response.url[-6] + body.xpath('div[2]/a[%s]/text()' % response.url[-6]).extract()[0]
        yield item
