import requests
from bs4 import BeautifulSoup
import datefinder
from csv import writer, reader
import pandas as pd
from ebay_listing_class import *

fname = "c_html"

def get_html_file():
    with open(fname, "r") as f:
        return f.read()


class EbayWatchlist:

    def __init__(self, html_file):
        self.soup = BeautifulSoup(html_file, "html.parser")

    def find_listings(self):
        get_m_items = self.soup.find("div", class_="m-items")
        all_listings= get_m_items.findChildren("div", class_="m-item")
        for listing in all_listings:
            t = self.get_listing_title(listing)
            p = self.get_listing_price(listing)
            s = self.get_listing_shipping(listing)
            d = self.get_listing_end_date(listing)
            e = self.get_listing_ended(listing)
            n = self.get_listing_note(listing)

            currentListing = EbayListing(t, p, s, d, e, n)
            currentListing.show_important()
            currentListing.output_csv_format()
            # print(dir(shipping))

    def get_listing_note(self, listing):
        x = ""
        note = listing.find(class_="item-ebaynotes")
        if note:
            n = note.findChild(class_="DEFAULT")
            x = n.text
        return x

    def get_listing_title(self, listing):
        x = "No Title"
        title = listing.findChild(class_="hide") # get a dirty title
        if title and len(str(title.text)) > 3:
            x = title.text
        else:
            stuff = listing.findChild(class_="title")
            if stuff:
                title = stuff.find('span').next_element.next_element
                x = title
        return x

    def get_listing_price(self, listing):
        x = "No Price Found"
        price = listing.findChild(class_="BOLD") # dirty price
        if price:
            x = price.text
        return x

    def get_listing_shipping(self, listing):
        x = "N/A"
        shipping = listing.findChild(class_="info-shipping")
        if shipping:
            x = shipping.text
        return x    

    def get_listing_end_date(self, listing):
        x = "N/A"
        end_date = listing.find(class_="info-timer")
        if end_date:
            time = end_date.findChild(class_="DEFAULT")
            if time:
                x = time.text
        else:
            end_date = listing.find(class_="info-time")
            if end_date:
                time = end_date.findChild(class_="BOLD")
                if time:
                    x = time.text
                    
        return x

    def get_listing_ended(self, listing):
        x = "LIVE"
        ended = listing.findChild(class_="NEGATIVE")
        if ended:
            x = ended.text
        return x