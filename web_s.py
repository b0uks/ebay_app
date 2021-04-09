#This will not run on online IDE
import requests
from ebay_class import EbayListing
from ebay_class import timezone_info
from bs4 import BeautifulSoup
import re,datetime
import datefinder
from dateutil.parser import parse

listing = EbayListing()

def printValues():
    for attr, val in listing.__dict__.items():
        print(attr + ": " + str(val))

def getStartCost(string):
    priceStart = string.find('$')
    new_string = string[priceStart:]            # create new string from $ to end
    priceEnd = new_string.find('<')            # find first non dollar sign value
    cropped_price = new_string[1:priceEnd]
    # print("price:" + cropped_price)   
    return cropped_price

def setUpSoup(listing, URL):
    if listing:
        listing.url = URL
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
    return soup
# print(soup.prettify())

def findTitle(soup):
    title = soup.find_all('title')
    print(title)
    string_title = str(title)
    start_title = string_title.find('>')
    end_title = string_title.find('|')
    clipped_title = string_title[start_title+1:end_title]
    # print(clipped_title)
    return clipped_title


def findPrice(soup):
    val = soup.find_all("span", class_="notranslate")
    return getStartCost(str(val))

def findQuantity(soup):
    qty = soup.find_all("span", id="qtySubTxt")
    qty_s = str(qty)
    for i in qty_s:
        if i.isdigit():
            # print("quant:" + str(i))
            return i
    return -1
    # print(clip)

def findShipping(soup):
    ship = soup.find_all("span", id="fshippingCost")
    # print(ship)
    ship_s = str(ship)
    free = ship_s.find("FREE")
    if free == -1:
        return getStartCost(str(ship))
    return 0

def lastUpdate(soup):
    last_update = soup.find_all("div", class_="vi-desc-revHistory")
    lu_s = str(last_update)
    # print(lu_s)

    for zone in timezone_info:
        index = lu_s.find(zone)
        if (index > 0):
            f_time = datefinder.find_dates(lu_s[:index], strict=False)
            for f in f_time:
                return str(f)
    return "unable to find time"

def main():

    list_listings = [
        "https://www.ebay.com/itm/Sports-Illustrated-COMMEMORATIVE-2019-New-England-Patriots-Super-Bowl-CHAMPIONS/163526245987?_trkparms=aid%3D1110006%26algo%3DHOMESPLICE.SIM%26ao%3D1%26asc%3D20201210111314%26meid%3Da65c0b3daa6e44e0986f2204c4a2b96d%26pid%3D101195%26rk%3D3%26rkt%3D12%26mehot%3Dpf%26sd%3D203300682401%26itm%3D163526245987%26pmt%3D1%26noa%3D0%26pg%3D2047675%26algv%3DSimplAMLv9PairwiseUnbiasedWeb&_trksid=p2047675.c101195.m1851",
        "https://www.ebay.com/itm/Sports-Illustrated-Commemorative-Miami-Heat-2013-Champions-Lebron-James-NEW/203300682401?hash=item2f55aa3aa1:g:gLQAAOSw8bhgSA7p",
        "https://www.ebay.com/itm/Sports-Illustrated-Philadelphia-Eagles-2018-Super-Bowl-Champions-Nick-Foles/163487866511?_trkparms=aid%3D1110006%26algo%3DHOMESPLICE.SIM%26ao%3D1%26asc%3D20201210111314%26meid%3D2a03c6dc4cb5404f9312d8249157bd8d%26pid%3D101195%26rk%3D5%26rkt%3D12%26mehot%3Dpf%26sd%3D163526245987%26itm%3D163487866511%26pmt%3D1%26noa%3D0%26pg%3D2047675%26algv%3DSimplAMLv9PairwiseUnbiasedWeb&_trksid=p2047675.c101195.m1851"
    ]

    sold_listing = "https://www.ebay.com/itm/2-Roy-DOC-Halladay-Philadelphia-Phillies-UNSIGNED-Sports-Illustrated-SI-NO-LABEL/232866473309?hash=item3637ec655d:g:hZAAAOSw0JFbXMei"
    url = sold_listing
    # for url in sold_listing: 
    soup = setUpSoup(listing, url)
    listing.title = findTitle(soup)
    listing.price = findPrice(soup)
    listing.quant = findQuantity(soup)
    listing.shipping = findShipping(soup)
    listing.lastUpdate = lastUpdate(soup)

    printValues()


if __name__ == "__main__":
    main()


