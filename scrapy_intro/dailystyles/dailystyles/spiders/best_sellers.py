# -*- coding: utf-8 -*-
import scrapy


class BestSellersSpider(scrapy.Spider):
    name = 'best_sellers'
    allowed_domains = ['www.mydailystyles.com']
    start_urls = ['https://www.mydailystyles.com/collections/best-selling']

#  cleans price string of white space and \\n
    def price_cleaner(self, price):
        price = price[price.find('$'):]
        return price[:price.find('\\n'):]

    def parse(self, response):
        for prod in response.xpath("//div[@class='grid-uniform']/div/div/a"):
            # turn price into str and extract polluted text
            price = str(prod.xpath(
                ".//span/span[@class='grid-product__price']//text()").extract())
            yield {
                'title': prod.xpath(".//span/text()").get(),
                'url': response.urljoin(prod.xpath(".//@href").get()),
                'price': self.price_cleaner(price)
            }

        # not all sites handle paginagnation with next button
        next_page = response.xpath("//span[@class='next']/a/@href").get()

        if next_page:
            # change relative path to absolute path
            next_url = response.urljoin(next_page)
            # recursively call parse again on next page to scrapy all products
            # and see if there is another page to scrap
            yield scrapy.Request(url=next_url, callback=self.parse)
