# -*- coding: utf-8 -*-
import scrapy
from scrapy_selenium import SeleniumRequest


class ExampleSpider(scrapy.Spider):
    name = 'example'
    url = 'https://duckduckgo.com/'
    # selenium will be sending requests no longer need allowed and start urls

    def start_requests(self):
        yield SeleniumRequest(url=self.url,
                              wait_time=3,
                              screenshot=True,
                              callback=self.parse
                              )

    def parse(self, response):
        # get screenshot from selenium
        img = response.meta['screenshot']

        with open('screenshot.png', 'wb') as f:
            f.write(img)
