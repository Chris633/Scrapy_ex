# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TittleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Fi9eld()
    title=scrapy.Field()
    src=scrapy.Field()
    page=scrapy.Field()
    pass

class ArtcleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Fi9eld()
    chapter=scrapy.Field()
    chapterurl=scrapy.Field()
    content=scrapy.Field()
    name=scrapy.Field()
    pass
