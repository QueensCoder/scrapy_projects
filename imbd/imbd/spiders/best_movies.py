# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestMoviesSpider(CrawlSpider):
    name = 'best_movies'
    allowed_domains = ['imdb.com']

    # do not need start urls when you overwrite start requests method and set request url to desired url
    # start_urls = [
    #     '']

# dummy user agent
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'

    # link extractor takes out the link from the xpath provided and passed that link to the callback method
    rules = (
        Rule(LinkExtractor(restrict_xpaths=r"//h3[@class='lister-item-header']/a"),
             callback='parse_item', follow=True, process_request='set_user_agent'),
        Rule(LinkExtractor(
            restrict_xpaths="(//a[@class='lister-page-next next-page'])[1]"), process_request='set_user_agent')
        # , after rule is required or spider will crash if one rule
        # rules are invoked in the order that they are written in
        # first get all the links from the first page, then use pagination
        # for second rule the default value for follow is true
        # each time a new page is visited the first rule will be called again so no need to use call back of parse_item in second rule
    )

    def start_requests(self):
        yield scrapy.Request(url='https://www.imdb.com/search/title/?groups=top_250&sort=user_rating', headers={
            'User-Agent': self.user_agent
        })

    def set_user_agent(self, request):
        request.headers['User-Agent'] = self.user_agent
        return request

    def parse_item(self, response):
        yield {
            'title': response.xpath("//div[@class='title_wrapper']/h1/text()").get(),
            'year': response.xpath("//span[@id='titleYear']/a/text()").get(),

            # normalize-space removes whitespace and \n inside of output text
            'duration': response.xpath("normalize-space(//div[@class='subtext']/time/text())").get(),
            'rating': response.xpath("//div[@class='ratingValue']/strong/span/text()").get(),
            'movie_url': response.xpath("//div[@class='title_wrapper']/h1/text()").get(),
            'genre': response.xpath("//div[@class='subtext']/a[1]/text()").get(),
            'movie_url': response.url,
            'user-agent': response.request.headers['User-Agent']
        }
