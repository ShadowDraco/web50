from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("listings/<int:id>", views.listings, name="listings"),
    path("listings/<int:id>/<str:bid_amount>", views.listings, name="bid"),
    path("create-listing", views.create_listing, name="create_listing"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("watchlist/<int:id>", views.add_to_watchlist, name="add_to_watchlist"),
    path("watchlist/<int:id>/remove", views.remove_from_watchlist, name="remove_from_watchlist"),
    path("categories", views.categories, name="categories"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register")
]
