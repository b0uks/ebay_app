from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import sys
import time, os


fp = webdriver.FirefoxProfile('/home/adam/firefox_profile')
driver = webdriver.Firefox(fp)
driver.get('https://www.google.com/search?channel=fs&client=ubuntu&q=hello')
driver.maximize_window()

element = driver.find_element_by_id("xjs")  #pagination__next icon-link m-pagination__control
print(element)
                        #style="display:block;margin-left:53px"

el = driver.find_element_by_xpath("//span[@class='SJajHc NVbCr']")
print(el)
time.sleep(1)
el.click()

print('execing')

os.system('python3 test_file.py')

#span class="SJajHc NVbCr"

