from selenium import webdriver
from shutil import which


# which handles the path for us
# had to add chrome driver to path ---will need to update if new version of chrome used
chrome_path = which('chromedriver')


driver = webdriver.Chrome(executable_path=chrome_path)
driver.get('https://duckduckgo.com')

search = driver.find_element_by_id('search_form_input_homepage')
search.send_keys('My User Agent')

btn = driver.find_element_by_id("search_button_homepage")
btn.click()
