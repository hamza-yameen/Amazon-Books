# -*- coding: utf-8 -*-
import scrapy


class AmzazonSpider(scrapy.Spider):
    name = 'amzazon'
    allowed_domains = ['amazon.com']
    start_urls = ['http://amazon.com/']

    def parse(self, response):
        pass
