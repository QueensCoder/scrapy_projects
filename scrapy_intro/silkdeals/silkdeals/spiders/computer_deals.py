# -*- coding: utf-8 -*-
import scrapy
from scrapy_selenium import SeleniumRequest


class ComputerDealsSpider(scrapy.Spider):
    name = 'computer_deals'

    def start_requests(self):
        yield SeleniumRequest(
            url='https://slickdeals.net/computer-deals/',
            wait_time=3,
            screenshot=True,
            callback=self.parse
        )

    def parse(self, response):
        products = response.xpath(
            "//ul[@class='dealTiles categoryGridDeals']/li")

        for prod in products:
            yield {
                'name': prod.xpath(".//a[@class='itemTitle']/text()").get(),
                'link': prod.xpath(".//a[@class='itemTitle']/@href").get(),
                'store': prod.xpath("normalize-space(.//span[@class='itemStore']/text())").get().strip(),
                'price': prod.xpath("normalize-space(.//div[@class='itemPrice  wide ']/text())").get()
            }
