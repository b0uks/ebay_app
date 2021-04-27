from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
fp = webdriver.FirefoxProfile('/home/adam/firefox_profile')
driver = webdriver.Firefox(fp)
driver.get('https://www.ebay.com/mye/myebay/watchlist')
driver.maximize_window()

element = WebDriverWait(driver, 20)

# email_address = driver.find_element_by_xpath("//span/input[@placeholder='Email or username']")
# password = driver.find_element_by_xpath("//span/input[@placeholder='Password']")
