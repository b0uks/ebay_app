from bs4 import BeautifulSoup
import datefinder
from csv import writer, reader
import pandas as pd
from ebay_watchlist_class import *
fname = "current_html"


fp = get_html_file()

myWatchlist = EbayWatchlist(fp)

# myWatchlist.find_titles()
myWatchlist.find_listings()




