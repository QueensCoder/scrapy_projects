# -*- coding: utf-8 -*-
import scrapy


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info']
    start_urls = [
        'https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        countries = response.xpath('//td/a')

        for i in countries:
            # ./ because we are not using xpath agaisnt the response obj anymore
            name = i.xpath(".//text()").get()
            link = i.xpath(".//@href").get()

            # to deal with relative urls

            # manually concat url
            # absolute_url = f"https://www.worldometers.info{link}"

            # url join is cleaner way to concat url with links
            # absolute_url = response.urljoin(link)

            # use with string concat methods above
            # yield scrapy.Request(url=absolute_url)

            # do not need concat methods above when using response.follow
            yield response.follow(url=link)
