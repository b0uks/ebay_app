from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from ebay_watchlist_class import *
import sys, glob, os, time
import parse_watchlist

watchlist_url = 'https://www.ebay.com/mye/myebay/watchlist?custom_list_id=WATCH_LIST&page=1&items_per_page=10'

def sel_driver():
    fp = webdriver.FirefoxProfile('/home/adam/firefox_profile')
    driver = webdriver.Firefox(fp)
    driver.get(watchlist_url)
    driver.maximize_window()
    return driver

def get_page_html(driver):
    watchlist_html = driver.page_source
    print('page url: ' + driver.current_url)
    return watchlist_html

def write_out_html(fname, wl_html):
    f = open(fname, "w")    # fname defined in watchlist class
    f.write(wl_html)
    f.close()

def get_next_page(web_driver):
    try:
        el = web_driver.find_element_by_xpath("//a[@class='pagination__next icon-link m-pagination__control']")
        print(el)
        time.sleep(2)
        el.click()
        time.sleep(2)

        return True             
    except:
        print("unable to find next page button")
        return False

def get_previous_page(web_driver):
    try:
        el = web_driver.find_element_by_xpath("//a[@class='pagination__previous icon-link m-pagination__control']")
        print(el)
        time.sleep(2)
        el.click()
        time.sleep(2)
        return True             
    except:
        print("unable to find prev page button")
        return False


def main_1(d):
    counter = 0
    html = get_page_html(d)
    write_out_html(fname + str(counter), html)

    while get_next_page(d):
        counter += 1
        html = get_page_html(d)
        write_out_html(fname + str(counter), html)

def main():
    d = sel_driver()
    counter = 0
    user_input(d)

    html = get_page_html(d)
    write_out_html(fname + str(counter), html)

    while get_next_page(d):
        counter += 1
        html = get_page_html(d)
        write_out_html(fname + str(counter), html)

    user_input(d)

def user_input(driver):
    for line in sys.stdin:
        if 'c' == line.rstrip():
            break
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
        if 'l' == line.rstrip():
            while(True):
                print("Looping")
            # remove all previous HTML
                for file in sorted(glob.glob(fname + "*")):
                    os.remove(file)
                    print("removed old files")
                time.sleep(5)
            # get new HTML
                main_1(driver)            
            # parse the HTML
                os.system('python3 parse_watchlist.py')
                x = 1
                t = x*60
                time.sleep(t)

            # go back to first watchlist page
                x = True
                while (x):
                    x = get_previous_page(driver)

        if 'n' == line.rstrip():                # "m-pagination__container"
            print("N")
            try:
                el = driver.find_element_by_xpath("//a[@class='pagination__next icon-link m-pagination__control']")
                print(el)
                time.sleep(5)
                el.click()
                f = open(fname, "w")    # fname defined in watchlist class
                f.write(watchlist_html)
                f.close()                
            except:
                print("unable to find next page button")


if __name__ == "__main__":
    main()