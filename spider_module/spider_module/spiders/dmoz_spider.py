# -*- coding: utf-8 -*-


# 文件通过系统命令进行创建
# scrapy genspider dmoz_spider  dmoz.com
# name: 用于区别spider，名字必须是唯一的，为不同的spider设计不同的名字
# start_urls 包含了spider再启动时进行爬取的url列表
#  parse sipder的一个方法，每个初始url完成下载后生成的response对象会作为唯一的参数传递给该函数。该函数负责解析数据、返回数据、或者生成需要进一步处理的url的request对象
# 一般来说，parse中会用到items中的类，spider会将爬取的数据以item对象返回，得到爬取的数据
import scrapy

from spider_module.items import DmozItem


class DmozSpiderSpider(scrapy.Spider):
    name = 'dmoz_spider'
    allowed_domains = ['dmoz.org']
    start_urls = [
 		"http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/",
	]

    def parse(self, response):
        for sel in response.xpath('//ul/li'):
            item = DmozItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            yield item
