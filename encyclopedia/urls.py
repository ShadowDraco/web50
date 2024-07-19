from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("random", views.randomEntry, name="random"),
    path("new", views.new, name="new"),
    path("edit/<str:title>", views.edit, name="edit"),
    path("<str:title>", views.entry, name="entry"),
]
