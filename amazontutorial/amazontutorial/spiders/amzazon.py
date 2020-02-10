# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazontutorialItem


class AmzazonSpider(scrapy.Spider):
    name = 'amzazon'
    allowed_domains = ['amazon.com']
    page_number = 2
    start_urls = ['https://www.amazon.com/s?k=last+30+days+books&i=stripbooks-intl-ship&crid=2FWMOUEENT482&sprefix=last+30+days%2Cstripbooks-intl-ship%2C382&ref=nb_sb_ss_i_2_12']

    def parse(self, response):
        items = AmazontutorialItem()

        product_name = response.css('.a-color-base.a-text-normal').css('::text').extract()
        product_author = response.css('.a-color-secondary .a-size-base:nth-child(2)').css('::text').extract()
        product_price = response.css('.a-spacing-top-small .a-price-whole').css('::text').extract()
        product_imgurl = response.css('.s-image::attr(src)').extract()

        items['product_name'] = product_name
        items['product_author'] = product_author
        items['product_imgurl'] = product_imgurl
        items['product_price'] = product_price

        yield items

        next_page = 'https://www.amazon.com/s?k=last+30+days+books&i=stripbooks-intl-ship&page=' + str(AmzazonSpider.page_number) + '&crid=8FWMOUEENT482&qid=1576791908&sprefix=last+30+days%2Cstripbooks-intl-ship%2C382&ref=sr_pg_3'
        if AmzazonSpider.page_number <=100:
            AmzazonSpider.page_number +=1
            yield response.follow(next_page,callback=self.parse())