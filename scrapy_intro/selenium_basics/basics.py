from selenium import webdriver
from shutil import which


# which handles the path for us
chrome_path = which('chrome')
print(chrome_path, '<><>>')

# driver = webdriver.Chrome(executable_path=chrome_path)
# driver.get('https://duckduckgo.com')
