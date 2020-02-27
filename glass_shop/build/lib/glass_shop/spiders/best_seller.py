# -*- coding: utf-8 -*-
import scrapy


class BestSellerSpider(scrapy.Spider):
    name = 'best_seller'

    # https infront of glassesshop.com caussed the spider to not scrape
    # after initial scrap, allowed domains should only contain site without full http address
    allowed_domains = ['www.glassesshop.com']
    start_urls = ['https://www.glassesshop.com/bestsellers']

    def parse(self, response):
        for raw in response.xpath("//div[@class='prlist row']/div"):

            # get img and url
            prod = raw.xpath(
                ".//div[@class='pimg default-image-front']/a")
            href = prod.xpath(".//@href").get()
            img = prod.xpath(".//img/@src").get()

            # get price and product name
            name = raw.xpath(".//div[@class='row']/p/a/text()").get()
            price = raw.xpath(
                ".//div[@class='row']//div/span/text()").get()

            yield {
                "url": href,
                "img_url": img,
                "name": name,
                "price": price,
                # using custom user agent that is passed in the settings.py file
                "user-agent": response.request.headers['User-Agent']
            }

        next_page = response.xpath(
            "//ul[@class='pagination']/li[last()]/a/@href").get()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)
