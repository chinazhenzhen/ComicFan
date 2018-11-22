# -*- coding: utf-8 -*-
import scrapy

from spider_module.items import CmadItem

class CmadSpiderSpider(scrapy.Spider):
    name = 'cmad_spider'
    allowed_domains = ['www.cartoonmad.com']
    start_urls = ['https://www.cartoonmad.com/comic/4085.html']

    def parse(self, response):
        item = CmadItem()
        # title 漫画的标题，desc 漫画的描述 url_set 漫画分级列表的链接
        item['m_title'] = response.css('a[href="/comic/4085.html"]::text').extract()[-1]
        item['m_desc'] = response.css('td[style="font-size:11pt;"]::text').extract()[1]
        #url_set = responst.css('fieldset[id="info"] a[target="_blank"]::attr(href)').extract()
        yield item
