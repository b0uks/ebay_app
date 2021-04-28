import requests
from bs4 import BeautifulSoup
import datefinder
from csv import writer, reader
import pandas as pd

fname = "c_html"

def get_html_file():
    with open(fname, "r") as f:
        return f.read()


class EbayWatchlist:

    def __init__(self, html_file):
        self.soup = BeautifulSoup(html_file, "html.parser")


    def find_titles(self):
        find_title = self.soup.find_all("a", class_="title")

        for item in find_title:
            for elem in item:
                print(elem)   # ISOLATES THE NAME FROM ALL THE GAR


    def get_listing_title(self, listing):
        title = listing.findChild(class_="hide") # get a dirty title
        print(title.text)

    def get_listing_price(self, listing):
        price = listing.findChild(class_="BOLD") # dirty price
        print(price.text)

    def get_listing_shipping(self, listing):
        shipping = listing.findChild(class_="info-shipping")
        if shipping:
            print(shipping.text)
        else:
            print("N/A")
    
    def get_listing_end_date(self, listing):
        end_date = listing.find(class_="info-timer")
        if end_date:
            time = end_date.findChild(class_="DEFAULT")
            if time:
                print(time.text)
                
        else:
            end_date = listing.find(class_="info-time")
            if end_date:
                time = end_date.findChild(class_="BOLD")
                if time:
                    print(time.text)
                    
            print("N/A")

    def get_listing_ended(self, listing):
        ended = listing.findChild(class_="NEGATIVE")
        if ended:
            print(ended.text)
        else:
            print("LIVE")

    def find_listings(self):
        i = 0
        get_mitems = self.soup.find("div", class_="m-items")
        all_listings= get_mitems.findChildren("div", class_="m-item")
        for listing in all_listings:
            i += 1
            self.get_listing_title(listing)

            self.get_listing_price(listing)

            self.get_listing_shipping(listing)
            
            self.get_listing_end_date(listing)

            self.get_listing_ended(listing)
            # print(dir(shipping))
            # break
            print('\n')