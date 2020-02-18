# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']
    absolute_url = 'http://quotes.toscrape.com/js/'

    script = '''
    function main(splash, args)
        assert(splash:go(args.url))
        assert(splash:wait(0.5))
	    return splash:html()
    end
    '''

    def start_requests(self):
        yield SplashRequest(url=self.absolute_url, callback=self.parse, endpoint='execute', args={'lua_source': self.script})

    def parse(self, response):
        quotes = response.xpath("//div[@class='quote']")

        for quote in quotes:
            yield {
                "text": quote.xpath('./span[1]/text()').get(),
                "author": quote.xpath('./span[2]/small/text()').get(),
                # get all allows you to get an array of all the elements data
                "tags": quote.xpath('./div/a/text()').getall()
            }

        next_page = response.xpath("//li[@class='next']/a/@href").get()
        if next_page:
            # if there is a next page concat the url with the next page
            absolute_url = f'http://quotes.toscrape.com{next_page}'

            # need to use splashReq again because the other pages require the js to be loaded in order to scrape them
            # lua script needs to be used on each page
            yield SplashRequest(url=absolute_url, callback=self.parse, endpoint='execute', args={'lua_source': self.script})
