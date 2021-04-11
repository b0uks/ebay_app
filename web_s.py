#This will not run on online IDE
from ebay_class import *

def get_listing_info(listing):
    listing.title = listing.findTitle(listing.soup)
    listing.price = listing.findPrice(listing.soup)
    listing.quant = listing.findQuantity(listing.soup)
    listing.shipping = listing.findShipping(listing.soup)
    listing.lupdate = listing.lastUpdate(listing.soup)


def main():

    list_listings = [
        "https://www.ebay.com/itm/Sports-Illustrated-COMMEMORATIVE-2019-New-England-Patriots-Super-Bowl-CHAMPIONS/163526245987?_trkparms=aid%3D1110006%26algo%3DHOMESPLICE.SIM%26ao%3D1%26asc%3D20201210111314%26meid%3Da65c0b3daa6e44e0986f2204c4a2b96d%26pid%3D101195%26rk%3D3%26rkt%3D12%26mehot%3Dpf%26sd%3D203300682401%26itm%3D163526245987%26pmt%3D1%26noa%3D0%26pg%3D2047675%26algv%3DSimplAMLv9PairwiseUnbiasedWeb&_trksid=p2047675.c101195.m1851",
        "https://www.ebay.com/itm/Sports-Illustrated-Commemorative-Miami-Heat-2013-Champions-Lebron-James-NEW/203300682401?hash=item2f55aa3aa1:g:gLQAAOSw8bhgSA7p",
        "https://www.ebay.com/itm/Sports-Illustrated-Philadelphia-Eagles-2018-Super-Bowl-Champions-Nick-Foles/163487866511?_trkparms=aid%3D1110006%26algo%3DHOMESPLICE.SIM%26ao%3D1%26asc%3D20201210111314%26meid%3D2a03c6dc4cb5404f9312d8249157bd8d%26pid%3D101195%26rk%3D5%26rkt%3D12%26mehot%3Dpf%26sd%3D163526245987%26itm%3D163487866511%26pmt%3D1%26noa%3D0%26pg%3D2047675%26algv%3DSimplAMLv9PairwiseUnbiasedWeb&_trksid=p2047675.c101195.m1851"
    ]

    sold_listing = "https://www.ebay.com/itm/2-Roy-DOC-Halladay-Philadelphia-Phillies-UNSIGNED-Sports-Illustrated-SI-NO-LABEL/232866473309?hash=item3637ec655d:g:hZAAAOSw0JFbXMei"
    url = sold_listing
    
    if (False):
        for url in list_listings: 
            listing = EbayListing(url)
            get_listing_info(listing)
            listing.show_important()
            print(listing.output_csv_format())
            print("")
            break
    else:
        listing = EbayListing()
        listing.populate_from_csv()

        # listing.show_important()


if __name__ == "__main__":
    main()


