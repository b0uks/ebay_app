from bs4 import BeautifulSoup
import datefinder, glob, os, time
from csv import writer, reader
import pandas as pd
from ebay_watchlist_class import *

# returns a list of files produced from the get_watchlist_html program
def get_watchlist_files(fname):
    files = []
    for file in sorted(glob.glob(fname + "*")):
        print(file)
        files.append(file)
    return files

# CREATE NEW CSV USING WATCHLIST PARSING OF MULTIPLE PAGES
def reset_csv(csv_name):
    try:
        os.remove(csv_name)
        print('deleted csv file: ' + csv_name)
    except:
        print('file does not exist, unable to delete')

# get a list of listings within from the CSV file
def get_current_csv_status(watchlist_obj):
    current_list = watchlist_obj.get_csv_file_listings( watchlist_obj.csv_name )
    return current_list

def create_old_set(old_list):
    old_set = set()
    for listing in old_list:
        old_set.add( (listing.title, listing.ended) )
    return old_set

def get_html_file(fname):
    with open(fname, "r") as f:
        return f.read()

def create_new_set(watchlist_obj):
    new_set = set()
    for listing in watchlist_obj.listings:
        new_set.add( (listing.title, listing.ended) )
    return new_set

def create_email(myWatchlist, dif_set):

    update_status = ""
    for title, ended in dif_set:
        update_status += (title + " has ended\n")

    myWatchlist.send_email_update(update_status)

def parse_all_pages(myWatchlist, files):
    for file_name in files:
        print(file_name)
        myWatchlist.change_html_file( get_html_file( file_name ) )
        myWatchlist.find_listings()
    myWatchlist.output_current_watchlist('w')

def main():
    csv_name = 'abo.csv'
    files = get_watchlist_files( fname )
    html = get_html_file( files[0] )
    myWatchlist = EbayWatchlist( html, csv_name )
    old_list = get_current_csv_status( myWatchlist )
    if old_list:
        old_set = create_old_set(old_list)
    else:
        old_set = set()
    
    reset_csv( csv_name )
    # time.sleep(2)
    # print(files)
    
    parse_all_pages(myWatchlist, files)


    new_set = create_new_set( myWatchlist )
    difference = new_set.difference(old_set)

    print(difference)
    create_email(myWatchlist, difference)


if __name__ == "__main__":
    main()