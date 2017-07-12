# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')


class QuanshuwangPipeline(object):

    def process_item(self, item, spider):
        if spider.name == 'title':
            self.file = open('%s.json' % item['page'], 'wb')
            output = json.dumps(dict(item), ensure_ascii=False, indent=2)
            self.file.write(output)
        elif spider.name == 'artcle':
            self.file = open('%s.json' % item['name'], 'wb')
            output = json.dumps(dict(item), ensure_ascii=False, indent=2)
            self.file.write(output)
        return item
