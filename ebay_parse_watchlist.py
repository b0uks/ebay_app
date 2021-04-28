from bs4 import BeautifulSoup
import datefinder
from csv import writer, reader
import pandas as pd
from ebay_watchlist_class import *
fname = "current_html"

with open(fname) as fp:
    soup = BeautifulSoup(fp, "html.parser")
    find_title = soup.find_all("a", class_="title")

    for item in find_title:
        for elem in item:
            print(elem)   # ISOLATES THE NAME FROM ALL THE GAR
