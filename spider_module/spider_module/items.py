# -*- coding: utf-8 -*-



#保存数据的容器，将我们所需要的数据进行格式化。
#相当于是保存数据的容器




# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class CmadItem(scrapy.Item):

    m_title = scrapy.Field()
    m_desc = scrapy.Field()


class DmozItem(scrapy.Item):

	title = scrapy.Field()
	link = scrapy.Field()
	desc = scrapy.Field()


class SpiderModuleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
