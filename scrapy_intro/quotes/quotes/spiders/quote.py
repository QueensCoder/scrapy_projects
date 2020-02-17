# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest


class QuoteSpider(scrapy.Spider):
    name = 'quote'
    allowed_domains = ['quotes.toscrape.com/js']

    script = '''
    function main(splash, args)
        assert(splash:go(args.url))
        assert(splash:wait(0.5))
	    splash:html()
    end
    '''

    def start_requests(self):
        yield SplashRequest(url='http://quotes.toscrape.com/js', callback=self.parse, endpoint='execute', args={'lua_source': self.script})

    def parse(self, response):
        quotes = response.xpath("//div[@class='container']/div")
        print(quotes, 'here<><><><><><>')
        print(len(quotes), '<><><><>')
        # for quote in quotes:
        #     yield {
        #         'text': quote.xpath('.//span[1]/text()').get(),
        #         'author': quote.xpath('.//span[2]/small/text()').get()
        #     }
