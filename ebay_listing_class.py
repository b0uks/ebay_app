import requests
from bs4 import BeautifulSoup
import datefinder
from csv import writer, reader
import pandas as pd
class EbayListing:


    def create_new(self, URL):
        if URL != None:
            r = requests.get(URL)
            soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
            return soup

    def __init__(self, title=None, price=None, shipping=None, end_date=None, ended=None, note=None):
        self.title=title
        self.price=price
        self.shipping=shipping
        self.end_date=end_date
        self.ended=ended
        self.note=note
        self.check_notes()


    def check_notes(self):
        if self.note:
            if str(self.note).find("out of stock") != -1:
                self.ended = "OUT OF STOCK"



    def show_important(self):
        print("Title: " + self.title)
        print("Price: ", self.price)
        print("Shipping: ", self.shipping)
        print("End Date:", self.end_date)
        print("Ended?: ", self.ended)
        print("Note: ", self.note)

    '''
        will create a new entry at the bottom of a given CSV -- will NOT OVERWRITE it will add duplicates
        IF no CSV file exists, it will create a new one with the given name
    '''
    def output_csv_format(self): 
        output_list = [ self.title, str(self.price), str(self.shipping), 
                        str(self.end_date), self.ended, self.note ]
        # print(output_list)
        with open('lt.csv', 'a') as f_obj:
            writer_obj = writer(f_obj)
            writer_obj.writerow(output_list)
            f_obj.close()
        return output_list

    def populate_from_csv(self):  #maybe make the file name variable
        df = pd.read_csv('lt.csv', header=0)
        # print (df)
        for index, row in df.iterrows():
            self.title      = row[0]
            self.price      = row[1]
            self.shipping   = row[2]
            self.end_date   = row[3]
            self.ended      = row[4]
            self.note       = row[5]

