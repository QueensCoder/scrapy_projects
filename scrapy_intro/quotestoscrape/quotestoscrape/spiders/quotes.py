# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    script = '''
    function main(splash, args)
        assert(splash:go(args.url))
        assert(splash:wait(0.5))
	    return splash:html()
    end
    '''

    def start_requests(self):
        yield SplashRequest(url='http://quotes.toscrape.com/js/', callback=self.parse, endpoint='execute', args={'lua_source': self.script})

    def parse(self, response):
        quotes = response.xpath("//div[@class='quote']")

        for quote in quotes:
            yield {
                "text": quote.xpath('./span[1]/text()').get(),
                "author": quote.xpath('./span[2]/small/text()').get(),
                # get all allows you to get an array of all the elements data
                "tags": quote.xpath('./div/a/text()').getall()
            }

        next = response.expath
