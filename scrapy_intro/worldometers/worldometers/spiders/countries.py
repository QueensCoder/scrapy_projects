# -*- coding: utf-8 -*-
import scrapy
import logging


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info']
    start_urls = [
        'https://www.worldometers.info/world-population/population-by-country/']

    # iterate over all countries on html
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
            yield response.follow(url=link, callback=self.parse_country, meta={'country_name': name})
            # meta allows us to pass the country name from method to method

    # for each country get the year and population data
    def parse_country(self, response):

        # get name from the response
        name = response.request.meta['country_name']

        rows = response.xpath(
            "(//table[@class='table table-striped table-bordered table-hover table-condensed table-list'])[1]/tbody")
        for row in rows:
            year = row.xpath(".//td[1]/text()").get()
            population = row.xpath(".//td[2]/strong/text()").get()

            yield {
                'country_name': name,
                'year': year,
                'population': population
            }
