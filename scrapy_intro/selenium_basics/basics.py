from selenium import webdriver
from shutil import which


# which handles the path for us
# not working atm
# chrome_path = which('chromedriver')


chrome_path = which('chromedriver')


driver = webdriver.Chrome(executable_path=chrome_path)
driver.get('https://duckduckgo.com')
