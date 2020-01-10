# -*- coding: utf-8 -*-
import scrapy


class BestSellerSpider(scrapy.Spider):
    name = 'best_seller'
    allowed_domains = ['https://www.glassesshop.com']
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
                "price": price
            }

        next_page = response.xpath("//a[@class='page-link']/@aria-label")
        # if next_page:
