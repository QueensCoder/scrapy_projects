# -*- coding: utf-8 -*-
import scrapy


class BestSellersSpider(scrapy.Spider):
    name = 'best_sellers'
    allowed_domains = ['www.mydailystyles.com']

    # overwrote start requests so no longer neeed to add start urls
    # start_urls = ['https://www.mydailystyles.com/collections/best-selling']

#  cleans price string of white space and \\n
    def price_cleaner(self, price):
        price = price[price.find('$'):]
        return price[:price.find('\\n'):]

# overwrite astart requests method
# alternative solution is to change user agent in settings.py and user user-agent genrator
    def start_requests(self):
        # crawl with user agent that is not scrapy's default
        # this is done to prevent web scraper blockers
        # look into using generated user agent
        yield scrapy.Request(url="https://www.mydailystyles.com/collections/best-selling", callback=self.parse, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"})

    def parse(self, response):
        for prod in response.xpath("//div[@class='grid-uniform']/div/div/a"):
            # turn price into str and extract polluted text
            price = str(prod.xpath(
                ".//span/span[@class='grid-product__price']//text()").extract())
            yield {
                'title': prod.xpath(".//span/text()").get(),
                'url': response.urljoin(prod.xpath(".//@href").get()),
                'price': self.price_cleaner(price),
                "User-Agent": response.request.headers['User-Agent']
            }

        # not all sites handle paginagnation with next button
        next_page = response.xpath("//span[@class='next']/a/@href").get()

        if next_page:
            # change relative path to absolute path
            next_url = response.urljoin(next_page)
            # recursively call parse again on next page to scrapy all products
            # and see if there is another page to scrap
            yield scrapy.Request(url=next_url, callback=self.parse,  headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"})
