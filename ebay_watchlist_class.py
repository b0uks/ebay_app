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

    def find_listings(self):
        get_mitems = self.soup.find("div", class_="m-items")
        all_listings= get_mitems.findChildren("div", class_="m-item")
        for listing in all_listings:
            title = listing.findChild(class_="hide") # get a dirty title
            print(title.text)
            price = listing.findChild(class_="BOLD") # dirty price
            print(price.text)
            shipping = listing.findChild(class_="info-shipping")
            if shipping:
                print(shipping.text)
            end_date = listing.findChild(class_="DEFAULT")
            if end_date:
                print(end_date.text)
            # print(dir(shipping))
            # break
            print('\n')
