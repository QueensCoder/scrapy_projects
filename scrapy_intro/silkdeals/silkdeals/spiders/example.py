# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy_selenium import SeleniumRequest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


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
        # img = response.meta['screenshot']

        # save screen shot
        # with open('screenshot.png', 'wb') as f:
        #     f.write(img)

        driver = response.meta['driver']

        search_input = driver.find_element_by_xpath(
            "//input[@id='search_form_input_homepage']")

        search_input.send_keys("Hello world")

        search_input.send_keys(Keys.ENTER)

        # response in parse will not provide html
        # need to get html text from driver and then turn it into a selector
        # use scrapy and selenium together
        html = driver.page_source
        response_obj = Selector(text=html)

        # use screen shot to show before and after
        # driver.save_screenshot('after_ENTER.png')

        links = response_obj.xpath("//div[@class='result__extras__url']/a")

        for link in links:
            yield {
                'url': link.xpath('.//@href').get()
            }
