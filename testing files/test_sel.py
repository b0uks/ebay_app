from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from ebay_watchlist_class import *

c_options = webdriver.ChromeOptions()
c_options.add_argument("user-data-dir=/home/adam/snap/chromium/common/chromium/Profile 1")
c_driver = webdriver.Chrome(executable_path='/snap/chromium/1568/usr/lib/chromium-browser/chrome', options=c_options)
c_driver.get('google.com')
