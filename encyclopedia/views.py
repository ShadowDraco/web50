from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(), "search": util.sort_entries(request.GET.get('q', 'default'))
    })

def entry(request, title):
    return render(request, "encyclopedia/entry.html", {
        "title": title, "data": util.get_entry(title) 
    })

def new(request):
    return render(request, "encyclopedia/new.html", {
        
    })
