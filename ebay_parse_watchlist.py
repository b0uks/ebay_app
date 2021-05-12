from bs4 import BeautifulSoup
import datefinder
from csv import writer, reader
import pandas as pd
from ebay_watchlist_class import *


html = get_html_file()



myWatchlist = EbayWatchlist(html, "847j.csv")

for item in myWatchlist.listings:
    master_list.append(item)


old_watchlist_entries_list = myWatchlist.get_csv_file_listings()
old_set = set()
for listing in old_watchlist_entries_list:
    old_set.add( (listing.title, listing.ended) )

myWatchlist.find_listings()
current_watchlist_enties = myWatchlist.listings
new_set = set()
for listing in current_watchlist_enties:
    new_set.add( (listing.title, listing.ended) )

difference = new_set.difference(old_set)

if False:
    update_status = ""
    for title, ended in difference:
        update_status += (title + " has ended\n")

    myWatchlist.send_email_update(update_status)
    myWatchlist.output_current_watchlist()




