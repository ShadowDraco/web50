from .models import User, Listing, Bid, Category
from django import forms

class ListingForm(forms.Form):
    title = forms.CharField(label="title", max_length=35)
    description = forms.CharField(label="description", widget=forms.Textarea, max_length=256)
    starting_bid = forms.FloatField(label="starting bid")
    image = forms.URLField(label="image URL")
    category = forms.IntegerField(label="category")

def getAllListings():
    listings = []
    try:
        listings = Listing.objects.all().filter(active=True)
    except LookupError:
        listings = None
    
    return listings

def getAllCategories():
    categories = []
    try:
        categories = Category.objects.all()
    except LookupError:
        categories = None
    
    return categories

def getUserWatchlist(user):
    user_watchlist = []
    try:
        user_watchlist = user.watchlist.all()
    except:
        user_watchlist = None
    
    return user_watchlist

def getListingData(listing_id):
    try:
        listing = Listing.objects.get(id=listing_id)    
        listing_bids = Bid.objects.all().filter(listing=listing).order_by("-amount").values()
        top_bidder = getTopBidder(listing_bids, True)

        if listing_bids.first():
            highest_bid = listing_bids.first()["amount"]
        else:
            highest_bid = listing.starting_bid

    except LookupError:
        listing = None

    return {  "listing": listing,
        "highest_bid": highest_bid,
        "listing_bids": listing_bids,
        "top_bidder": top_bidder, 
        "message": "" }

def getTopBidder(listing_bids, username=False):
    user = "N/A"
    try: 
        user = User.objects.get(id=listing_bids.first()["bidder_id"])
        if username:
            return user.username
        else: 
            print('no username')
            return user
    except:
        # exception will occur when there are no bids, Not an issue
        return user
  