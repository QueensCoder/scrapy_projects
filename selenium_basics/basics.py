from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from shutil import which

# allows you to perform a headless scrape (does not open the browser)
chrome_options = Options()
chrome_options.add_argument('--headless')

# which handles the path for us
# had to add chrome driver to path ---will need to update if new version of chrome used
chrome_path = which('chromedriver')


driver = webdriver.Chrome(executable_path=chrome_path, options=chrome_options)
driver.get('https://duckduckgo.com')

search = driver.find_element_by_id('search_form_input_homepage')
search.send_keys('My User Agent')

# click search btn by first finding button by id
# btn = driver.find_element_by_id("search_button_homepage")
# btn.click()

# USE KEYS.ENTER TO PEFORM SEARCH
search.send_keys(Keys.ENTER)

# print page source to terminal
print(driver.page_source)

# make sure to close driver
driver.close()
