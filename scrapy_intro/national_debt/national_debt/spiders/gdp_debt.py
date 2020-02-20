# -*- coding: utf-8 -*-
import scrapy


class GdpDebtSpider(scrapy.Spider):
    name = 'gdp_debt'
    allowed_domains = ['http://worldpopulationreview.com/']
    start_urls = [
        'http://worldpopulationreview.com/countries/countries-by-national-debt/']

    def parse(self, response):
        debt_info = response.xpath("//table//tr")
        for data in debt_info:
            name = data.xpath(".//a/text()").get()
            debt_ratio = data.xpath(".//td[2]/text()").get()
            population = data.xpath(".//td[3]/text()").get()

            yield {
                'name': name,
                'debt_ratio': debt_ratio,
                'population': population
            }
