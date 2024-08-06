from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    pass


class Category(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField(max_length=100)
   
    def __str__(self):
        return f"Category: {self.title}"

class Listing(models.Model):
    lister = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings")
    title = models.CharField(max_length=64)
    starting_bid = models.FloatField(max_length=10)
    date = models.DateField(auto_now=True)
    image = models.ImageField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"Listing: {self.title} for ${self.starting_bid}"


class Bid(models.Model):
    amount = models.FloatField()
    bidder = models.ForeignKey(User, related_name="bids", on_delete=models.CASCADE,)
    listing = models.ForeignKey(Listing, verbose_name="Listing the bid was placed on", on_delete=models.CASCADE)
    def __str__(self):
        return f"Bid: {self.amount} for ${self.amount}"

class Comment(models.Model):
    commenter = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE,)
    comment = models.TextField(max_length=150)
    listing = models.ForeignKey(Listing, verbose_name="Listing the comment was placed on", on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Comment from: {self.commenter.username}"
