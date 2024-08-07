from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Listing, Bid


def index(request):
    listings = []
    try:
        listings = Listing.objects.all()
    except LookupError:
        listings = None

    return render(request, "auctions/index.html", {
        "listings": listings
    })

def listings(request, id):

    if request.method == "POST" and request.user:
        # add selected listing to user's watchlist relation
        listing = Listing.objects.get(id=id)
        user = request.user
        user.watchlist.add(listing)
        user.save()
    else: 
        # send listing data
        listing = None
        try:
            listing = Listing.objects.get(id=id)    
        except LookupError:
            listing = None

    listing_bids = Bid.objects.all().filter(listing=listing).order_by("amount")
    print(listing_bids)
    highest_bid = 10
    return render(request, "auctions/listings.html", {
        "listing": listing,
        "highest_bid": highest_bid,
        "bids": len(listing_bids)
    })

def create_listing(request):
    return render(request, "auctions/create_listing.html")

def watchlist(request):
    user_watchlist = []
    try:
        user_watchlist = request.user.watchlist.all()
    except:
        user_watchlist = None
    
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
