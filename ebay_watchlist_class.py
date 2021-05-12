import requests
from bs4 import BeautifulSoup
import datefinder
from csv import writer, reader
import pandas as pd
from ebay_listing_class import *
import ssl, smtplib
import SMS
fname = "c_html"

#TODO comment this out once we get the other program running
def get_html_file():
    with open(fname, "r") as f:
        return f.read()

# all these methods get data from the watchlist, not the individual listing.
class EbayWatchlist:

    def __init__(self, html_file, csv_name=None):
        self.soup = BeautifulSoup(html_file, "html.parser")
        self.csv_name = csv_name
        if self.csv_name == None:
            self.csv_file = no_file_name_given.csv
        self.listings = []
        self.pages = self.watchlist_pages()

    def watchlist_pages(self):
        pages = []
        pagenation_class = self.soup.find(class_="pagination__items")
        if pagenation_class:
            for count, child in enumerate(pagenation_class.children):
                print(count)

    def change_html_file(self, html_file):
        self.soup = BeautifulSoup(html_file, "html.parser")


    def find_listings(self):
        get_m_items = self.soup.find("div", class_="m-items")
        if not get_m_items:
            print("UNABLE TO GET M ITEMS FROM SOUP FINDING")
            exit()
        all_listings= get_m_items.findChildren("div", class_="m-item")
        for listing in all_listings:
            s = self.get_listing_shipping(listing)
            p = self.get_listing_price(listing)
            n = self.get_listing_note(listing)
            t = self.get_listing_title(listing)
            
            l = self.get_listing_url(listing)
            d = self.get_listing_end_date(listing)
            e = self.get_listing_ended(listing, d)

            currentListing = EbayListing(t, p, s, d, e, n, l)
            # currentListing.show_important()
            self.listings.append(currentListing)
            # print(dir(shipping))

    # MODE refers to either read or write or append, one letter only 'w', 'a', 'r'.
    def output_current_watchlist(self, mode):
        csv_file = self.csv_name
        header = ['TITLE', 'PRICE', 'SHIPPING', 'END_DATE', 'ENDED', 'URL', 'NOTE']
        # print(output_list)
        with open(csv_file, mode) as f_obj:
            writer_obj = writer(f_obj)
            file_size = 0
            if mode == 'w':
                writer_obj.writerow(header)
            for l in self.listings:    
                output_list = [ str(l.title), str(l.price), str(l.shipping), 
                                str(l.end_date), str(l.ended), l.url, l.note ]
                writer_obj.writerow(output_list)
            f_obj.close()

    def get_csv_file_listings(self, csv_name=None):
        if csv_name == None:
            csv_name = self.csv_name
        try:
            old_listings = []
            df = pd.read_csv(csv_name, header=0)
            for index, row in df.iterrows():
                listing = EbayListing()
                listing.title      = row[0]
                listing.price      = row[1]
                listing.shipping   = row[2]
                listing.end_date   = row[3]
                listing.ended      = row[4]
                listing.url        = row[5]
                listing.note       = row[6]
                old_listings.append(listing)
            return old_listings
        except IOError:
            print("File not found")

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
        end_date = listing.find(class_="info-time")
        if end_date:
            time = end_date.findChild(class_="BOLD")
            if time:
                x = time.text
            else:
                x = end_date.text   #special case where info-time does not have child with time value

        else:
            end_date = listing.find(class_="info-timer")
            if end_date:
                time = end_date.findChild(class_="DEFAULT")
                if time:
                    x = time.text
                    
        return x

    def get_listing_ended(self, listing, end_date):
        x = 'LIVE'
        ended = listing.findChild(class_="NEGATIVE")
        if ended:
            if ended.text == 'ENDED':
                x = ended.text
            else:
                x = 'uncertain'
                week = ["monday", 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
                for days in week:
                    if days in str(end_date).lower():
                        x = 'LIVE'
                        break
                        
        return x

    def get_listing_url(self, listing):
        url = listing.find('a', href=True)['href']
        return url

    def send_email_update(self, message):
        port = 465
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(SMS.sending_email, SMS.sending_pass)

            server.sendmail(SMS.sending_email, SMS.rec_email, SMS.mess + message)