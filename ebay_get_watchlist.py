from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from ebay_watchlist_class import *

# driver = webdriver.Chrome()
fp = webdriver.FirefoxProfile('/home/adam/firefox_profile')
driver = webdriver.Firefox(fp)
driver.get('https://www.ebay.com/mye/myebay/watchlist')
driver.maximize_window()

watchlist_html = driver.page_source



f = open(fname, "w")    # fname defined in watchlist class
f.write(watchlist_html)
f.close()



# print(watchlist_html)




