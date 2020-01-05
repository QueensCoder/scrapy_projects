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
            absolute_url = f"https://www.worldometers.info{link}"
            yield scrapy.Request(url=absolute_url)
