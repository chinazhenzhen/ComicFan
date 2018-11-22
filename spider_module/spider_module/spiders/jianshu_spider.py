# -*- coding: utf-8 -*-
import scrapy


class JianshuSpiderSpider(scrapy.Spider):
    name = 'jianshu_spider'
    allowed_domains = ['www.jianshu.com']
    start_urls = ['http://www.jianshu.com/']

    def parse(self, response):
        pass
