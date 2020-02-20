# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestBooksSpider(CrawlSpider):
    name = 'best_books'

    # www before allowed domain caused error
    # learn differences between http and https in scrapy
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com']

    rules = (
        Rule(LinkExtractor(
            restrict_xpaths=r"//article[@class='product_pod']/h3/a"), callback='parse_item', follow=True),
        Rule(LinkExtractor(
            restrict_xpaths=r"//li[@class='next']/a")
        )
    )

    def parse_item(self, response):
        yield {
            'book_name': response.xpath('//h1/text()').get(),
            'price': response.xpath('//p[@class="price_color"]/text()').get(),
            # 'user-agent': response.request.headers['User-Agent']
        }
