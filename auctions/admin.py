from django.contrib import admin
from .models import User, Bid, Category, Comment, Listing
# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    list_display = ("id", "lister", "title")
    fields = ("lister", "title", "description", "starting_bid", "image", "closed", "active", "winner", "category")

admin.site.register(User)
admin.site.register(Bid)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Listing, ListingAdmin)