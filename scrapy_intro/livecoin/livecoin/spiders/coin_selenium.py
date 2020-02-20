# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from scrapy.selector import Selector
from shutil import which


class CoinSpiderSelenium(scrapy.Spider):
    name = 'coin_selenium'
    allowed_domains = ['www.livecoin.net/en']
    start_urls = ['https://www.livecoin.net/en']

    # inside contructor set up selenium
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")

        chrome_path = which('chromedriver')

        driver = webdriver.Chrome(
            executable_path=chrome_path, options=chrome_options)

        # ser window to maximum size
        driver.set_window_size(1920, 1080)
        driver.get('https://www.livecoin.net/en')

        rur_tab = driver.find_elements_by_class_name('filterPanelItem___2z5Gb')
        rur_tab[4].click()

        # add html to as string to html property
        self.html = driver.page_source
        driver.close()

    def parse(self, response):
        # instead of using response from scrapy we take the html stored in the class.html property
        # then change the self.html to selector so we can use xpath on it to find the information we need
        resp = Selector(text=self.html)
        for currency in resp.xpath("//div[contains(@class,'ReactVirtualized__Table__row tableRow___3EtiS ')]"):
            yield {
                'currency_pair': currency.xpath(".//div[1]/div/text()").get(),
                'volume(24h)': currency.xpath(".//div[2]/span/text()").get()
            }
