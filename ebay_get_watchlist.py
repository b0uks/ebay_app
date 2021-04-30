from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from ebay_watchlist_class import *
import sys

# driver = webdriver.Chrome()
# c_options = webdriver.ChromeOptions()
# c_options.add_argument("user-data-dir=/home/adam/snap/chromium/common/chromium/Profile 1")
# c_driver = webdriver.Chrome(executable_path='/snap/chromium/1568/usr/lib/chromium-browser/chrome', chrome_options=c_options)
# c_driver.get('google.com')

fp = webdriver.FirefoxProfile('/home/adam/firefox_profile')
driver = webdriver.Firefox(fp)
driver.get('https://www.ebay.com/mye/myebay/watchlist')
driver.maximize_window()

watchlist_html = driver.page_source



f = open(fname, "w")    # fname defined in watchlist class
f.write(watchlist_html)
f.close()

for line in sys.stdin:
    if 'q' == line.rstrip():
        driver.close()
        break
    if 'r' == line.rstrip():
        driver.refresh()
    if 't' == line.rstrip():
        watchlist_html = driver.page_source
        print(driver.current_url)
        f = open(fname, "w")    # fname defined in watchlist class
        f.write(watchlist_html)
        f.close()

# print(watchlist_html)




