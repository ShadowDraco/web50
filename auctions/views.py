from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import datetime
from .models import User, Listing, Bid
from .lib import *


def index(request):
    listings = getAllListings()
    
    return render(request, "auctions/index.html", {
        "listings": listings
    })

def listings(request, id):

    # Create reusable render data
    listing_data = getListingData(id)

    # Check for form submission
    if request.method == "POST" and request.user:
        # if not bidding, do watchlist logic
        bid_amount = request.POST["bid"]
        if not bid_amount:
            try:
                listing = listing_data["listing"]
                user = request.user
                user.watchlist.add(listing)
                user.save()
            except:
                listing_data["message"] = f"Listing or User may not exist: Error" 
        # Do bid logic
        else:
            try:
                amount = float(bid_amount)
                if amount > listing_data["highest_bid"]:
                    newBid = Bid(amount=amount, bidder=request.user, listing=listing_data["listing"])
                    newBid.save()
                    listing_data = getListingData(id)
                    listing_data["message"] = "Success!" 
                else:
                    listing_data["message"] = "Bid too low!" 
            except ValueError:
                listing_data["message"] = f"Bid could not be completed {ValueError}" 
   
    return render(request, "auctions/listings.html", listing_data)

def create_listing(request):

    form = ListingForm(request.POST)
    categories = getAllCategories()
   
    if request.method == "POST":
        
        try:
            if form.is_valid():
                user = User.objects.get(id=request.user.id)
                title = form.cleaned_data["title"]
                description = form.cleaned_data["description"]
                image = form.cleaned_data["image"]
                starting_bid = form.cleaned_data["starting_bid"]
                category = Category.objects.get(id=form.cleaned_data["category"])
                newListing = Listing(lister=user, title=title, description=description, image=image, starting_bid=starting_bid, category=category)
                newListing.save()
                
                return render(request, "auctions/listings.html", {
                    "listing": newListing,
                    "highest_bid": newListing.starting_bid,
                    "listing_bids": 0
                })
            else:
                return render(request, "auctions/create_listing.html", {
                 "categories": categories,"message": "There is something wrong with your listing."
            })

        except:
            return render(request, "auctions/create_listing.html", {
                "categories": categories, "message": "There is something wrong with your listing."
            })
        

    return render(request, "auctions/create_listing.html", {
        "categories": categories, "message": ""
    })

def watchlist(request):
    user_watchlist = getUserWatchlist()
    
    return render(request, "auctions/watchlist.html", {
        "watchlist": user_watchlist
    })

def categories(request):
    return render(request, "auctions/categories.html")

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
