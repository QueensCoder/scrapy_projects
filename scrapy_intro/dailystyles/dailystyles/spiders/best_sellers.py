# -*- coding: utf-8 -*-
import scrapy


class BestSellersSpider(scrapy.Spider):
    name = 'best_sellers'
    allowed_domains = ['www.mydailystyles.com']
    start_urls = ['https://www.mydailystyles.com/collections/best-selling']

    def parse(self, response):
        for prod in response.xpath("//div[@class='grid-uniform']/div/div/a"):
            price = str(prod.xpath(
                ".//span/span[@class='grid-product__price']/text()"))
            yield {
                'title': prod.xpath(".//span/text()").get(),
                'url': response.urljoin(prod.xpath(".//@href").get()),
                'price': price[price.find('$'):]
            }
