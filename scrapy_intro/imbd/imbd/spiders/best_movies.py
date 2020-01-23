# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestMoviesSpider(CrawlSpider):
    name = 'best_movies'
    allowed_domains = ['imdb.com']
    start_urls = [
        'https://www.imdb.com/search/title/?groups=top_250&sort=user_rating']

    # link extractor takes out the link from the xpath provided and passed that link to the callback method
    rules = (
        Rule(LinkExtractor(restrict_xpaths=r"//h3[@class='lister-item-header']/a"),
             callback='parse_item', follow=True),
        Rule(LinkExtractor(
            restrict_xpaths="(//a[@class='lister-page-next next-page'])[1]"))
        # , after rule is required or spider will crash if one rule
        # rules are invoked in the order that they are written in
        # first get all the links from the first page, then use pagination
        # for second rule the default value for follow is true
        # each time a new page is visited the first rule will be called again so no need to use call back of parse_item in second rule
    )

    def parse_item(self, response):
        yield {
            'title': response.xpath("//div[@class='title_wrapper']/h1/text()").get(),
            'year': response.xpath("//span[@id='titleYear']/a/text()").get(),

            # normalize-space removes whitespace and \n inside of output text
            'duration': response.xpath("normalize-space(//div[@class='subtext']/time/text())").get(),
            'rating': response.xpath("//div[@class='ratingValue']/strong/span/text()").get(),
            'movie_url': response.xpath("//div[@class='title_wrapper']/h1/text()").get(),
            'genre': response.xpath("//div[@class='subtext']/a[1]/text()").get(),
            'movie_url': response.url


        }
